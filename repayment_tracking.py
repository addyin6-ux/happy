# repayment_tracking.py
from fastapi import APIRouter, Depends
from database import get_db
router = APIRouter(prefix="/nbfc/repayments")

@router.get("/summary")
def repayment_summary(db=Depends(get_db)):
    # Placeholder: aggregate repayments per NBFC
    return {"summary": []}
