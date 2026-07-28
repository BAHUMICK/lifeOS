from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from app.database.database import Base

class Task(Base):
    __tablename__ = "tasks"