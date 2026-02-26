# kyc.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db, User
from security import encrypt_aes, decrypt_aes
from datetime import datetime

router = APIRouter(prefix="/kyc")

class KYCRequest(BaseModel):
    user_id: int
    pan: str = None
    aadhaar: str = None
    voter_id: str = None

@router.post("/submit")
def submit_kyc(req: KYCRequest, db=Depends(get_db)):
    user = db.query(User).filter(User.id == req.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if req.pan:
        user.pan_enc = encrypt_aes(req.pan)
    if req.aadhaar:
        user.aadhaar_enc = encrypt_aes(req.aadhaar)
    if req.voter_id:
        user.voter_id_enc = encrypt_aes(req.voter_id)
    db.add(user); db.commit()
    return {"status": "kyc_saved", "user_id": user.id}
