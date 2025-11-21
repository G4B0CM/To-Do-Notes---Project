import pytest
from ..test_dependencies import note_create_data, note_read_data, mock_repo, use_case

def test_save_note_calls_repository(use_case, mock_repo, note_create_data, note_read_data):
    # Arrange (Preparar)
    mock_repo.save_note.return_value = note_read_data
    
    # Act (Actuar)
    result = use_case.save_note(note_create_data)
    
    # Assert (Verificar)
    mock_repo.save_note.assert_called_once_with(note=note_create_data)
    assert result.id == 1
    assert result.title == note_create_data.title

