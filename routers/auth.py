from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.user import UserCreate, UserResponse
from services.auth_service import register_user,login_user
from app.database import get_db
from app.dependencies import get_current_user
from models.user import User

router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/register")
async def register(user_data: UserCreate,db: AsyncSession = Depends(get_db)) ->UserResponse:
    new_user = await register_user(db,user_data)
    return new_user

@router.post("/login")
async def login(db: AsyncSession = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_user(db = db, email = form_data.username, password = form_data.password)

@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return current_user