from fastapi import APIRouter, Query
from src.core.policy_engine import build_policy, simulate_policy, apply_policy
from src.core.audit_trail import log_audit

router = APIRouter()

@router.post("/build")
def build(policy: dict):
    return build_policy(policy)

@router.post("/simulate")
def simulate(policy: dict):
    return simulate_policy(policy)

@router.post("/apply")
def apply(policy: dict):
    result = apply_policy(policy)
    log_audit(user_id="admin", action="policy_apply", sources=["policy"], policies=[policy["name"]], masks=[], latency=0.1, cost=0.0)
    return result
