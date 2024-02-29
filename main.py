from faker import Faker
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import autogui_clicker

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

fake = Faker()
termos_nomes = [fake.name() for _ in range(1000)]

i = 0
lista_sites = []

# Configurar o WebDriver
servico = Service(ChromeDriverManager().install())

# Lista de termos de pesquisa
termos_pesquisa = ["fitness", "academia"]
options = Options()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

navegador = webdriver.Chrome(service=servico, options=options)

valor_fixo = (
    "( “@outlook.com” OR “@hotmail.com” OR “@live.com”) AND site:instagram.com/"
)

try:
    for termo in termos_nomes:
        navegador.get("https://www.google.com")
        try:
            checkbox = WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located(
                    By.CLASS_NAME, "recaptcha-checkbox-border"
                )
            )
            if checkbox:
                autogui_clicker.realizar_sequencia_de_cliques()
        except:
            pass
        try:
            botao_aceitar_tudo = WebDriverWait(navegador, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[text()='Aceitar tudo']")
                )
            )

            if botao_aceitar_tudo.is_displayed():
                botao_aceitar_tudo.click()
        except:
            campo_pesquisa = WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            campo_pesquisa.send_keys(termo + " " + valor_fixo)
            campo_pesquisa.send_keys(Keys.RETURN)

            time.sleep(random.choice(range(5, 20)))

            lista_sites.append(navegador.current_url)
            i += 1
        if i % 30 == 0:
            autogui_clicker.realizar_sequencia_de_cliques()

except Exception as e:
    print(f"Erro durante a execução: {e}")

finally:
    print(lista_sites)
    texto_da_lista = "\n".join(lista_sites)
    # Escrevendo a string no bloco de texto
    with open("caminho_do_arquivo.txt", "w") as arquivo:
        arquivo.write(texto_da_lista)
    navegador.quit()
