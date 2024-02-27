import re
import openpyxl
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


def extrair_emails(url):
    try:
        # Faça uma requisição para o site
        response = requests.get(url)

        # Verifique se a requisição foi bem-sucedida
        if response.status_code == 200:
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

            time.sleep(1)

            return emails_encontrados

    except Exception as e:
        print(f"Erro ao processar {url}: {e}")
        return []


# Lista de sites
lista_sites = [
    "https://www.google.com/search?q=Donald+Nguyen+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=-ifdZZsVk9LWxA_c84bQBQ&iflsig=ANes7DEAAAAAZd02CorLR6N8lG2kWgC5paaMh8xUQeQN&udm=&ved=0ahUKEwib-vmZncqEAxUTqZUCHdy5AVoQ4dUDCA0&uact=5&oq=Donald+Nguyen+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImpEb25hbGQgTmd1eWVuICgg4oCcQGdtYWlsLmNvbeKAnSBPUiDigJxAaG90bWFpbC5jb23igJ0gT1Ig4oCcQHlhaG9vLmNvbeKAnSkgQU5EIEJyYXppbCBzaXRlOmluc3RhZ3JhbS5jb20vSHRQAFhlcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
    "https://www.google.com/search?q=Andrea+Rojas+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=_SfdZfDdE_C-vr0P44uq0A4&iflsig=ANes7DEAAAAAZd02DaYTx_W1Sas6y9aTm-jNsCCidcj1&udm=&ved=0ahUKEwiw0MSbncqEAxVwn68BHeOFCuoQ4dUDCA0&uact=5&oq=Andrea+Rojas+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImlBbmRyZWEgUm9qYXMgKCDigJxAZ21haWwuY29t4oCdIE9SIOKAnEBob3RtYWlsLmNvbeKAnSBPUiDigJxAeWFob28uY29t4oCdKSBBTkQgQnJhemlsIHNpdGU6aW5zdGFncmFtLmNvbS9IkgFQAFhicAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
    "https://www.google.com/search?q=Michael+White+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=ACjdZd_2MOXG1e8Pk9ungAU&iflsig=ANes7DEAAAAAZd02EFEh3juj_9vcoQXcGp7wRk7k6aUs&udm=&ved=0ahUKEwjf9pidncqEAxVlY_UHHZPtCVAQ4dUDCA0&uact=5&oq=Michael+White+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImpNaWNoYWVsIFdoaXRlICgg4oCcQGdtYWlsLmNvbeKAnSBPUiDigJxAaG90bWFpbC5jb23igJ0gT1Ig4oCcQHlhaG9vLmNvbeKAnSkgQU5EIEJyYXppbCBzaXRlOmluc3RhZ3JhbS5jb20vSHVQAFhjcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
    "https://www.google.com/search?q=Sara+Anderson+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=BCjdZeqTD5Kmvr0PloaUkAE&iflsig=ANes7DEAAAAAZd02FJkvLqwNeUTdWDyi9LhAoOlC5fP7&udm=&ved=0ahUKEwjqpeuencqEAxUSk68BHRYDBRIQ4dUDCA0&uact=5&oq=Sara+Anderson+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImpTYXJhIEFuZGVyc29uICgg4oCcQGdtYWlsLmNvbeKAnSBPUiDigJxAaG90bWFpbC5jb23igJ0gT1Ig4oCcQHlhaG9vLmNvbeKAnSkgQU5EIEJyYXppbCBzaXRlOmluc3RhZ3JhbS5jb20vSHJQAFhdcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
    "https://www.google.com/search?q=Gregory+Dean+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=ByjdZeyzIpG_vr0P0KG38AI&iflsig=ANes7DEAAAAAZd02Fz4Oma5p4ihXkqUU9uw1bhz_7u_C&udm=&ved=0ahUKEwis07WgncqEAxWRn68BHdDQDS4Q4dUDCA0&uact=5&oq=Gregory+Dean+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImlHcmVnb3J5IERlYW4gKCDigJxAZ21haWwuY29t4oCdIE9SIOKAnEBob3RtYWlsLmNvbeKAnSBPUiDigJxAeWFob28uY29t4oCdKSBBTkQgQnJhemlsIHNpdGU6aW5zdGFncmFtLmNvbS9Ic1AAWGBwAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEBmAIAoAIAmAMAkgcA&sclient=gws-wiz",
    "https://www.google.com/search?q=Richard+Johnson+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=CijdZcClNJDk1e8Pps-IuA0&iflsig=ANes7DEAAAAAZd02G7c8AunidJ4ddAcAV9WH-XGQvZq3&udm=&ved=0ahUKEwjA0v6hncqEAxUQcvUHHaYnAtcQ4dUDCA0&uact=5&oq=Richard+Johnson+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImxSaWNoYXJkIEpvaG5zb24gKCDigJxAZ21haWwuY29t4oCdIE9SIOKAnEBob3RtYWlsLmNvbeKAnSBPUiDigJxAeWFob28uY29t4oCdKSBBTkQgQnJhemlsIHNpdGU6aW5zdGFncmFtLmNvbS9IdlAAWGRwAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEBmAIAoAIAmAMAkgcA&sclient=gws-wiz",
    "https://www.google.com/search?q=Alex+Fowler+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=DijdZb-PEPao1e8PuYakmA4&iflsig=ANes7DEAAAAAZd02Hgrof61iJ8udcNDz3hQ9ojspf4hH&udm=&ved=0ahUKEwi_zs6jncqEAxV2VPUHHTkDCeMQ4dUDCA0&uact=5&oq=Alex+Fowler+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImhBbGV4IEZvd2xlciAoIOKAnEBnbWFpbC5jb23igJ0gT1Ig4oCcQGhvdG1haWwuY29t4oCdIE9SIOKAnEB5YWhvby5jb23igJ0pIEFORCBCcmF6aWwgc2l0ZTppbnN0YWdyYW0uY29tL0hvUABYXHAAeACQAQCYAQCgAQCqAQC4AQPIAQD4AQGYAgCgAgCYAwCSBwA&sclient=gws-wiz",
    "https://www.google.com/search?q=Shannon+Fleming+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=ESjdZZidKce4vr0P8qOk-A4&iflsig=ANes7DEAAAAAZd02IaOJAwxs26-hFsH2RvtLXKK-WjdD&udm=&ved=0ahUKEwjY6Z6lncqEAxVHnK8BHfIRCe8Q4dUDCA0&uact=5&oq=Shannon+Fleming+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImxTaGFubm9uIEZsZW1pbmcgKCDigJxAZ21haWwuY29t4oCdIE9SIOKAnEBob3RtYWlsLmNvbeKAnSBPUiDigJxAeWFob28uY29t4oCdKSBBTkQgQnJhemlsIHNpdGU6aW5zdGFncmFtLmNvbS9IdlAAWGJwAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEBmAIAoAIAmAMAkgcA&sclient=gws-wiz",
    "https://www.google.com/search?q=Cassandra+Carey+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=FSjdZeKpDs7f1e8P4M2biAU&iflsig=ANes7DEAAAAAZd02JX5_oDoTB6N4PVG0tCl39-N8Qwh8&udm=&ved=0ahUKEwiiiPimncqEAxXOb_UHHeDmBlEQ4dUDCA0&uact=5&oq=Cassandra+Carey+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImxDYXNzYW5kcmEgQ2FyZXkgKCDigJxAZ21haWwuY29t4oCdIE9SIOKAnEBob3RtYWlsLmNvbeKAnSBPUiDigJxAeWFob28uY29t4oCdKSBBTkQgQnJhemlsIHNpdGU6aW5zdGFncmFtLmNvbS9Ic1AAWF9wAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEBmAIAoAIAmAMAkgcA&sclient=gws-wiz",
    "https://www.google.com/search?q=Jessica+Davidson+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=aa9558a2cbdb6cbe&source=hp&ei=GCjdZazVKOrt1e8P9N2ZsAU&iflsig=ANes7DEAAAAAZd02KCakInvoxBUqlZHlrf9cPKZhkxiO&udm=&ved=0ahUKEwiswcmoncqEAxXqdvUHHfRuBlYQ4dUDCA0&uact=5&oq=Jessica+Davidson+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6Im1KZXNzaWNhIERhdmlkc29uICgg4oCcQGdtYWlsLmNvbeKAnSBPUiDigJxAaG90bWFpbC5jb23igJ0gT1Ig4oCcQHlhaG9vLmNvbeKAnSkgQU5EIEJyYXppbCBzaXRlOmluc3RhZ3JhbS5jb20vSHBQAFhecAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
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
