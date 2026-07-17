from app.database import Base

from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column

class WorkoutSet(Base):
    __tablename__ = "workoutset"
    id: Mapped[int] = mapped_column(primary_key=True)
    workout_id: Mapped[int] = mapped_column(ForeignKey('workout.id'))
    exercise_id: Mapped[int] = mapped_column(ForeignKey('exercise.id'))
    weight: Mapped[float| int] = mapped_column(Float, nullable=False)
    reps: Mapped[int]
    set_number: Mapped[int]

    workout: Mapped["Workout"] = relationship("Workout", back_populates="workout_sets")
    exercise: Mapped["Exercise"] = relationship("Exercise", back_populates="workout_sets")
