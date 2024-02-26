from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar o WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Lista de termos de pesquisa
termos_pesquisa = ["fitness", "academia"]

valor_fixo = (
    "( “@gmail.com” OR “@hotmail.com” OR “@yahoo.com”) AND Brazil site:instagram.com/"
)
try:
    for termo in termos_pesquisa:
        # Navegar até a página inicial do Google
        navegador.get("https://www.google.com")

        # Encontrar o campo de pesquisa e enviar o termo
        campo_pesquisa = navegador.find_element(By.NAME, "q")
        campo_pesquisa.send_keys(termo)
        campo_pesquisa.send_keys(Keys.RETURN)

        # Aguardar um curto período para simular um comportamento mais humano
        time.sleep(2)

        # Imprimir a URL da página de pesquisa
        print(navegador.current_url)

        print()  # Adicionar uma linha em branco entre os termos

except Exception as e:
    print(f"Erro durante a execução: {e}")

finally:
    print("Pesquisas concluídas.")
    # Fechar o navegador
    navegador.quit()
