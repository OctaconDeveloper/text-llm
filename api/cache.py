import redis.asyncio as redis
import json
from .config import REDIS_URL, CACHE_TTL

class CacheManager:
    def __init__(self):
        self.redis = None

    async def connect(self):
        if not self.redis:
            self.redis = redis.from_url(REDIS_URL, decode_responses=True)

    async def get(self, key):
        await self.connect()
        data = await self.redis.get(key)
        return json.loads(data) if data else None

    async def set(self, key, value, ttl=CACHE_TTL):
        await self.connect()
        await self.redis.set(key, json.dumps(value), ex=ttl)

    async def delete(self, key):
        await self.connect()
        await self.redis.delete(key)

cache = CacheManager()
