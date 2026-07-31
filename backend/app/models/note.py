from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.database.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, nullable=False)
    content= Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="notes")
    
