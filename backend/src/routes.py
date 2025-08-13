import json
import os
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Submission
from .validation import validate_aadhaar, validate_pan, validate_email, validate_otp

router = APIRouter()

class SubmissionIn(BaseModel):
    aadhaar: str = Field(...)
    otp: str | None = None
    pan: str = Field(...)
    name: str | None = None
    email: str | None = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/schema")
def get_schema():
    schema_path = os.getenv("SCHEMA_PATH", os.path.join(os.path.dirname(__file__), "..", "..", "scraping", "schema.json"))
    schema_path = os.path.abspath(schema_path)
    if not os.path.exists(schema_path):
        raise HTTPException(404, detail="schema.json not found. Run the scraper.")
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)

@router.post("/submit")
def submit(data: SubmissionIn, db: Session = Depends(get_db)):
    if not validate_aadhaar(data.aadhaar):
        raise HTTPException(status_code=400, detail="Invalid Aadhaar")
    if not validate_pan(data.pan):
        raise HTTPException(status_code=400, detail="Invalid PAN")
    if not validate_email(data.email):
        raise HTTPException(status_code=400, detail="Invalid Email")
    if not validate_otp(data.otp):
        raise HTTPException(status_code=400, detail="Invalid OTP")

    sub = Submission(aadhaar=data.aadhaar, otp=data.otp, pan=data.pan, name=data.name, email=data.email)
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return {"id": sub.id, "message": "saved"}
