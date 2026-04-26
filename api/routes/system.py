import os
import glob
from fastapi import APIRouter
from ..config import MODELS_DIR, PROFILES_DIR, MODEL_ALIASES, MODEL_DESCRIPTIONS, N_CTX, N_THREADS
from ..llm_manager import manager

router = APIRouter()

@router.get("/health")
async def health():
    files = glob.glob(os.path.join(MODELS_DIR, "*.gguf"))
    available_models = [os.path.basename(f) for f in files if "active_model.gguf" not in f]
    
    model_details = {}
    for alias, filename in MODEL_ALIASES.items():
        if filename in available_models:
            model_details[alias] = {
                "file": filename,
                "quality": MODEL_DESCRIPTIONS.get(alias, "No description available.")
            }
    
    profile_files = glob.glob(os.path.join(PROFILES_DIR, "*.txt"))
    available_profiles = [os.path.basename(f).replace(".txt", "") for f in profile_files]
    
    current_model = manager.get_current_model()
    alias = next((k for k, v in MODEL_ALIASES.items() if v == current_model), "none")
    
    return {
        "status": "ready" if manager.get_llm() else "idle",
        "current_model": current_model or "none",
        "alias": alias,
        "available_models": available_models,
        "model_qualities": model_details,
        "available_profiles": available_profiles,
        "all_aliases": MODEL_ALIASES,
        "n_ctx": N_CTX,
        "n_threads": N_THREADS
    }

@router.get("/models")
async def list_models():
    files = glob.glob(os.path.join(MODELS_DIR, "*.gguf"))
    return {
        "available_models": [os.path.basename(f) for f in files if "active_model.gguf" not in f],
        "current_model": manager.get_current_model()
    }

@router.get("/profiles")
async def list_profiles():
    files = glob.glob(os.path.join(PROFILES_DIR, "*.txt"))
    return {"available_profiles": [os.path.basename(f).replace(".txt", "") for f in files]}
