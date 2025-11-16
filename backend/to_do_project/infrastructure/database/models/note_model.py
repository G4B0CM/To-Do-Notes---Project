from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import declarative_base

from core.entites.note import NoteRead

Base = declarative_base()

class NoteModel(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    note_content = Column(Text, nullable= False)
    creation_date = Column(DateTime, nullable=False)
    is_completed = Column(Boolean, nullable=False)

    def to_entity(self) -> NoteRead:
        return NoteRead(
            id = self.id,
            title= self.title,
            note_content= self.note_content,
            creation_date= self.creation_date,
            is_completed= self.is_completed
        )
    
    @staticmethod
    def from_entity(note: NoteRead) -> "NoteModel":
        return NoteModel(
            title = note.title,
            note_content = note.note_content,
            creation_date = note.creation_date,
            is_completed = note.is_completed
        )