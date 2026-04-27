from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    history: Optional[List[dict]] = []
    
    # Persona & Physical Attributes
    name: Optional[str] = None
    style: Optional[str] = None
    ethnicity: Optional[str] = None
    ageRange: Optional[str] = None
    hairStyle: Optional[str] = None
    hairColor: Optional[str] = None
    eyeColor: Optional[str] = None
    bodyType: Optional[str] = None
    breastStyle: Optional[str] = None
    personality: Optional[str] = None
    background: Optional[str] = None
    
    # Legacy / Additional Parameters (keeping for compatibility)
    sex: Optional[str] = None
    race: Optional[str] = None
    complexion: Optional[str] = None
    hair_length: Optional[str] = None
    
    profile_name: Optional[str] = None
    model_name: Optional[str] = None
    system_prompt: Optional[str] = None
    temperature: float = 1.0
    repeat_penalty: float = 1.1
    max_tokens: int = 200

class ChatResponse(BaseModel):
    session_id: Optional[str]
    response: str
    usage: dict
