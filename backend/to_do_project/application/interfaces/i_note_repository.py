from abc import ABC, abstractmethod
from typing import List, Optional

from core.entites.note import NoteCreate, NoteRead

class INoteRepository(ABC):
    @abstractmethod
    def save_note(self, note : NoteCreate) -> NoteRead:
        pass

    @abstractmethod
    def get_all_notes(self) -> List[NoteRead]:
        pass

    @abstractmethod
    def get_by_id(self, note_id:int) -> Optional[NoteRead]:
        pass

    @abstractmethod
    def update_note(self, note_id: int, note_content: NoteCreate) -> Optional[NoteRead]:
        pass

    @abstractmethod
    def delete_note(self, note_id: int) -> bool:
        pass