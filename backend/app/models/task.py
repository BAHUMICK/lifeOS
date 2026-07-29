from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.database.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, nullable= False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default= False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default= datetime.utcnow)
    user = relationship("User", back_populates= "tasks")