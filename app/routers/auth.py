from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import register_user, login_user

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_db)) -> UserResponse:
    new_user = await register_user(db, user_data)
    return new_user


@router.post("/login")
async def login(db: AsyncSession = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_user(db=db, email=form_data.username, password=form_data.password)


@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return current_user
