import httpx
from src.core.config import settings

async def route_query(query: str, dept: str) -> str:
    # короткий вопрос → дешёвая модель
    if len(query) < 100:
        return await call_cheap_model(query)
    # длинный/сложный → дорогая модель
    return await call_expensive_model(query)

async def call_cheap_model(query: str) -> str:
    async with httpx.AsyncClient() as client:
        r = await client.post("https://openrouter.ai/api/v1/chat/completions",
                              headers={"Authorization": f"Bearer {settings.openrouter_key}"},
                              json={"model": "moonshotai/kimi-k2:free", "messages": [{"role": "user", "content": query}]})
        return r.json()["choices"][0]["message"]["content"]

async def call_expensive_model(query: str) -> str:
    async with httpx.AsyncClient() as client:
        r = await client.post("https://openrouter.ai/api/v1/chat/completions",
                              headers={"Authorization": f"Bearer {settings.openrouter_key}"},
                              json={"model": "gpt-4o", "messages": [{"role": "user", "content": query}]})
        return r.json()["choices"][0]["message"]["content"]
