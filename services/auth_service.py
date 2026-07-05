from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user import User
from schemas.user import UserCreate
from utils.security import hash_password, verify_password
from fastapi import HTTPException
from starlette import status
from utils.jwt import create_access_token

async def register_user(db: AsyncSession, user_data: UserCreate):
    result = await db.execute(
        select(User).where(
            (User.email == user_data.email) |
            (User.username == user_data.username)
        )
    )
    exist_user = result.scalars().first()
    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with that email or username already exists."
        )
    hashed_password = hash_password(user_data.password)

    new_user = User(
        username = user_data.username,
        email = user_data.email,
        password_hash = hashed_password,
        birth_date = user_data.birth_date
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def login_user(db: AsyncSession, email: str, password: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    if not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}