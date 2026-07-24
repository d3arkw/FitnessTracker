from fastapi import HTTPException
from app.models.workout import Workout
from app.services.workout_service import create_workout, get_workouts, update_workout, delete_workout
from app.schemas.workouts import WorkoutCreate, WorkoutUpdate, WorkoutResponse
from sqlalchemy import select
import pytest
import datetime


@pytest.mark.asyncio
async def test_create_workout(db_session, test_user):
    schema = WorkoutCreate(title="chest day", date=datetime.date(2026, 1, 1), notes="good day")
    result = await create_workout(workout=schema, db=db_session, current_user=test_user)
    assert result is not None
    assert result.title == "chest day"
    query = await db_session.execute(select(Workout).where(Workout.title == "chest day"))
    db_result = query.scalars().first()
    assert db_result is not None
    assert db_result.title == "chest day"
    assert db_result.date == datetime.date(2026, 1, 1)
    assert db_result.notes == "good day"


@pytest.mark.asyncio
async def test_get_workout(db_session, test_user, seed_fitness):
    result = await get_workouts(db_session, test_user)
    assert result is not None
    assert len(result) == 1
    assert result[0].title == "Грудь Понедельник"


@pytest.mark.asyncio
async def test_update_workout(db_session, test_user, seed_fitness):
    schema = WorkoutUpdate(title="test", date=datetime.date(2026, 1, 1), notes="test")
    result = await update_workout(workout_data=schema, db=db_session, current_user=test_user, workout_id=1)
    assert result is not None
    query = await db_session.execute(select(Workout).where(Workout.id == 1))
    db_result = query.scalars().first()
    assert db_result is not None
    assert db_result.title == "test"
    assert db_result.date == datetime.date(2026, 1, 1)
    assert db_result.notes == "test"


@pytest.mark.asyncio
async def test_update_workout_with_incorrect_id(db_session, test_user, seed_fitness):
    schema = WorkoutUpdate(title="test", date=datetime.date(2026, 1, 1), notes="test")
    with pytest.raises(HTTPException) as e:
        await update_workout(workout_data=schema, db=db_session, current_user=test_user, workout_id=99)
    assert e.value.status_code == 404


@pytest.mark.asyncio
async def test_delete_workout(db_session, test_user, only_workout):
    result = await delete_workout(workout_id=1, db=db_session, current_user=test_user)
    assert result is not None
    query = await db_session.execute(select(Workout).where(Workout.id == 1))
    db_result = query.scalars().first()
    assert db_result is None
