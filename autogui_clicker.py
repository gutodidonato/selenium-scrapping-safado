import pyautogui
import time


def realizar_sequencia_de_cliques():
    time.sleep(5)
    pyautogui.click(1674, 1055)
    time.sleep(1)
    pyautogui.rightClick(1713, 1015)
    time.sleep(1)
    pyautogui.click(1695, 965)
    time.sleep(1)
    pyautogui.click(1367, 1062)
    time.sleep(15)
    pyautogui.click(1674, 1055)
    time.sleep(3)
    pyautogui.rightClick(1713, 1015)
    time.sleep(1)
    pyautogui.click(1694, 965)
    time.sleep(10)
    pyautogui.click(1367, 1062)
    time.sleep(5)


def clicar_cookies():
    pyautogui.click(570, 852)


realizar_sequencia_de_cliques()
