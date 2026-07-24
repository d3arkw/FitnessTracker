from app.services.auth_service import register_user, login_user
from app.models.user import User
from app.schemas.user import UserCreate
import pytest
from sqlalchemy import select
from fastapi import HTTPException
from app.utils.security import hash_password


@pytest.mark.asyncio
async def test_create_user(db_session):
    user = UserCreate(username="denis", email="denis@test.com", password="123456789", birth_date="2008-09-27")
    reg_user = await register_user(db_session, user)
    assert reg_user.id is not None
    assert reg_user.username == "denis"
    assert reg_user.email == "denis@test.com"
    query = await db_session.execute(select(User).where(User.email == "denis@test.com"))
    db_user = query.scalars().first()
    assert db_user is not None
    assert db_user.username == "denis"
    assert db_user.password_hash != "1234556789"


@pytest.mark.asyncio
async def test_create_user_duplicate(db_session, test_user):
    dublicate_user = UserCreate(username="denis", email="denis@test.com", password="123456789", birth_date="2008-09-27")

    with pytest.raises(HTTPException) as e:
        await register_user(db=db_session, user_data=dublicate_user)
    assert e.value.status_code == 409


@pytest.mark.asyncio
async def test_login_user(db_session, test_user):
    logged_user = await login_user(db=db_session, email=test_user.email, password=test_user.raw_password)
    assert logged_user is not None
    assert "access_token" in logged_user
    assert logged_user["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_user_with_invalid_password(db_session, test_user):
    invalid_password = hash_password("111111111")
    with pytest.raises(HTTPException) as e:
        await login_user(db=db_session, email=test_user.email, password=invalid_password)
    assert e.value.status_code == 401
