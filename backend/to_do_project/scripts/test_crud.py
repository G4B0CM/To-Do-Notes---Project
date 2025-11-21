from core.entites.note import NoteCreate
from core.repositories.sqlite_note_repository import SQLiteNoteRepository

def main():
    repo = SQLiteNoteRepository()

    # Crear nota
    note = repo.save_note(NoteCreate(content="Mi primera nota"))
    print("Creada:", note)

    # Leer todas las notas
    all_notes = repo.get_all_notes()
    print("Todas:", all_notes)

    # Leer por ID
    note_by_id = repo.get_by_id(note.id)
    print("Por ID:", note_by_id)

    # Actualizar nota
    updated = repo.update_note(note.id, NoteCreate(content="Nota actualizada"))
    print("Actualizada:", updated)

    # Eliminar nota
    deleted = repo.delete_note(note.id)
    print("Eliminada:", deleted)

if __name__ == "__main__":
    main()
