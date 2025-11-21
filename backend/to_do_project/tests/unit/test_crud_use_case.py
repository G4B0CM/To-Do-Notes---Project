import pytest
from unittest.mock import Mock
from datetime import datetime

from application.use_cases.crud_note_use_case import CrudNoteUseCase
from core.entites.note import NoteCreate, NoteRead

# Fixtures para configurar datos comunes
@pytest.fixture
def mock_repo():
    return Mock()

@pytest.fixture
def use_case(mock_repo):
    return CrudNoteUseCase(mock_repo)

@pytest.fixture
def note_create_data():
    return NoteCreate(
        title="Nota de prueba unitaria",
        note_content="Contenido suficiente para la prueba",
        is_completed=False
    )

@pytest.fixture
def note_read_data():
    return NoteRead(
        id=1,
        title="Nota de prueba unitaria",
        note_content="Contenido suficiente para la prueba",
        creation_date=datetime.now(),
        is_completed=False
    )

def test_save_note_calls_repository(use_case, mock_repo, note_create_data, note_read_data):
    # Arrange (Preparar)
    mock_repo.save_note.return_value = note_read_data
    
    # Act (Actuar)
    result = use_case.save_note(note_create_data)
    
    # Assert (Verificar)
    mock_repo.save_note.assert_called_once_with(note=note_create_data)
    assert result.id == 1
    assert result.title == note_create_data.title

def test_get_by_id_success(use_case, mock_repo, note_read_data):
    mock_repo.get_by_id.return_value = note_read_data
    
    result = use_case.get_by_id(1)
    
    assert result == note_read_data

def test_get_by_id_not_found(use_case, mock_repo):
    # Simulamos que el repo devuelve None
    mock_repo.get_by_id.return_value = None
    
    # Verificamos que lance la excepción
    with pytest.raises(Exception) as excinfo:
        use_case.get_by_id(999)
    
    assert "No se encontró la nota con ID 999" in str(excinfo.value)

def test_update_note_success(use_case, mock_repo, note_create_data, note_read_data):
    # Primero debe encontrar la nota (get_by_id)
    mock_repo.get_by_id.return_value = note_read_data
    # Luego devuelve la nota actualizada
    mock_repo.update_note.return_value = note_read_data
    
    result = use_case.update_note(1, note_create_data)
    
    assert result == note_read_data
    mock_repo.update_note.assert_called_once()