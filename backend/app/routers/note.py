from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
from app.core.security import get_current_user

def get_note_or_404(
        note_id : int,
        db :  Session ,
        current_user 
):
    note = db.query(Note).filter(Note.id == note_id).first()  
    if not note:
        raise HTTPException(
            status_code= 404,
            detail= "Note not found"
        )
    if note.user_id != current_user.id :
        raise HTTPException(
            status_code= 403,
            detail= "Not authorized"
        )
    return note

router = APIRouter()

@router.post("/notes", response_model=NoteResponse) 
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_note = Note(
        title = note.title,
        content = note.content,
        user_id=current_user.id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

@router.get("/notes", response_model= list[NoteResponse])
def get_notes(
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    notes = db.query(Note).filter(Note.user_id == current_user.id).all()
    return notes

@router.get("/notes/{note_id}", response_model= NoteResponse)
def get_note(
    note_id : int,
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    note = get_note_or_404(note_id, db, current_user)
    return note

@router.put("/notes/{note_id}", response_model= NoteResponse)
def update_note(
    note_id : int,
    note_data : NoteUpdate,
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    note = get_note_or_404(note_id, db, current_user)
    note.title = note_data.title
    note.content = note_data.content

    db.commit()
    db.refresh(note)
    return note

@router.delete("/notes/{note_id}", response_model= NoteResponse)
def delete_note(
    note_id: int,
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    note = get_note_or_404(note_id, db, current_user)
    db.delete(note)
    db.commit()
    return note