import re


OTP_STORE = {}

PAN_RE = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
AADHAAR_RE = re.compile(r"^\d{12}$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
OTP_RE = re.compile(r"^\d{4,6}$")

def validate_pan(pan: str) -> bool:
    return bool(PAN_RE.match(pan or ""))

def validate_aadhaar(aadhaar: str) -> bool:
    return bool(AADHAAR_RE.match(aadhaar or ""))

def validate_email(email: str | None) -> bool:
    if not email:
        return True
    return bool(EMAIL_RE.match(email))
    
def validate_otp(otp: str | None) -> bool:
    if not otp:
        return True
    return bool(OTP_RE.match(otp))
