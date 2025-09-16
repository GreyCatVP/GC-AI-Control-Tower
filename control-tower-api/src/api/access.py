from fastapi import APIRouter, Query
from src.core.scim_offboard import offboard_user
from src.core.audit_trail import log_audit

router = APIRouter()

@router.post("/offboard")
def offboard(username: str = Query(...)):
    offboard_user(username)
    log_audit(user_id="admin", action="offboard", sources=["user"], policies=[], masks=[], latency=0.1, cost=0.0)
    return {"message": f"User {username} offboarded → keys deleted, cache cleared"}
