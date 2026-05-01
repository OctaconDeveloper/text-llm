import os
import glob
import uuid
from fastapi import APIRouter, HTTPException, Depends
from ..limiter import RateLimiter
from ..schemas import ChatRequest
from ..config import MODELS_DIR, PROFILES_DIR, MODEL_ALIASES, DEFAULT_SYSTEM_PROMPT, CHAT_RATE_LIMIT, DEFAULT_MODEL_ALIAS
from ..llm_manager import manager
from ..database import get_session_history, save_session_history, get_profile
from ..logger import logger

router = APIRouter()

@router.post("/chat", dependencies=[Depends(RateLimiter(times=int(CHAT_RATE_LIMIT.split('/')[0]), seconds=60))])
async def chat(request: ChatRequest):
    if not request.sessionId:
        request.sessionId = str(uuid.uuid4())
        logger.info("Generated new sessionId", extra={"sessionId": request.sessionId})

    logger.info("Chat request received", extra={"sessionId": request.sessionId, "message_preview": request.message[:50]})

    # 0. Load Profile if profileId is provided
    if request.profileId:
        p_traits = await get_profile(request.profileId)
        if p_traits:
            logger.info("Loaded profile traits", extra={"profileId": request.profileId})
            for key, value in p_traits.items():
                if hasattr(request, key) and getattr(request, key) is None:
                    setattr(request, key, value)
    # 1. Build Base System Prompt
    base_prompt = DEFAULT_SYSTEM_PROMPT
    if request.systemPrompt:
        base_prompt = request.systemPrompt
    elif request.profileName:
        profile_path = os.path.join(PROFILES_DIR, f"{request.profileName}.txt")
        if os.path.exists(profile_path):
            with open(profile_path, "r") as f:
                base_prompt = f.read().strip()

    # 2. Build Persona Description
    identity = []
    if request.name: identity.append(f"Name: {request.name}")
    if request.type: identity.append(f"Type: {request.type}")
    if request.ethnicity: identity.append(f"Ethnicity: {request.ethnicity}")
    elif request.race: identity.append(f"Ethnicity: {request.race}")
    if request.ageRange: identity.append(f"Age: {request.ageRange}")
    if request.sex: identity.append(f"Sex: {request.sex}")

    personality = []
    if request.style: personality.append(f"Interaction Style: {request.style}")
    if request.personality: personality.append(f"Personality: {request.personality}")
    if request.background: personality.append(f"Background: {request.background}")

    physical = []
    if request.bodyType: physical.append(f"Body Type: {request.bodyType}")
    if request.breastStyle: physical.append(f"Breasts: {request.breastStyle}")
    if request.hairStyle: physical.append(f"Hair Style: {request.hairStyle}")
    if request.hairColor: physical.append(f"Hair Color: {request.hairColor}")
    if request.eyeColor: physical.append(f"Eye Color: {request.eyeColor}")
    if request.complexion: physical.append(f"Complexion: {request.complexion}")

    persona_prompt = ""
    if identity: persona_prompt += "\n\n[IDENTITY]\n" + "\n".join(identity)
    if personality: persona_prompt += "\n\n[PERSONALITY & STYLE]\n" + "\n".join(personality)
    if physical: persona_prompt += "\n\n[PHYSICAL DESCRIPTION]\n" + "\n".join(physical)

    final_system_prompt = base_prompt + persona_prompt

    # 3. Model Selection
    requested_model = request.modelName
    if requested_model and requested_model.lower() in MODEL_ALIASES:
        requested_model = MODEL_ALIASES[requested_model.lower()]
    
    current_model = manager.get_current_model()
    if not requested_model:
        if current_model:
            requested_model = current_model
        else:
            requested_model = MODEL_ALIASES.get(DEFAULT_MODEL_ALIAS)
            if not requested_model or not os.path.exists(os.path.join(MODELS_DIR, requested_model)):
                available = glob.glob(os.path.join(MODELS_DIR, "*.gguf"))
                if not available: raise HTTPException(status_code=503, detail="No models found.")
                requested_model = os.path.basename(available[0])

    logger.info("Using model for generation", extra={"model": requested_model})

    # 4. Load Model if switched
    if requested_model != current_model:
        try:
            manager.load_model(requested_model)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    llm = manager.get_llm()
    if llm is None: raise HTTPException(status_code=503, detail="Model not loaded.")
    
    try:
        # 5. Build Context
        messages = [{"role": "system", "content": final_system_prompt}]
        session_history = []
        
        if request.sessionId:
            session_history = await get_session_history(request.sessionId)
            messages.extend(session_history)
        elif request.history:
            messages.extend(request.history)
            
        messages.append({"role": "user", "content": request.message})

        # 6. Generate Response
        logger.info("Starting LLM generation")
        response = llm.create_chat_completion(
            messages=messages, 
            temperature=request.temperature, 
            repeat_penalty=request.repeat_penalty,
            max_tokens=request.max_tokens
        )
        reply = response["choices"][0]["message"]["content"]
        logger.info("Generation finished", extra={"tokens": response['usage']['total_tokens']})
        
        # 7. Persistence
        if request.sessionId:
            session_history.append({"role": "user", "content": request.message})
            session_history.append({"role": "assistant", "content": reply})
            
            # Limit history to 20 by default, or None (no limit) if override is set
            history_limit = None if request.ignoreLimit else 20
            await save_session_history(request.sessionId, session_history, limit=history_limit)

        return {
            "sessionId": request.sessionId, 
            "response": reply, 
            "usage": response["usage"]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
