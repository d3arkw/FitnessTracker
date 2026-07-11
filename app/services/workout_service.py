from app.schemas.workouts import WorkoutCreate, WorkoutUpdate, WorkoutResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy import select
from starlette import status
from app.models.user import User
from app.models.workout import Workout

async def create_workout(workout: WorkoutCreate, db: AsyncSession,current_user: User):
    new_workout = Workout(title=workout.title, date=workout.date, notes=workout.notes, user_id=current_user.id)
    db.add(new_workout)
    await db.commit()
    await db.refresh(new_workout)
    return new_workout

async def get_workouts(db: AsyncSession,current_user: User):
    result = await db.execute(select(Workout).where(Workout.user_id == current_user.id))
    workouts = result.scalars().all()
    return workouts

async def update_workout(workout_data: WorkoutUpdate, db: AsyncSession,current_user: User,exercise_id: int):
    result = await db.execute(select(Workout).where(Workout.id == exercise_id, Workout.user_id == current_user.id))
    workout = result.scalars().first()
    if not workout:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Workout not found")
    workout.title = workout_data.title
    workout.date = workout_data.date
    workout.notes = workout_data.notes
    await db.commit()
    await db.refresh(workout)
    return workout

async def delete_workout(workout_id: int, db: AsyncSession, current_user: User):
    result = await db.execute(select(Workout).where(Workout.id == workout_id, Workout.user_id == current_user.id))
    workout = result.scalars().first()
    if not workout:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Workout not found")
    await db.delete(workout)
    await db.commit()
    return {"message":"Workout deleted"}