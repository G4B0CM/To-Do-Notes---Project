from pydantic import BaseModel, Field
from datetime import datetime

class NoteBase(BaseModel):
    title : str = Field(...,min_length=10, max_length=50)
    note_content : str = Field(..., min_length=10)
    creation_date : datetime = Field(default_factory=datetime.now)
    is_completed : bool = Field(default=False)

class NoteCreate(NoteBase):
    pass

class NoteRead(NoteBase):
    id : int