import aioredis
from src.core.config import Config

jti_expiry = 60 * 30  # 30 minutes

redis_token_blocklist = aioredis.StrictRedis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=0,
)


async def add_jti_to_blocklist(jti: str) -> None:
    await redis_token_blocklist.set(name=jti, value="", ex=jti_expiry)


async def token_in_blocklist(jti: str) -> bool:
    jti = await redis_token_blocklist.exists(jti)

    return True if jti else False
