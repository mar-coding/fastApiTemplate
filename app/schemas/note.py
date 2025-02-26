from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteCreationResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: Optional[int] = None

    class Config:
        from_attributes = True
