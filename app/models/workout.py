from app.database import Base
from sqlalchemy import String, Date, ForeignKey, Text,DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import date,datetime


class Workout(Base):
    __tablename__ = "workout"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80),nullable=False)
    date: Mapped[date] = mapped_column(Date,nullable=False)
    notes: Mapped[str] = mapped_column(Text,nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime,nullable=False, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    user: Mapped["User"] = relationship(back_populates="workouts")
