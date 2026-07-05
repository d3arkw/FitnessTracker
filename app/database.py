from app.config import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT)

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(autoflush=False, bind=engine,expire_on_commit=False)
Base = declarative_base()