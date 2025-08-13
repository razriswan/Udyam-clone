from pydantic import BaseModel, Field
from typing import Optional

class SubmissionSchema(BaseModel):
    aadhaar: str = Field(...)
    otp: Optional[str]
    pan: str
    name: Optional[str]
    email: Optional[str]