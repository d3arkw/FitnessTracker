from typing import List

from app.services.statistics_service import get_statistics as get_statistics_service
from app.services.statistics_service import get_best_result as get_best_result_service
from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.statistic import StatisticResponse, BestResult
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["statistics"], prefix="/statistics")

@router.get("", response_model=StatisticResponse)
async def get_statistics(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await get_statistics_service(db=db, current_user=current_user)

@router.get("/bestresult", response_model=List[BestResult])
async def get_best_result(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await get_best_result_service(db=db, current_user=current_user)
