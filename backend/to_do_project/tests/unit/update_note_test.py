import pytest
from ..test_dependencies import note_create_data, note_read_data, mock_repo, use_case

def test_update_note_success(use_case, mock_repo, note_create_data, note_read_data):
    # Primero debe encontrar la nota (get_by_id)
    mock_repo.get_by_id.return_value = note_read_data
    # Luego devuelve la nota actualizada
    mock_repo.update_note.return_value = note_read_data
    
    result = use_case.update_note(1, note_create_data)
    
    assert result == note_read_data
    mock_repo.update_note.assert_called_once()