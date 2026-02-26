# bank_verification.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db, User
from security import encrypt_aes
router = APIRouter(prefix="/bank")

class BankReq(BaseModel):
    user_id: int
    account_number: str
    ifsc: str

@router.post("/verify")
def verify_bank(req: BankReq, db=Depends(get_db)):
    user = db.query(User).filter(User.id == req.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Placeholder: integrate penny-drop API here
    user.bank_account_enc = encrypt_aes(f"{req.account_number}|{req.ifsc}")
    db.add(user); db.commit()
    return {"status": "bank_verified"}
