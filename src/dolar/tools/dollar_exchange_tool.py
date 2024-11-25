from crewai.tools import tool
from datetime import datetime, timedelta
import requests

# Variáveis globais para controle de cache
ultima_consulta = None
cache_dolar = None

@tool
def dollar_exchange_tool() -> str:
    """Consulta a cotação do dólar em relação ao real (USD-BRL), com suporte a cache."""
    global ultima_consulta, cache_dolar
    agora = datetime.now()

    # Verifica se o cache pode ser usado
    if ultima_consulta and (agora - ultima_consulta < timedelta(hours=1)):
        return f"Usando cache: a cotação do dólar é R$ {cache_dolar}"

    # Faz uma nova consulta se o cache não for válido
    url_cotacao = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url_cotacao)
    if resposta.status_code == 200:
        dados = resposta.json()
        cotacao_dolar = dados["USDBRL"]["bid"]
        cache_dolar = cotacao_dolar  # Atualiza o cache
        ultima_consulta = agora  # Atualiza o horário da última consulta
        return f"A cotação atual do dólar é R$ {cotacao_dolar}."
    else:
        return "Erro ao consultar a cotação do dólar."

