# repayment.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db, LoanApplication
router = APIRouter(prefix="/repayment")

class RepayReq(BaseModel):
    application_id: int
    amount: float

@router.post("/pay")
def pay_emi(req: RepayReq, db=Depends(get_db)):
    app = db.query(LoanApplication).filter(LoanApplication.id == req.application_id).first()
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    # Placeholder: integrate payment gateway
    return {"status": "payment_received"}
