# main.py
from fastapi import FastAPI
from login import app as auth_app
from nbfc_login import app as nbfc_app
from kyc import router as kyc_router
from bank_verification import router as bank_router
from credit_check import router as credit_router
from loan_offers import router as offers_router
from agreement import router as agreement_router
from lead_transfer import router as lead_router
from repayment import router as repayment_router
from api_config import router as api_router
from offer_management import router as offer_mgmt_router
from lead_management import router as lead_mgmt_router
from repayment_tracking import router as repay_track_router

app = FastAPI(title="Loan Marketplace API")

app.mount("/auth", auth_app)
app.mount("/nbfc-auth", nbfc_app)
app.include_router(kyc_router)
app.include_router(bank_router)
app.include_router(credit_router)
app.include_router(offers_router)
app.include_router(agreement_router)
app.include_router(lead_router)
app.include_router(repayment_router)
app.include_router(api_router)
app.include_router(offer_mgmt_router)
app.include_router(lead_mgmt_router)
app.include_router(repay_track_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
