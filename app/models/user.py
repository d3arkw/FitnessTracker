from datetime import datetime

from app.database import Base

from sqlalchemy import Column, Integer, String, DateTime, Date


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    birth_date = Column(Date, nullable=False)
    password_hash = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
