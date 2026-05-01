import redis.asyncio as aioredis
from fastapi import Request, Response, HTTPException, Depends
from starlette.status import HTTP_429_TOO_MANY_REQUESTS
from pyrate_limiter import Duration, Limiter, Rate
from fastapi_limiter.depends import RateLimiter as BaseRateLimiter
from typing import Optional, Callable, Union, List

# Compatibility layer for FastAPILimiter 0.2.0
class FastAPILimiter:
    redis: Optional[aioredis.Redis] = None
    
    @classmethod
    async def init(cls, redis_instance: aioredis.Redis):
        cls.redis = redis_instance

class RateLimiter(BaseRateLimiter):
    def __init__(
        self,
        times: int = 1,
        milliseconds: int = 0,
        seconds: int = 0,
        minutes: int = 0,
        hours: int = 0,
        limiter: Optional[Limiter] = None,
        **kwargs
    ):
        # Calculate interval in ms
        interval = milliseconds + (seconds * 1000) + (minutes * 60000) + (hours * 3600000)
        if interval == 0:
            interval = 1000 # Default to 1 second if not specified
            
        rate = Rate(times, interval)
        
        # If no limiter is provided, we use a simple InMemory Limiter for now.
        # For production-grade Redis state sharing with 0.2.0, 
        # we would need to initialize RedisBucket asynchronously.
        if limiter is None:
            limiter = Limiter(rate)
            
        super().__init__(limiter=limiter, **kwargs)
