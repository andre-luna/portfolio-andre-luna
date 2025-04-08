import requests

def converter(valor, de, para):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={de}&to={para}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        taxa = dados["rates"].get(para)

        if taxa:
            print(f"✅ {valor} {de} = {taxa:.2f} {para}")
        else:
            print("❗ Moeda de destino não encontrada.")
    else:
        print("❌ Erro ao acessar a API. Código:", resposta.status_code)

# Teste
converter(100, 'BRL', 'USD')
converter(50, 'USD', 'EUR')
