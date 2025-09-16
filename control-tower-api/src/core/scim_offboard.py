from src.core.audit_trail import log_audit
import redis

redis_client = redis.from_url("redis://redis:6379", decode_responses=True)

def offboard_user(username: str) -> str:
    # удаляем ключи, очищаем кэш, логируем
    redis_client.delete(f"user:{username}")
    redis_client.delete(f"cache:{username}")
    log_audit(user_id="admin", action="offboard", sources=["user"], policies=[], masks=[], latency=0.1, cost=0.0)
    return f"User {username} offboarded → keys deleted, cache cleared"
