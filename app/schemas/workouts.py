
from pydantic import BaseModel, ConfigDict
import datetime

class WorkoutCreate(BaseModel):
    title: str
    date: datetime.date
    notes: str | None = None

class WorkoutUpdate(BaseModel):
    title: str | None = None
    date: datetime.date | None = None
    notes: str | None = None

class WorkoutResponse(BaseModel):
    id: int
    title: str
    date: datetime.date
    notes: str | None
    created_at: datetime.datetime
    user_id: int
    model_config = ConfigDict(from_attributes=True)
