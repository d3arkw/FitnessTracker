from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.exercises import (ExerciseCreate, ExerciseUpdate, ExerciseResponse)
from app.services.exercise_service import get_exercises, create_exercise, delete_exercise, update_exercise
from app.dependencies import get_db, get_current_user
from app.models.user import User

router = APIRouter(tags=["exercises"], prefix="/exercises")


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)) -> list[ExerciseResponse]:
    return await get_exercise(db=db, current_user=current_user)


@router.post("/")
async def create(exercise_data: ExerciseCreate, current_user: User = Depends(get_current_user),
                 db: AsyncSession = Depends(get_db)) -> ExerciseResponse:
    return await create_exercise(db=db, exercise=exercise_data, current_user=current_user)


@router.put("/{exercise_id}")
async def update(exercise_id: int, exercise_data: ExerciseUpdate, current_user: User = Depends(get_current_user),
                 db: AsyncSession = Depends(get_db)) -> ExerciseResponse:
    return await update_exercise(db=db, exercise_id=exercise_id, exercise_data=exercise_data, current_user=current_user)


@router.delete("/{exercise_id}")
async def delete(exercise_id: int, current_user: User = Depends(get_current_user),
                 db: AsyncSession = Depends(get_db)):
    return await delete_exercise(exercise_id=exercise_id, current_user=current_user, db=db)
