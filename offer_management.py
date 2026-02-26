# offer_management.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db, LoanOffer, NBFC
router = APIRouter(prefix="/nbfc/offers")

class OfferCreate(BaseModel):
    nbfc_id: int
    name: str
    interest_rate: float
    min_amount: float
    max_amount: float
    tenure_months: int

@router.post("/create")
def create_offer(req: OfferCreate, db=Depends(get_db)):
    nbfc = db.query(NBFC).filter(NBFC.id == req.nbfc_id).first()
    if not nbfc:
        raise HTTPException(status_code=404, detail="NBFC not found")
    offer = LoanOffer(nbfc_id=nbfc.id, name=req.name, interest_rate=req.interest_rate, min_amount=req.min_amount, max_amount=req.max_amount, tenure_months=req.tenure_months)
    db.add(offer); db.commit(); db.refresh(offer)
    return {"status": "created", "offer_id": offer.id}
