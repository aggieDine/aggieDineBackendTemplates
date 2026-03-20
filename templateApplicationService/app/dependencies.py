from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_db as _get_db
from app.middleware.auth import get_current_user as _get_current_user

_redis_pool: Redis | None = None


async def get_db() -> AsyncSession:
    async for session in _get_db():
        yield session


async def get_current_user(claims=None) -> dict:
    return await _get_current_user(claims)


async def get_redis() -> Redis:
    global _redis_pool
    if _redis_pool is None:
        _redis_pool = Redis.from_url(settings.REDIS_URL, decode_responses=True)
    return _redis_pool
