from pydantic import BaseModel, EmailStr, Field
from datetime import date

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    birth_date: date

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    birth_date: date
    class Config:
        from_attributes = False