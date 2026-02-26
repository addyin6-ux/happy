# database.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean, LargeBinary, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from config import SettingsFactory

settings = SettingsFactory()
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(20), unique=True, index=True, nullable=False)
    role = Column(String(20), default="borrower")
    created_at = Column(DateTime, default=datetime.utcnow)
    pan_enc = Column(LargeBinary, nullable=True)
    aadhaar_enc = Column(LargeBinary, nullable=True)
    voter_id_enc = Column(LargeBinary, nullable=True)
    bank_account_enc = Column(LargeBinary, nullable=True)

class NBFC(Base):
    __tablename__ = "nbfcs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password_hash = Column(String(300), nullable=False)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    api_configs = relationship("APIConfig", back_populates="nbfc")

class APIConfig(Base):
    __tablename__ = "api_configs"
    id = Column(Integer, primary_key=True, index=True)
    nbfc_id = Column(Integer, ForeignKey("nbfcs.id"))
    provider = Column(String(100))
    credentials_enc = Column(LargeBinary)
    nbfc = relationship("NBFC", back_populates="api_configs")

class LoanOffer(Base):
    __tablename__ = "loan_offers"
    id = Column(Integer, primary_key=True, index=True)
    nbfc_id = Column(Integer, ForeignKey("nbfcs.id"))
    name = Column(String(200))
    interest_rate = Column(Float)
    min_amount = Column(Float)
    max_amount = Column(Float)
    tenure_months = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

class LoanApplication(Base):
    __tablename__ = "loan_applications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    offer_id = Column(Integer, ForeignKey("loan_offers.id"))
    status = Column(String(50), default="pending")
    applied_at = Column(DateTime, default=datetime.utcnow)
    cibil_score = Column(Integer, nullable=True)
    decision_notes = Column(Text, nullable=True)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    actor = Column(String(200))
    action = Column(String(200))
    details = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
