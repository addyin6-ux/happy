# lead_management.py
from fastapi import APIRouter, Depends, HTTPException
from database import get_db, LoanApplication
router = APIRouter(prefix="/nbfc/leads")

@router.get("/list")
def list_leads(db=Depends(get_db)):
    leads = db.query(LoanApplication).filter(LoanApplication.status == "sent_to_nbfc").all()
    return {"leads": [{"id": l.id, "user_id": l.user_id, "offer_id": l.offer_id, "applied_at": l.applied_at.isoformat()} for l in leads]}

@router.post("/decide")
def decide_lead(lead_id: int, approve: bool, db=Depends(get_db)):
    lead = db.query(LoanApplication).filter(LoanApplication.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    lead.status = "approved" if approve else "rejected"
    db.add(lead); db.commit()
    return {"status": lead.status}
