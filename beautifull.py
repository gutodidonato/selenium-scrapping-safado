import re
import random
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

        # requisição para o site com headers
        response = requests.get(url, headers=headers)
        print(f"Status code for {url}: {response.status_code}")
        if response and response.status_code == 200:

            # Use BeautifulSoup para analisar o HTML
            soup = BeautifulSoup(response.text, "html.parser")
            all_texts = soup.find_all(text=True)
            all_text_as_string = " ".join(all_texts)

            # REGEX
            email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

            # Encontrar emails usando a expressão regular
            emails_encontrados = re.findall(email_pattern, all_text_as_string)

            time.sleep(random.choice(range(15, 40)))

            return emails_encontrados if emails_encontrados else []
        else:
            print(f"Erro na requisição")
            return []

    except Exception as e:
        print(f"Erro ao processar {url}: {e}")
        return []


# Lista de sites
lista_sites = [
    "https://www.google.com/search?q=Daniel+Hill+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=RObdZeT0J4Ku5OUPkNeMgAI&iflsig=ANes7DEAAAAAZd30VGb6DHjQdBu6BwJMO3dz9V-_5mhn&udm=&ved=0ahUKEwjkpvTW0suEAxUCF7kGHZArAyAQ4dUDCA0&uact=5&oq=Daniel+Hill+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImhEYW5pZWwgSGlsbCAoIOKAnEBnbWFpbC5jb23igJ0gT1Ig4oCcQGhvdG1haWwuY29t4oCdIE9SIOKAnEB5YWhvby5jb23igJ0pIEFORCBCcmF6aWwgc2l0ZTppbnN0YWdyYW0uY29tL0h3UABYYnAAeACQAQCYAQCgAQCqAQC4AQPIAQD4AQGYAgCgAgCYAwCSBwA&sclient=gws-wiz",
    "https://www.google.com/search?q=Melanie+Mann+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=R-bdZcPBKNTc5OUPsaWu6As&iflsig=ANes7DEAAAAAZd30Vxs9Q_dZH_IG41vbDXu0vlYQMLp8&udm=&ved=0ahUKEwiDgazY0suEAxVULrkGHbGSC70Q4dUDCA0&uact=5&oq=Melanie+Mann+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImlNZWxhbmllIE1hbm4gKCDigJxAZ21haWwuY29t4oCdIE9SIOKAnEBob3RtYWlsLmNvbeKAnSBPUiDigJxAeWFob28uY29t4oCdKSBBTkQgQnJhemlsIHNpdGU6aW5zdGFncmFtLmNvbS9IiwFQAFhjcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
    "https://www.google.com/search?q=Anthony+Gonzalez+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=SubdZeOhHbGz5OUPiIGhuAM&iflsig=ANes7DEAAAAAZd30Wmo5eGnjW-aNtbdv8Pimhc4kB7e9&udm=&ved=0ahUKEwjj7tfZ0suEAxWxGbkGHYhACDcQ4dUDCA0&uact=5&oq=Anthony+Gonzalez+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6Im1BbnRob255IEdvbnphbGV6ICgg4oCcQGdtYWlsLmNvbeKAnSBPUiDigJxAaG90bWFpbC5jb23igJ0gT1Ig4oCcQHlhaG9vLmNvbeKAnSkgQU5EIEJyYXppbCBzaXRlOmluc3RhZ3JhbS5jb20vSHpQAFhlcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
    "https://www.google.com/search?q=Sharon+Wilson+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=TebdZduoCPrQ5OUPoqWKMA&iflsig=ANes7DEAAAAAZd30XXuX0-oABzio_WaC1nae4gEbXWz4&udm=&ved=0ahUKEwibg_ra0suEAxV6KLkGHaKSAgYQ4dUDCA0&uact=5&oq=Sharon+Wilson+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImpTaGFyb24gV2lsc29uICgg4oCcQGdtYWlsLmNvbeKAnSBPUiDigJxAaG90bWFpbC5jb23igJ0gT1Ig4oCcQHlhaG9vLmNvbeKAnSkgQU5EIEJyYXppbCBzaXRlOmluc3RhZ3JhbS5jb20vSHhQAFhgcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
    "https://www.google.com/search?q=Sean+Castro+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=T-bdZc_2Lc2A5OUP6IydoAQ&iflsig=ANes7DEAAAAAZd30X_Qx0_TYxRVktN1Bu89zKuGG56HP&udm=&ved=0ahUKEwiP2pnc0suEAxVNALkGHWhGB0QQ4dUDCA0&uact=5&oq=Sean+Castro+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImhTZWFuIENhc3RybyAoIOKAnEBnbWFpbC5jb23igJ0gT1Ig4oCcQGhvdG1haWwuY29t4oCdIE9SIOKAnEB5YWhvby5jb23igJ0pIEFORCBCcmF6aWwgc2l0ZTppbnN0YWdyYW0uY29tL0h0UABYXnAAeACQAQCYAQCgAQCqAQC4AQPIAQD4AQGYAgCgAgCYAwCSBwA&sclient=gws-wiz",
    "https://www.google.com/search?q=Louis+Duncan+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=UubdZfHAF6O55OUP-L2tuAU&iflsig=ANes7DEAAAAAZd30YtmBBt5Oepy4QkKGlsztUs5P192y&udm=&ved=0ahUKEwjxsbrd0suEAxWjHLkGHfheC1cQ4dUDCA0&uact=5&oq=Louis+Duncan+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImlMb3VpcyBEdW5jYW4gKCDigJxAZ21haWwuY29t4oCdIE9SIOKAnEBob3RtYWlsLmNvbeKAnSBPUiDigJxAeWFob28uY29t4oCdKSBBTkQgQnJhemlsIHNpdGU6aW5zdGFncmFtLmNvbS9IdlAAWGBwAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEBmAIAoAIAmAMAkgcA&sclient=gws-wiz",
    "https://www.google.com/search?q=Stephanie+Rasmussen+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=VebdZd7PAeiN5OUPooSH-As&iflsig=ANes7DEAAAAAZd30ZcSpU2fmofxQlHm8rwUGw4h7Gshe&udm=&ved=0ahUKEwieztve0suEAxXoBrkGHSLCAb8Q4dUDCA0&uact=5&oq=Stephanie+Rasmussen+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6InBTdGVwaGFuaWUgUmFzbXVzc2VuICgg4oCcQGdtYWlsLmNvbeKAnSBPUiDigJxAaG90bWFpbC5jb23igJ0gT1Ig4oCcQHlhaG9vLmNvbeKAnSkgQU5EIEJyYXppbCBzaXRlOmluc3RhZ3JhbS5jb20vSHxQAFhlcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
    "https://www.google.com/search?q=Monica+Wright+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=V-bdZd3GKPLX5OUPlqOegAs&iflsig=ANes7DEAAAAAZd30Z1q-RIZ_ytipNTCqawuJqMwVYgD-&udm=&ved=0ahUKEwidzvzf0suEAxXyK7kGHZaRB7AQ4dUDCA0&uact=5&oq=Monica+Wright+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6ImpNb25pY2EgV3JpZ2h0ICgg4oCcQGdtYWlsLmNvbeKAnSBPUiDigJxAaG90bWFpbC5jb23igJ0gT1Ig4oCcQHlhaG9vLmNvbeKAnSkgQU5EIEJyYXppbCBzaXRlOmluc3RhZ3JhbS5jb20vSHhQAFhhcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAA&sclient=gws-wiz",
    "https://www.google.com/search?q=Mrs.+Rachel+Rogers+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=WubdZa3aEdXA5OUPvdKs0AU&iflsig=ANes7DEAAAAAZd30auFxE-2La8Bb9ZkYy5yP3Izi5t-l&udm=&ved=0ahUKEwit75zh0suEAxVVILkGHT0pC1oQ4dUDCA0&uact=5&oq=Mrs.+Rachel+Rogers+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6Im9NcnMuIFJhY2hlbCBSb2dlcnMgKCDigJxAZ21haWwuY29t4oCdIE9SIOKAnEBob3RtYWlsLmNvbeKAnSBPUiDigJxAeWFob28uY29t4oCdKSBBTkQgQnJhemlsIHNpdGU6aW5zdGFncmFtLmNvbS9IflAAWGhwAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEBmAIAoAIAmAMAkgcA&sclient=gws-wiz",
    "https://www.google.com/search?q=Jennifer+Mitchell+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&sca_esv=85af15397c77c0f6&source=hp&ei=XebdZbN_1Nzk5Q-xpa7oCw&iflsig=ANes7DEAAAAAZd30bfrqkta5wDtpzcudpJ11QJhP74PW&udm=&ved=0ahUKEwjzocPi0suEAxVULrkGHbGSC70Q4dUDCA0&uact=5&oq=Jennifer+Mitchell+%28+%E2%80%9C%40gmail.com%E2%80%9D+OR+%E2%80%9C%40hotmail.com%E2%80%9D+OR+%E2%80%9C%40yahoo.com%E2%80%9D%29+AND+Brazil+site%3Ainstagram.com%2F&gs_lp=Egdnd3Mtd2l6Im5KZW5uaWZlciBNaXRjaGVsbCAoIOKAnEBnbWFpbC5jb23igJ0gT1Ig4oCcQGhvdG1haWwuY29t4oCdIE9SIOKAnEB5YWhvby5jb23igJ0pIEFORCBCcmF6aWwgc2l0ZTppbnN0YWdyYW0uY29tL0iAAVAAWGdwAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEBmAIAoAIAmAMAkgcA&sclient=gws-wiz",
]

todos_emails = []

# Iterar sobre a lista de sites e extrair emails
for site in lista_sites:

    # chamando a funcao
    emails_site = extrair_emails(site)
    todos_emails.extend(emails_site)


emails_unicos = set(todos_emails)
emails_certos = list(emails_unicos)

# Criar um DataFrame do pandas com a lista de emails
df_emails = pd.DataFrame({"Emails": emails_certos})

# Exportar o DataFrame para um arquivo XLSX
df_emails.to_excel("emails_extraidos.xlsx", index=False)

print("Exportação concluída. Verifique o arquivo 'emails_extraidos.xlsx'.")
