from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class ChatRequest(BaseModel):
    message: str
    sessionId: Optional[str] = None
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
    type: Optional[str] = None
    
    # Legacy / Additional Parameters (keeping for compatibility)
    sex: Optional[str] = None
    race: Optional[str] = None
    complexion: Optional[str] = None
    hair_length: Optional[str] = None
    
    profileName: Optional[str] = None
    profileId: Optional[str] = None
    modelName: Optional[str] = None
    systemPrompt: Optional[str] = None
    temperature: float = 1.0
    repeat_penalty: float = 1.1
    max_tokens: int = 200
    ignoreLimit: bool = False

class ProfileCreate(BaseModel):
    name: str
    style: str
    sex: str
    type: str
    ethnicity: Optional[str] = None
    ageRange: Optional[str] = None
    hairStyle: Optional[str] = None
    hairColor: Optional[str] = None
    eyeColor: Optional[str] = None
    bodyType: Optional[str] = None
    breastStyle: Optional[str] = None
    personality: Optional[str] = None
    background: Optional[str] = None
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Mistress Elena",
                "style": "Dominant and sophisticated",
                "ethnicity": "Latin",
                "ageRange": "20-34",
                "sex": "Female",
                "type": "human | anime",
                "hairStyle": "Long curly",
                "personality": "Strict but fair, highly intelligent",
                "hairColor": "Black",
                "eyeColor": "Emerald Green",
                "bodyType": "Thick",
                "breastStyle": "large",
                "background": "Born in the slums of argentina, went to a public school, became an adult star earlier in life"
            }
        }
    }
    
    # Keeping these for internal compatibility if needed, though not in the user's model
    race: Optional[str] = None
    complexion: Optional[str] = None
    hair_length: Optional[str] = None

class ChatResponse(BaseModel):
    sessionId: Optional[str]
    response: str
    usage: dict
