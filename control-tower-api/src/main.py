from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.api.cost import router as cost_router
from src.api.risk import router as risk_router
from src.api.access import router as access_router
from src.api.audit import router as audit_router
from src.core.config import settings

app = FastAPI(title="AI Control Tower", version="1.0.0")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

app.include_router(cost_router, prefix="/cost", tags=["cost"])
app.include_router(risk_router, prefix="/risk", tags=["risk"])
app.include_router(access_router, prefix="/access", tags=["access"])
app.include_router(audit_router, prefix="/audit", tags=["audit"])

@app.get("/")
def root():
    return {"message": "AI Control Tower — 1 screen to rule all company AIs"}
