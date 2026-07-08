from app.database import AsyncSessionLocal
from app.models.user import User
from app.utils.jwt import decode_access_token

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        result = await db.execute(select(User).where(User.id == int(user_id)))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except Exception as e:
        print("-----ОШИБКА-----:", repr(e))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate or retrieve user")