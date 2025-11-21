import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infrastructure.database.models.note_model import Base
from infrastructure.database.repositories.note_repository import NoteRepository
from core.entites.note import NoteCreate

# Configuración de DB en memoria para pruebas
@pytest.fixture(scope="function")
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine) # Crea las tablas
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    
    yield session # Entrega la sesión al test
    
    session.close()
    Base.metadata.drop_all(engine)

def test_create_and_retrieve_note(db_session):
    repo = NoteRepository(db_session)
    new_note = NoteCreate(
        title="Integration Test", 
        note_content="Testing SQLite connection",
        is_completed=False
    )
    
    # 1. Guardar
    saved_note = repo.save_note(new_note)
    assert saved_note.id is not None
    
    # 2. Recuperar
    retrieved_note = repo.get_by_id(saved_note.id)
    assert retrieved_note.title == "Integration Test"
    assert retrieved_note.note_content == "Testing SQLite connection"

def test_delete_note(db_session):
    repo = NoteRepository(db_session)
    new_note = NoteCreate(title="To Delete", note_content="Delete me", is_completed=False)
    saved = repo.save_note(new_note)
    
    # Borrar
    result = repo.delete_note(saved.id)
    assert result is True
    
    # Verificar que ya no existe
    assert repo.get_by_id(saved.id) is None