from app.schemas.exercises import ExerciseCreate, ExerciseUpdate, ExerciseResponse
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from starlette import status
from app.models.exercise import Exercise
from app.models.user import User


async def create_exercise(exercise: ExerciseCreate, db: AsyncSession, current_user: User):
    new_exercise = Exercise(name=exercise.name, description=exercise.description, muscle_group=exercise.muscle_group,
                            user_id=current_user.id)
    db.add(new_exercise)
    await db.commit()
    await db.refresh(new_exercise)
    return new_exercise


async def get_exercises(db: AsyncSession, current_user: User):
    result = await db.execute(select(Exercise).where(Exercise.user_id == current_user.id))
    exercises = result.scalars().all()
    return exercises


async def update_exercise(db: AsyncSession, current_user: User, exercise_id: int, exercise_data: ExerciseUpdate):
    result = await db.execute(select(Exercise).where(Exercise.id == exercise_id, Exercise.user_id == current_user.id))
    exercise = result.scalars().first()
    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
    exercise.name = exercise_data.name
    exercise.description = exercise_data.description
    exercise.muscle_group = exercise_data.muscle_group
    await db.commit()
    await db.refresh(exercise)
    return exercise


async def delete_exercise(db: AsyncSession, current_user: User, exercise_id: int):
    result = await db.execute(select(Exercise).where(Exercise.id == exercise_id, Exercise.user_id == current_user.id))
    exercise = result.scalars().first()
    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
    await db.delete(exercise)
    await db.commit()
    await db.refresh(exercise)
    return {"message": "Exercise deleted"}