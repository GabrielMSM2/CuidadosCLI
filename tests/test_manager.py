import pytest
from unittest.mock import patch, MagicMock
from src.manager import MedicationManager


@patch("src.manager.create_client")
def test_add_medication_success(mock_create_client):
    mock_create_client.return_value = MagicMock()

    manager = MedicationManager()
    med = manager.add_medication("Aspirina", "08:00")

    assert med["name"] == "Aspirina"
    assert med["time"] == "08:00"


@patch("src.manager.create_client")
def test_add_medication_empty_name(mock_create_client):
    mock_create_client.return_value = MagicMock()

    manager = MedicationManager()
    msg = "O nome do medicamento não pode ser vazio."
    with pytest.raises(ValueError, match=msg):
        manager.add_medication("   ", "08:00")


@patch("src.manager.create_client")
def test_add_medication_empty_time(mock_create_client):
    mock_create_client.return_value = MagicMock()

    manager = MedicationManager()
    with pytest.raises(ValueError, match="O horário não pode ser vazio."):
        manager.add_medication("Aspirina", "")


@patch("src.manager.create_client")
def test_list_medications(mock_create_client):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.data = [
        {"name": "Aspirina", "time": "08:00"},
        {"name": "Dipirona", "time": "14:00"},
    ]
    mock_response_obj = mock_client.table.return_value.select.return_value
    mock_response_obj.execute.return_value = mock_response
