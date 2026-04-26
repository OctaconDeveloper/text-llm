import os
import uvicorn
from fastapi import FastAPI
from .database import init_db
from .llm_manager import manager
from .config import MODEL_ALIASES, MODELS_DIR
from .routes import chat, system

app = FastAPI(title="Suggy AI Text Model API")

# Include Routers
app.include_router(chat.router, prefix="/api")
app.include_router(system.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    # 1. Initialize DB
    init_db()
    
    # 2. Eager load Smol (Fastest)
    smol_file = MODEL_ALIASES.get("smol")
    if smol_file and os.path.exists(os.path.join(MODELS_DIR, smol_file)):
        try:
            manager.load_model(smol_file)
        except Exception as e:
            print(f"Startup Error: Could not load Smol: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
