
from typing import List, Optional
from sqlalchemy.orm import Session
from aplicacion.interfaces.i_note_repository import INoteRepository
from infrastructure.database.models.note_model import NoteModel
from core.entites.note import NoteCreate, NoteRead
'''Llamamos las clases NoteCreate y NoteRead desde el modulo note.py'''
from to_do_project.core.entites.note import NoteCreate, NoteRead, Note


class NoteRepository(INoteRepository):

    def __init__(self, db: Session):
        self.db = db
    #Correciones hechas dentro de los metodos CRUD
    def save_note(self, note: NoteCreate) -> NoteRead:
        note_db = NoteModel.from_entity(note) 
        self.db.add(note_db)                  
        self.db.flush()                       
        self.db.refresh(note_db)              
        return note_db.to_entity()            

    def get_all_notes(self) -> List[NoteRead]:
        return [model.to_entity() for model in self.db.query(NoteModel).all()]

    def get_by_id(self, note_id: int) -> Optional[NoteRead]:
        note_db = self.db.query(NoteModel).filter(NoteModel.id == note_id).first()
        if not note_db:
            return None
        return note_db.to_entity()

    def update_note(self, note_id: int, note_content: NoteCreate) -> Optional[NoteRead]:
        note_db = self.db.query(NoteModel).filter(NoteModel.id == note_id).first()
        if not note_db:
            return None
        note_db.content = note_content.content  # Ajusta según tus atributos reales
        self.db.flush()
        return note_db.to_entity()

    def delete_note(self, note_id: int) -> bool:
        note_db = self.db.query(NoteModel).filter(NoteModel.id == note_id).first()
        if not note_db:
            return False
        self.db.delete(note_db)
        self.db.flush()
        return True
