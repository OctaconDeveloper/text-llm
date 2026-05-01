import uuid
from fastapi import APIRouter, HTTPException, Depends
from ..limiter import RateLimiter
from ..schemas import ProfileCreate
from ..database import create_profile
from ..config import DEFAULT_RATE_LIMIT
from ..logger import logger

router = APIRouter()

@router.post("/profiles", dependencies=[Depends(RateLimiter(times=int(DEFAULT_RATE_LIMIT.split('/')[0]), seconds=60))])
async def create_new_profile(request: ProfileCreate):
    profile_id = str(uuid.uuid4())
    traits = request.model_dump(exclude_unset=True)
    
    try:
        await create_profile(profile_id, traits)
        logger.info("Created new profile", extra={"profileId": profile_id, "profileName": request.name})
        return {
            "status": "success",
            "profileId": profile_id,
            "traits": traits
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
