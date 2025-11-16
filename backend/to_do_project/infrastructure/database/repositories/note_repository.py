
from typing import List, Optional
from sqlalchemy.orm import Session
from aplicacion.interfaces.i_note_repository import INoteRepository
from infrastructure.database.models.note_model import NoteModel
from core.entites.note import NoteCreate, NoteRead

class NoteRepository(INoteRepository):

    def __init__(self, db : Session):
        self.db = db

    def save_note(self, note : NoteCreate) -> NoteRead:
        note_db = NoteModel.from_entity(note)
        self.db.add(note)
        self.db.flush()
        self.db.refresh(note_db)
        return note_db


    def get_all_notes(self) -> List[NoteRead]:
        return self.db.query(NoteModel).all()

    def get_by_id(self, note_id:int) -> Optional[NoteRead]:
        return self.db.query(NoteModel).filter(NoteModel.id == note_id).first()

    def update_note(self, note_id: int, note_content: NoteCreate) -> Optional[NoteRead]:
        note_db = self.db.query(NoteModel).filter(NoteModel.id == note_id).first()
        note_db.title = note_content.title
        note_db.note_content = note_content.note_content
        note_db.is_completed = note_content.is_completed
        self.db.flush()
        return note_db

    def delete_note(self, note_id: int) -> bool:
        note_db = self.db.query(NoteModel).filter(NoteModel.id == note_id).first()
        self.db.delete(note_db)
        return True