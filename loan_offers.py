# loan_offers.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db, LoanOffer
router = APIRouter(prefix="/offers")

class OfferQuery(BaseModel):
    amount: float
    tenure_months: int

@router.post("/search")
def search_offers(q: OfferQuery, db=Depends(get_db)):
    offers = db.query(LoanOffer).filter(LoanOffer.min_amount <= q.amount, LoanOffer.max_amount >= q.amount, LoanOffer.tenure_months == q.tenure_months).all()
    result = [{"id": o.id, "nbfc_id": o.nbfc_id, "interest_rate": o.interest_rate, "name": o.name} for o in offers]
    return {"offers": result}
