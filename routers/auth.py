from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserCreate, UserResponse
from services.auth_service import register_user
from app.database import AsyncSessionLocal,get_db

router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/register")
async def register(user_data: UserCreate,db: AsyncSession = Depends(get_db)) ->UserResponse:
    new_user = await register_user(db,user_data)
    return new_user
