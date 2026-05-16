import requests
import pytest
from unittest.mock import patch, Mock
from src.api_client import fetch_medication_info


def test_fetch_medication_info_success():
    """
    Teste de integração: valida o fluxo completo quando a API retorna dados.
    Utiliza mock para garantir isolamento e estabilidade no CI.
    """
    mock_data = {
        "results": [
            {
                "openfda": {
                    "brand_name": ["Aspirin"],
                    "manufacturer_name": ["Bayer"],
                },
                "purpose": ["Pain reliever and fever reducer."],
            }
        ]
    }
    mock_response = Mock()
    mock_response.json.return_value = mock_data
    mock_response.raise_for_status.return_value = None

    with patch("src.api_client.requests.get", return_value=mock_response):
        result = fetch_medication_info("Aspirin")

    assert result is not None
    assert result["name"] == "Aspirin"
    assert result["manufacturer"] == "Bayer"
    assert "Pain" in result["purpose"]


def test_fetch_medication_info_not_found():
    """
    Teste de integração: valida o fluxo quando a API não retorna resultados.
    """
    mock_response = Mock()
    mock_response.json.return_value = {"results": []}
    mock_response.raise_for_status.return_value = None

    with patch("src.api_client.requests.get", return_value=mock_response):
        result = fetch_medication_info("MedicamentoInexistente")

    assert result is None


def test_fetch_medication_info_connection_error():
    """
    Teste de integração: valida o tratamento de falha de conexão.
    A aplicação não deve quebrar se a API estiver indisponível.
    """
    with patch(
        "src.api_client.requests.get",
        side_effect=requests.exceptions.ConnectionError,
    ):
        result = fetch_medication_info("Aspirina")

    assert result is None