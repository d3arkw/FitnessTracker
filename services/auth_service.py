from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user import User
from schemas.user import UserCreate
from utils.security import hash_password, verify_password
from fastapi import HTTPException
from starlette import status


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
        password = hashed_password,
        birth_date = user_data.birth_date
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
