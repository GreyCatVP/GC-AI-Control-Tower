import redis
from sentence_transformers import SentenceTransformer
import numpy as np

redis_client = redis.from_url("redis://redis:6379", decode_responses=True)
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_cache_key(query: str) -> str:
    emb = model.encode([query])[0]
    return f"cache:{np.hash(emb.tobytes())}"

def get_cached_answer(query: str) -> str | None:
    key = get_cache_key(query)
    return redis_client.get(key)

def set_cached_answer(query: str, answer: str, ttl: int = 3600):
    key = get_cache_key(query)
    redis_client.setex(key, ttl, answer)
