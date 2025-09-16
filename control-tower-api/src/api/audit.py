from fastapi import APIRouter, Query
from src.core.worm_log import get_worm_logs
from src.core.soc2_mapper import get_soc2_evidence

router = APIRouter()

@router.get("/siem-export")
def siem_export(limit: int = Query(1000, ge=1, le=10000)):
    logs = get_worm_logs(limit)
    evidence = get_soc2_evidence(logs)
    return {"logs": logs, "soc2_evidence": evidence}
