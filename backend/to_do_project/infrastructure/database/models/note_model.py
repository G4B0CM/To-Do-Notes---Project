from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

from core.entites.note import NoteCreate, NoteRead

Base = declarative_base()

class NoteModel(Base):
    __tablename__ = "note"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String(50), nullable=False)
    note_content : Mapped[str] = mapped_column(Text, nullable= False)
    creation_date : Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_completed : Mapped[bool] = mapped_column(Boolean, nullable=False)

    def to_entity(self) -> NoteRead:
        return NoteRead(
            id = self.id,
            title= self.title,
            note_content= self.note_content,
            creation_date= self.creation_date,
            is_completed= self.is_completed
        )
    
    @staticmethod
    def from_entity(note: NoteCreate) -> "NoteModel":
        return NoteModel(
            title = note.title,
            note_content = note.note_content,
            creation_date = note.creation_date,
            is_completed = note.is_completed
        )