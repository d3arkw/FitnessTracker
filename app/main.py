from app.routers import auth, exercises, workouts, statistics

from fastapi import FastAPI

app = FastAPI()

app.include_router(auth.router)
app.include_router(exercises.router)
app.include_router(workouts.router)
app.include_router(statistics.router)