from pydantic import BaseModel

class StatisticResponse(BaseModel):
    total_workouts: int
    best_bench_press: float
    total_exercises: int
    total_volume: float