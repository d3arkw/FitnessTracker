from app.models.workout import Workout
from app.models.exercise import Exercise
from app.models.workoutset import WorkoutSet
from app.schemas.statistic import StatisticResponse, BestResult
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User


async def get_statistics(db: AsyncSession, current_user: User) -> StatisticResponse:
    result = await db.execute(select(func.count(Workout.id)).where(Workout.user_id == current_user.id))
    total_workouts = result.scalar_one()
    result = await db.execute(select(
        func.max(WorkoutSet.weight)).join(Exercise, WorkoutSet.exercise_id == Exercise.id).where(
        func.lower(Exercise.name) == "bench press"))
    best_bench_press = result.scalar() or 0
    result = await db.execute(select(func.count(func.distinct(WorkoutSet.exercise_id))))
    total_exercises = result.scalar_one()
    result = await db.execute(select(func.sum(WorkoutSet.weight * WorkoutSet.reps)))
    total_volume = result.scalar() or 0
    return StatisticResponse(total_workouts=total_workouts, total_exercises=total_exercises,
                             best_bench_press=best_bench_press, total_volume=total_volume)


async def get_best_result(db: AsyncSession, current_user: User):
    result = await db.execute(
        select(Exercise.name, func.max(WorkoutSet.weight).label("max_weight")).join(WorkoutSet.exercise).join(WorkoutSet.workout).where(Workout.user_id == current_user.id).group_by(Exercise.name,Exercise.id))
    rows = result.all()
    return [BestResult(exercise=row.name, max_weight=row.max_weight) for row in rows]
