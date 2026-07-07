from app.database import Base
from sqlalchemy import String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship,Mapped,mapped_column
from datetime import datetime

class Exercise(Base):
    __tablename__ = 'exercises'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable= False)
    description: Mapped[str] = mapped_column(Text)
    muscle_group: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable= False)
    user: Mapped["User"]= relationship(back_populates="exercises")