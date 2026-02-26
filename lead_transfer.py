# lead_transfer.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db, LoanApplication, LoanOffer
router = APIRouter(prefix="/lead")

class TransferReq(BaseModel):
    application_id: int
    offer_id: int

@router.post("/send")
def send_lead(req: TransferReq, db=Depends(get_db)):
    app = db.query(LoanApplication).filter(LoanApplication.id == req.application_id).first()
    offer = db.query(LoanOffer).filter(LoanOffer.id == req.offer_id).first()
    if not app or not offer:
        raise HTTPException(status_code=404, detail="Application or offer not found")
    app.offer_id = offer.id
    app.status = "sent_to_nbfc"
    db.add(app); db.commit()
    return {"status": "lead_sent", "nbfc_id": offer.nbfc_id}
