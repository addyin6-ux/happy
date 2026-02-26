# api_config.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db, APIConfig, NBFC
from security import encrypt_aes, decrypt_aes
router = APIRouter(prefix="/nbfc/api")

class APIConfigReq(BaseModel):
    nbfc_id: int
    provider: str
    credentials: str

@router.post("/save")
def save_api_config(req: APIConfigReq, db=Depends(get_db)):
    nbfc = db.query(NBFC).filter(NBFC.id == req.nbfc_id).first()
    if not nbfc:
        raise HTTPException(status_code=404, detail="NBFC not found")
    cfg = APIConfig(nbfc_id=nbfc.id, provider=req.provider, credentials_enc=encrypt_aes(req.credentials))
    db.add(cfg); db.commit(); db.refresh(cfg)
    return {"status": "saved", "config_id": cfg.id}
