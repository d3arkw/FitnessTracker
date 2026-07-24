from dotenv import load_dotenv

load_dotenv(".env.test", override=True)
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.models.exercise import Exercise
from app.models.user import User
from app.models.workout import Workout
from app.models.workoutset import WorkoutSet
from app.database import Base
from datetime import date
from app.utils.security import hash_password

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture
async def db_session():
    engine = create_async_engine(TEST_DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        yield session
    await engine.dispose()


@pytest_asyncio.fixture
async def test_user(db_session: AsyncSession):
    raw_password = "123456789"
    user = User(username="denis",
                email="denis@test.com",
                birth_date=date(200, 1, 1),
                password_hash=hash_password(raw_password))
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)
    user.raw_password = raw_password
    return user


@pytest_asyncio.fixture
async def seed_fitness(db_session: AsyncSession, test_user: User):
    bench_press = Exercise(name="Bench Press", description="Жим лежа", muscle_group="Chest", user_id=test_user.id)
    squat = Exercise(name="Squat", description="Приседания", muscle_group="legs", user_id=test_user.id)
    db_session.add_all([bench_press, squat])
    await db_session.commit()

    workout = Workout(title="Грудь Понедельник", date=date(2026, 4, 1), notes="Пошло хорошо", user_id=test_user.id)
    db_session.add(workout)
    await db_session.commit()

    set1 = WorkoutSet(workout_id=workout.id, exercise_id=bench_press.id, weight=100, reps=5, set_number=1)
    set2 = WorkoutSet(workout_id=workout.id, exercise_id=bench_press.id, weight=160, reps=1, set_number=2)
    set3 = WorkoutSet(workout_id=workout.id, exercise_id=squat.id, weight=200, reps=3, set_number=1)
    db_session.add_all([set1, set2, set3])
    await db_session.commit()
    return {"user": test_user, "exercises": [bench_press, squat], "workout": workout, "sets": [set1, set2, set3]}


@pytest_asyncio.fixture
async def only_exercise(db_session: AsyncSession, test_user: User):
    bench_press = Exercise(name="Bench Press", description="Жим лежа", muscle_group="Chest", user_id=test_user.id)
    squat = Exercise(name="Squat", description="Приседания", muscle_group="legs", user_id=test_user.id)
    db_session.add_all([bench_press, squat])
    await db_session.commit()
    return {"user": test_user, "exercises": [bench_press, squat]}


@pytest_asyncio.fixture
async def only_workout(db_session: AsyncSession, test_user: User):
    workout = Workout(title="Грудь Понедельник", date=date(2026, 4, 1), notes="Пошло хорошо", user_id=test_user.id)
    db_session.add(workout)
    await db_session.commit()
    return workout
