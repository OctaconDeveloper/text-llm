import os
import glob
from fastapi import APIRouter, HTTPException
from ..schemas import ChatRequest
from ..config import MODELS_DIR, PROFILES_DIR, MODEL_ALIASES, DEFAULT_SYSTEM_PROMPT
from ..llm_manager import manager
from ..database import get_session_history, save_session_history

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    # 1. Build Base System Prompt
    base_prompt = DEFAULT_SYSTEM_PROMPT
    if request.system_prompt:
        base_prompt = request.system_prompt
    elif request.profile_name:
        profile_path = os.path.join(PROFILES_DIR, f"{request.profile_name}.txt")
        if os.path.exists(profile_path):
            with open(profile_path, "r") as f:
                base_prompt = f.read().strip()

    # 2. Add Dynamic Persona/Physical Profile
    persona_traits = []
    if request.name: persona_traits.append(f"Name: {request.name}")
    if request.style: persona_traits.append(f"Style: {request.style}")
    if request.ethnicity: persona_traits.append(f"Ethnicity: {request.ethnicity}")
    elif request.race: persona_traits.append(f"Ethnicity: {request.race}")
    
    if request.ageRange: persona_traits.append(f"Age Range: {request.ageRange}")
    if request.personality: persona_traits.append(f"Personality: {request.personality}")
    if request.background: persona_traits.append(f"Background: {request.background}")
    
    if request.bodyType: persona_traits.append(f"Body Type: {request.bodyType}")
    if request.breastStyle: persona_traits.append(f"Breast Style: {request.breast_size or request.breastStyle}")
    if request.eyeColor: persona_traits.append(f"Eye Color: {request.eyeColor}")
    if request.hairStyle: persona_traits.append(f"Hair Style: {request.hairStyle}")
    if request.hairColor: persona_traits.append(f"Hair Color: {request.hairColor}")
    
    # Handle legacy fields if not already covered
    if request.sex and not request.style: persona_traits.append(f"Sex: {request.sex}")
    if request.complexion: persona_traits.append(f"Complexion: {request.complexion}")

    final_system_prompt = base_prompt
    if persona_traits:
        final_system_prompt += "\n\nYour Persona Description:\n" + "\n".join(persona_traits)

    # 3. Model Selection
    requested_model = request.model_name
    if requested_model and requested_model.lower() in MODEL_ALIASES:
        requested_model = MODEL_ALIASES[requested_model.lower()]
    
    current_model = manager.get_current_model()
    if not requested_model:
        if current_model:
            requested_model = current_model
        else:
            smol_file = MODEL_ALIASES.get("smol")
            if smol_file and os.path.exists(os.path.join(MODELS_DIR, smol_file)):
                requested_model = smol_file
            else:
                available = glob.glob(os.path.join(MODELS_DIR, "*.gguf"))
                if not available: raise HTTPException(status_code=503, detail="No models found.")
                requested_model = os.path.basename(available[0])

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
        
        if request.session_id:
            session_history = get_session_history(request.session_id)
            messages.extend(session_history)
        elif request.history:
            messages.extend(request.history)
            
        messages.append({"role": "user", "content": request.message})

        # 6. Generate Response
        response = llm.create_chat_completion(
            messages=messages, 
            temperature=request.temperature, 
            repeat_penalty=request.repeat_penalty,
            max_tokens=request.max_tokens
        )
        reply = response["choices"][0]["message"]["content"]
        
        # 7. Persistence
        if request.session_id:
            session_history.append({"role": "user", "content": request.message})
            session_history.append({"role": "assistant", "content": reply})
            save_session_history(request.session_id, session_history)

        return {
            "session_id": request.session_id, 
            "response": reply, 
            "usage": response["usage"]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
