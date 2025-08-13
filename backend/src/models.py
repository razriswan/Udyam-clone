from sqlalchemy import Column, Integer, String
from .database import Base

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    aadhaar = Column(String, nullable=False)
    otp = Column(String, nullable=True)
    pan = Column(String, nullable=False)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)