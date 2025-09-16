from typing import Dict
from src.core.multi_model_router import get_cost_per_1k_tokens, get_latency_p95, get_cache_hit_rate
from src.core.dept_quota import get_quota_burn

def get_cost_report(dept: str, days: int) -> Dict:
    cost = get_cost_per_1k_tokens(dept, days)
    latency = get_latency_p95(dept, days)
    cache = get_cache_hit_rate(dept, days)
    burn = get_quota_burn(dept, days)
    return {
        "dept": dept,
        "cost_per_1k_tokens": cost,
        "latency_p95_ms": latency,
        "cache_hit_rate": cache,
        "quota_burn_percent": burn,
        "recommendation": "Switch to local LLM for simple queries → save 28%"
    }
