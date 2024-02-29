import requests
import random


def get_random_proxy():
    return random.choice(lista_proxys())


def lista_proxys():
    url = "https://www.proxy-list.download/api/v1/get?type=https"
    try:

        response = requests.get(url)

        if response.status_code == 200:
            proxies_list = response.text.split("\r\n")

            print("Exemplo de 10 primeiros proxies:")
            return proxies_list[:10]

        else:
            print(f"Erro na solicitação. Código de status: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação: {e}")
