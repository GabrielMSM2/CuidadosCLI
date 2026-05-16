import requests

OPENFDA_URL = "https://api.fda.gov/drug/label.json"


def fetch_medication_info(name):
    """
    Busca informações de um medicamento na API pública OpenFDA.

    Args:
        name (str): Nome do medicamento a ser pesquisado.

    Returns:
        dict | None: Dicionário com dados ou None se não encontrado/erro.
    """
    params = {
        "search": f'openfda.brand_name:"{name}"',
        "limit": 1,
    }
    try:
        response = requests.get(OPENFDA_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        if not results:
            return None
        result = results[0]
        openfda = result.get("openfda", {})
        purpose = result.get("purpose", ["Informação não disponível"])
        return {
            "name": openfda.get("brand_name", [name])[0],
            "manufacturer": openfda.get("manufacturer_name", ["N/A"])[0],
            "purpose": purpose[0][:200],
        }
    except requests.exceptions.RequestException:
        return None