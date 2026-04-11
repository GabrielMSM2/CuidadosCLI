import pytest
from src.manager import MedicationManager


def test_add_medication_success():
    """Testa se um medicamento é adicionado corretamente."""
    manager = MedicationManager()
    med = manager.add_medication("Aspirina", "08:00")

    assert med["name"] == "Aspirina"
    assert med["time"] == "08:00"
    assert len(manager.list_medications()) == 1


def test_add_medication_empty_name():
    """Testa se o sistema bloqueia cadastro sem nome."""
    manager = MedicationManager()
    msg = "O nome do medicamento não pode ser vazio."
    with pytest.raises(ValueError, match=msg):
        manager.add_medication("   ", "08:00")


def test_add_medication_empty_time():
    """Testa se o sistema bloqueia cadastro sem horário."""
    manager = MedicationManager()
    with pytest.raises(ValueError, match="O horário não pode ser vazio."):
        manager.add_medication("Aspirina", "")


def test_list_medications():
    """Testa se a listagem retorna todos os itens cadastrados."""
    manager = MedicationManager()
    manager.add_medication("Aspirina", "08:00")
    manager.add_medication("Dipirona", "14:00")

    meds = manager.list_medications()
    assert len(meds) == 2
    assert meds[0]["name"] == "Aspirina"
    assert meds[1]["name"] == "Dipirona"
