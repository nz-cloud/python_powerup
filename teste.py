import pyautogui
import time
# apertar a tecla do windows 
pyautogui.press("win")
# digitar o nome do programa - chrome
pyautogui.write("google chrome")
# apertar enter 
pyautogui.press("enter")

time.sleep(2)
# digitar o link - https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar enter 
pyautogui.press("enter")
#esperar 5 seg após esse comando (enter)
time.sleep(2)