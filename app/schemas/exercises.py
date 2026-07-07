from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ExerciseCreate(BaseModel):
    name: str
    description: str | None = None
    muscle_group: str

class ExerciseUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    muscle_group: str | None = None

class ExerciseResponse(BaseModel):
    id: int
    name: str
    description: str | None
    muscle_group: str
    created_at: datetime
    user_id: int
    model_config = ConfigDict(from_attributes=True)
