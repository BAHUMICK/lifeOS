from pydantic import BaseModel
from datetime import datetime

class CalendarCreate(BaseModel):
    title : str 
    description : str | None = None
    event_date : datetime | None = None

class CalendarUpdate(BaseModel):
    title : str | None = None
    description : str | None = None
    event_date : datetime | None = None

class CalendarResponse(BaseModel):
    id : int  
    title : str 
    description : str | None = None
    event_date :  datetime | None = None
    user_id : int 

    model_config = {
    "from_attributes": True
    } 