from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.workouts import (WorkoutCreate, WorkoutUpdate, WorkoutResponse)
from app.models.user import User
from app.services.workout_service import create_workout, get_workouts, update_workout, delete_workout
from app.dependencies import get_db, get_current_user
from typing import List

router = APIRouter(tags=['Workouts'], prefix="/workouts")


@router.get("/", response_model=List[WorkoutResponse])
async def get(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    await get_workouts(db=db, current_user=current_user)

@router.post("/", response_model=WorkoutResponse)
async def create(workout_data: WorkoutCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    await create_workout(db=db, current_user=current_user, workout=workout_data)

@router.put("/", response_model=WorkoutResponse)
async def update(workout_data: WorkoutUpdate,exercise_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    await update_workout(db=db, exercise_id=exercise_id, workout=workout_data, current_user=current_user)

@router.delete("/")
async def delete(workout_id:int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    await delete_workout(db=db, workout_id=workout_id, current_user=current_user)