import pytest
from ..test_dependencies import note_create_data, note_read_data, mock_repo, use_case

def test_get_by_id_not_found(use_case, mock_repo):
    # Simulamos que el repo devuelve None
    mock_repo.get_by_id.return_value = None
    
    with pytest.raises(Exception) as excinfo:
        use_case.get_by_id(999)
    
    assert "No se encontró la nota con ID 999" in str(excinfo.value)