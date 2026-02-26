# nbfc_login.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from database import get_db, NBFC
from security import hash_password, verify_password, create_jwt_token
from sqlalchemy.exc import IntegrityError

app = FastAPI(title="LoanMarketplace - NBFC Auth")

class NBFCSignUp(BaseModel):
    name: str
    email: EmailStr
    password: str

class NBFCLogin(BaseModel):
    email: EmailStr
    password: str

@app.post("/nbfc/signup")
def nbfc_signup(req: NBFCSignUp, db=Depends(get_db)):
    nbfc = NBFC(name=req.name, email=req.email, password_hash=hash_password(req.password))
    db.add(nbfc)
    try:
        db.commit(); db.refresh(nbfc)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"status": "created", "nbfc_id": nbfc.id}

@app.post("/nbfc/login")
def nbfc_login(req: NBFCLogin, db=Depends(get_db)):
    nbfc = db.query(NBFC).filter(NBFC.email == req.email).first()
    if not nbfc or not verify_password(req.password, nbfc.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_jwt_token({"sub": f"nbfc:{nbfc.id}", "role": "nbfc"})
    return {"access_token": token, "token_type": "bearer"}
