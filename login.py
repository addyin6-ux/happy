# login.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
from security import create_jwt_token
from database import get_db, User
from config import SettingsFactory

settings = SettingsFactory()
app = FastAPI(title="LoanMarketplace - Borrower Auth")
OTP_STORE = {}

class PhoneRequest(BaseModel):
    phone: str

class VerifyRequest(BaseModel):
    phone: str
    otp: str

@app.post("/auth/request-otp")
async def request_otp(req: PhoneRequest):
    phone = req.phone.strip()
    if not phone:
        raise HTTPException(status_code=400, detail="Phone required")
    otp = f"{random.randint(100000,999999)}"
    OTP_STORE[phone] = {"otp": otp, "expires": datetime.utcnow() + timedelta(minutes=5)}
    print(f"[DEV] OTP for {phone}: {otp}")
    return {"status": "otp_sent"}

@app.post("/auth/verify-otp")
async def verify_otp(req: VerifyRequest, db=Depends(get_db)):
    record = OTP_STORE.get(req.phone)
    if not record or record["expires"] < datetime.utcnow() or record["otp"] != req.otp:
        raise HTTPException(status_code=401, detail="Invalid or expired OTP")
    user = db.query(User).filter(User.phone == req.phone).first()
    if not user:
        user = User(phone=req.phone, role="borrower")
        db.add(user); db.commit(); db.refresh(user)
    token = create_jwt_token({"sub": str(user.id), "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
