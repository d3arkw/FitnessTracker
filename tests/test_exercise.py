from app.services.exercise_service import create_exercise, get_exercises, update_exercise, delete_exercise
from app.schemas.exercises import ExerciseCreate, ExerciseUpdate, ExerciseResponse
import pytest
from app.models.exercise import Exercise
from fastapi import HTTPException
from sqlalchemy import select


@pytest.mark.asyncio
async def test_create_exercise(db_session, test_user):
    data_exercise = ExerciseCreate(name="test", description="test", muscle_group="test")
    result = await create_exercise(exercise=data_exercise, db=db_session, current_user=test_user)
    assert result is not None
    assert result.name == "test"
    assert result.description == "test"
    assert result.muscle_group == "test"
    assert result.id is not None
    query = await db_session.execute(select(Exercise).where(Exercise.name == "test"))
    db_exercise = query.scalars().first()
    assert db_exercise.name == "test"
    assert db_exercise.description == "test"


@pytest.mark.asyncio
async def test_get_exercise(db_session, test_user, seed_fitness):
    exercises = await get_exercises(db_session, test_user)
    assert exercises is not None
    assert len(exercises) == 2
    assert exercises[0].name == "Bench Press"
    assert exercises[1].name == "Squat"


@pytest.mark.asyncio
async def test_update_exercise(db_session, test_user, seed_fitness):
    shema = ExerciseUpdate(name="test", description="test", muscle_group="test")
    result = await update_exercise(db=db_session, current_user=test_user, exercise_id=1, exercise_data=shema)
    assert result is not None
    query = await db_session.execute(select(Exercise).where(Exercise.id == 1))
    db_exercise = query.scalars().first()
    assert db_exercise.name == "test"
    assert db_exercise.description == "test"


@pytest.mark.asyncio
async def test_update_exercise_with_incorrect_id(db_session, test_user, seed_fitness):
    shema = ExerciseUpdate(name="test", description="test", muscle_group="test")
    with pytest.raises(HTTPException) as e:
        await update_exercise(db=db_session, current_user=test_user, exercise_id=85, exercise_data=shema)
    assert e.value.status_code == 404


@pytest.mark.asyncio
async def test_delete_exercise(db_session, test_user, only_exercise):
    result = await delete_exercise(db=db_session, current_user=test_user, exercise_id=1)
    assert result is not None
    query = await db_session.execute(select(Exercise).where(Exercise.name == "bench_press"))
    db_delete = query.scalars().first()
    assert (db_delete is None)


@pytest.mark.asyncio
async def test_delete_exercise_with_incorrect_id(db_session, test_user, only_exercise):
    with pytest.raises(HTTPException) as e:
        await delete_exercise(db=db_session, current_user=test_user, exercise_id=85)
    assert e.value.status_code == 404
