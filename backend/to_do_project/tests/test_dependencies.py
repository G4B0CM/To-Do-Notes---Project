import pytest
from unittest.mock import Mock
from datetime import datetime
from core.entites.note import NoteCreate, NoteRead
from application.use_cases.crud_note_use_case import CrudNoteUseCase

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