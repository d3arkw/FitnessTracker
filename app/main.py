from app.routers import auth, exercises

from fastapi import FastAPI

app = FastAPI()

app.include_router(auth.router)
app.include_router(exercises.router)