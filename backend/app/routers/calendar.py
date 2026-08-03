from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.calendar import Calendar
from app.schemas.calendar import CalendarCreate, CalendarUpdate, CalendarResponse
from app.core.security import get_current_user

def get_calendar_or_404(
        calendar_id : int,
        db : Session,
        current_user
):
    calendar = db.query(Calendar).filter(Calendar.id == calendar_id).first()
    if not calendar:
        raise HTTPException(
            status_code= 404,
            detail="Calendar not found"
        )
    if calendar.user_id != current_user.id:
        raise HTTPException(
            status_code= 403,
            detail=" Not authorized"
        )
    return calendar

router = APIRouter()

@router.post("/calendars", response_model= CalendarResponse)
def create_calendar(
    calendar : CalendarCreate,
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_calendar = Calendar(
        title = calendar.title,
        description = calendar.description,
        event_date = calendar.event_date,
        user_id = current_user.id
    )

    db.add(new_calendar)
    db.commit()
    db.refresh(new_calendar)

    return new_calendar

@router.get("/calendars", response_model=list[CalendarResponse])
def get_calendars(
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    calendar = db.query(Calendar).filter(Calendar.user_id == current_user.id).all()
    return calendar

@router.get("/calendars/{calendar_id}", response_model=CalendarResponse)
def get_calendar(
    calendar_id : int,
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    calendar = get_calendar_or_404(calendar_id, db, current_user)
    return calendar

@router.put("/calendars/{calendar_id}", response_model= CalendarResponse)
def update_calendar(
    calendar_id : int,
    calendar_data : CalendarUpdate,
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    calendar = get_calendar_or_404(calendar_id, db, current_user)
    calendar.title = calendar_data.title
    calendar.description = calendar_data.description
    calendar.event_date = calendar_data.event_date
    db.commit()
    db.refresh(calendar)
    return calendar

@router.delete("/calendars/{calendar_id}", response_model= CalendarResponse)
def delete_calendar(
    calendar_id : int,
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    calendar = get_calendar_or_404(calendar_id, db, current_user)
    db.delete(calendar)
    db.commit()
    return calendar