import pytest
from ..test_dependencies import note_read_data, mock_repo, use_case

def test_get_by_id_success(use_case, mock_repo, note_read_data):
    mock_repo.get_by_id.return_value = note_read_data
    
    result = use_case.get_by_id(1)
    
    assert result == note_read_data