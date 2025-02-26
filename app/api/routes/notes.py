from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import SessionLocal
from app.models.note import Note
from app.models.user import User
from app.schemas.note import NoteCreate, NoteCreationResponse
from app.core.security import verify_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Protected Route:
@router.post("/", response_model=NoteCreationResponse)
def create_note(
    note_data: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(verify_token)
):
    note = Note(title=note_data.title, content=note_data.content, owner_id=current_user.id)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

# ✅ Public Route:
@router.get("/", response_model=List[NoteCreationResponse])
def read_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()
