from sqlalchemy import Column, Integer, String
from app.database.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users" 

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    tasks = relationship("Task", back_populates="user")
    notes = relationship("Note", back_populates="user")

