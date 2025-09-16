from typing import Dict
from src.core.audit_trail import log_audit

def build_policy(policy: Dict) -> Dict:
    return {"policy": policy, "status": "built"}

def simulate_policy(policy: Dict) -> Dict:
    # симуляция: если «юристы ≠ HR» → разрешено
    if policy["who"] == "юристы" and policy["where"] == "HR-документы":
        return {"result": "denied", "reason": "Policy matches restriction"}
    return {"result": "allowed"}

def apply_policy(policy: Dict) -> Dict:
    result = simulate_policy(policy)
    log_audit(user_id="admin", action="policy_apply", sources=["policy"], policies=[policy["name"]], masks=[], latency=0.1, cost=0.0)
    return {"message": "Policy applied", "result": result}
