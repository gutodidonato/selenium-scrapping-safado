import pyautogui
import time

# Aguarde alguns segundos antes de começar
time.sleep(5)

while True:
    # Verifica se o botão esquerdo do mouse está pressionado
    if pyautogui.mouseInfo().get("left") == "down":
        # Obtém as coordenadas atuais do mouse
        current_mouse_position = pyautogui.position()

        # Salva as coordenadas na lista
        print(
            f"Posição atual do mouse: X = {current_mouse_position[0]}, Y = {current_mouse_position[1]}"
        )

    # Adiciona um pequeno atraso entre as verificações
    time.sleep(1)
