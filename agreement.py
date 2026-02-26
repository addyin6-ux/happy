# agreement.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db, LoanApplication
from config import SettingsFactory
router = APIRouter(prefix="/agreement")
settings = SettingsFactory()

class SignReq(BaseModel):
    application_id: int
    aadhaar: str

@router.post("/esign")
def esign(req: SignReq, db=Depends(get_db)):
    app = db.query(LoanApplication).filter(LoanApplication.id == req.application_id).first()
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    # Placeholder: call Aadhaar e-sign API using settings.AADHAAR_ESIGN_URL
    app.status = "signed"
    db.add(app); db.commit()
    return {"status": "signed"}
