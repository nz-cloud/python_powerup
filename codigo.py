# clicar - pyautogui.click
# escrever - pyautogui.write
# apertar uma tecla - pyautogui.press
# atalho - pyautogui.hotkey("ctrl", "C")
# scroll (rolar) - pyautogui.scroll

#Passo a passo do meu projeto

import pyautogui
import time

pyautogui.PAUSE = 0.5

#Passo 1 - Entrar no sistema da empresa:

   # # https://dlp.hashtagtreinamentos.com/python/intensivao/login

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

#Passo 2 - Fazer login no sistema da empresa:

# clicar no campo de e-mail
pyautogui.click(x=302, y=410)
# escrever e-mail
pyautogui.write("nicolasmlima@icloud.com")
# clicar no campo de senha
pyautogui.press("tab")
# escrever senha
pyautogui.write("nzvulgonizao")
# clicar em logar
pyautogui.click(x=516, y=569)
time.sleep(2)

#Passo 3 - Importar a base de dados:
import pandas
tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    #Passo 4 - Cadastrar um produto:
    # clicar em codigo do produto
    pyautogui.click(x=252, y=290)
    # escrever o codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #"1"
    pyautogui.press("tab")
    # preço unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar o produto
    pyautogui.press("enter")

    pyautogui.scroll(2500)    
#Passo 5 - Repetir isso até acabar a base de dados:


