from app.services.statistics_service import get_statistics
from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.statistic import StatisticResponse
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["statistics"], prefix="/statistics")

@router.get("", response_model=StatisticResponse)
async def get_statistics(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await get_statistics(db=db, current_user=current_user)