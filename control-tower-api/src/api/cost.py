from fastapi import APIRouter, Query
from src.core.finops_engine import get_cost_report

router = APIRouter()

@router.get("/report")
def cost_report(dept: str = Query(...), days: int = Query(30)):
    report = get_cost_report(dept, days)
    return report
