import re
import openpyxl
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


def extrair_emails(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        # Faça uma requisição para o site com headers
        response = requests.get(url, headers=headers)

        # Print the response status code for debugging
        print(f"Status code for {url}: {response.status_code}")

        # Verifique se a requisição foi bem-sucedida
        if response and response.status_code == 200:
            # Use BeautifulSoup para analisar o HTML
            soup = BeautifulSoup(response.text, "html.parser")

            # Encontre todos os textos dentro das tags
            all_texts = soup.find_all(text=True)

            # Combine todos os textos em uma única string
            all_text_as_string = " ".join(all_texts)

            # Exemplo de expressão regular para encontrar emails
            email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

            # Encontrar emails usando a expressão regular
            emails_encontrados = re.findall(email_pattern, all_text_as_string)

            time.sleep(5)

            return emails_encontrados if emails_encontrados else []
        else:
            print(f"Erro na requisição")
            return []

    except Exception as e:
        print(f"Erro ao processar {url}: {e}")
        return []


# Lista de sites
lista_sites = [
    "https://www.google.com/search?q=Donald+Nguyen+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=-ifdZZsVk9LWxA_c84bQBQ&iflsig=ANes7DEAAAAAZd02CorLR6N8lG2kWgC5paaMh8xUQeQN&udm=&ved=0ahUKEwib-vmZncqEAxUTqZUCHdy5AVoQ4dUDCA0&uact=5&oq=Donald+Nguyen+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImpEb25hbGQgTmd1eWVuICgg4oCcQGdtYWlsLmNvbeKAnSBPUiDigJxAaG90bWFpbC5jb23igJ0gT1Ig4oCcQHlhaG9vLmNvbeKAnSkgQU5EIEJyYXppbCBzaXRlOmluc3RhZ3JhbS5jb20vSHRQAFhlcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz"
]


# Criar uma lista para armazenar os emails de todos os sites
todos_emails = []

# Iterar sobre a lista de sites e extrair emails
for site in lista_sites:
    emails_site = extrair_emails(site)
    todos_emails.extend(emails_site)


emails_unicos = set(todos_emails)
emails_certos = list(emails_unicos)

# Criar um DataFrame do pandas com a lista de emails
df_emails = pd.DataFrame({"Emails": emails_certos})

# Exportar o DataFrame para um arquivo XLSX
df_emails.to_excel("emails_extraidos.xlsx", index=False)

print("Exportação concluída. Verifique o arquivo 'emails_extraidos.xlsx'.")
