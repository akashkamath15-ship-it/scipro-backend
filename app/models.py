from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Signup(Base):
    __tablename__ = "signups"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
