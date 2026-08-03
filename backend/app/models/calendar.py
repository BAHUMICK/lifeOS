from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.database.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Calendar(Base):
    __tablename__ = "Calendars"
    id = Column(Integer, primary_key= True, index=True)
    title = Column(String, nullable= False)
    description = Column(String, nullable= True)
    event_date = Column(DateTime)
    created_at = Column(DateTime, default= datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates= "calendars")
