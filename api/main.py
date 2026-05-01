import os
import uvicorn
from fastapi import FastAPI, Header, HTTPException, status, Request, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, Response, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import redis.asyncio as redis
from .limiter import FastAPILimiter, RateLimiter
from .database import init_db
from .llm_manager import manager
from .config import MODEL_ALIASES, MODELS_DIR, BASE_DIR, REDIS_URL, API_KEYS, DEFAULT_MODEL_ALIAS
from .routes import chat, system, profiles
from .logger import logger

# Security Dependency
async def verify_api_key(request: Request, m_api_key: str = Header(None)):
    if request.method == "POST":
        if not m_api_key or m_api_key not in API_KEYS:
            logger.warning("Invalid or missing API key", extra={"path": request.url.path, "key_provided": m_api_key})
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing API key in m-api-key header"
            )
    return m_api_key

app = FastAPI(title="Suggy AI Text Model API")

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Validation Error Handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error_details = []
    for error in exc.errors():
        field = " -> ".join([str(loc) for loc in error["loc"][1:]])
        message = error["msg"]
        error_details.append(f"Field '{field}': {message}")
    
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "message": "Invalid request parameters provided.",
            "issues": error_details
        },
    )

# Global Catch-all Error Handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error("Unhandled error occurred", extra={"error": str(exc), "path": request.url.path})
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "An unexpected internal error occurred.",
            "details": str(exc)
        },
    )

# Favicon handler
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    file_path = os.path.join(BASE_DIR, "static", "favicon.ico")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return Response(status_code=204)

# Include Routers with Security
app.include_router(chat.router, prefix="/api", dependencies=[Depends(verify_api_key)])
app.include_router(system.router, prefix="/api", dependencies=[Depends(verify_api_key)])
app.include_router(profiles.router, prefix="/api", dependencies=[Depends(verify_api_key)])

@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up")
    # 1. Initialize Redis for Rate Limiting
    try:
        r = redis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
        await FastAPILimiter.init(r)
        logger.info("Redis initialized successfully")
    except Exception as e:
        logger.error("Failed to initialize Redis", extra={"error": str(e)})
    
    # 2. Initialize DB (Async)
    await init_db()
    
    # 3. Eager load default model
    requested_model = MODEL_ALIASES.get(DEFAULT_MODEL_ALIAS)
    if requested_model and os.path.exists(os.path.join(MODELS_DIR, requested_model)):
        try:
            manager.load_model(requested_model)
            logger.info("Default model loaded successfully", extra={"model": requested_model})
        except Exception as e:
            logger.error("Failed to load default model", extra={"error": str(e)})

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down")
    # Add any cleanup logic here (e.g., closing LLM, db connections if needed)
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
