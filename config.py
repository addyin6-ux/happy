import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "LoanMarketplace"
    env: str = os.getenv("ENV", "development")
    jwt_secret: str = os.getenv("JWT_SECRET", "change_this_secret")
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60 * 24 * 7
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    sms_provider_api_key: str = os.getenv("SMS_PROVIDER_API_KEY", "")
    aes_key: str = os.getenv("AES_KEY", "32_byte_aes_key_here_1234567890")
    cibil_api_url: str = os.getenv("CIBIL_API_URL", "")
    aadhaar_esign_url: str = os.getenv("AADHAAR_ESIGN_URL", "")
    payment_gateway_url: str = os.getenv("PAYMENT_GATEWAY_URL", "")

    class Config:
        env_file = ".env"

def SettingsFactory():
    return Settings()
