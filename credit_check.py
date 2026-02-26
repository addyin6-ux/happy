# credit_check.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db, LoanApplication
from config import SettingsFactory
router = APIRouter(prefix="/credit")
settings = SettingsFactory()

class CreditReq(BaseModel):
    application_id: int

@router.post("/cibil")
def cibil_check(req: CreditReq, db=Depends(get_db)):
    app = db.query(LoanApplication).filter(LoanApplication.id == req.application_id).first()
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    # Placeholder: call CIBIL API using settings.CIBIL_API_URL
    app.cibil_score = 700
    db.add(app); db.commit()
    return {"status": "cibil_fetched", "score": app.cibil_score}
