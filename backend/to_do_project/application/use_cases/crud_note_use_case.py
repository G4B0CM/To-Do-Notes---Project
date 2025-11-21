

from typing import List, Optional

from application.interfaces.i_note_repository import INoteRepository
from core.entites.note import NoteCreate, NoteRead


class CrudNoteUseCase:

    def __init__(self, note_repo: INoteRepository):
        self.note_repo = note_repo

    def save_note(self, note : NoteCreate) -> NoteRead:
        return self.note_repo.save_note(note=note)

    def get_all_notes(self) -> List[NoteRead]:
        return self.note_repo.get_all_notes()

    def get_by_id(self, note_id:int) -> Optional[NoteRead]:
        note = self.note_repo.get_by_id(note_id=note_id)
        if not note:
            raise Exception(f"No se encontró la nota con ID {note_id}")
        return note

    def update_note(self, note_id: int, note_content: NoteCreate) -> Optional[NoteRead]:
        note = self.note_repo.get_by_id(note_id=note_id)
        if not note:
            raise Exception(f"No se encontró la nota con ID {note_id}")
        return self.note_repo.update_note(note_id=note_id, note_content=note_content)

    def delete_note(self, note_id: int) -> bool:
        note = self.note_repo.get_by_id(note_id=note_id)
        if not note:
            raise Exception(f"No se encontró la nota con ID {note_id}")
        return self.note_repo.delete_note(note_id=note_id)