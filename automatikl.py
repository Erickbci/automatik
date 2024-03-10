import pyautogui
from time import sleep

pyautogui.useImageNotFoundException()

counter = 0

#       Buscar imagem icone do Discord
while True:
        if counter <= 20:
                print(counter)
                #       Localizar imagem
                try:
                        disc = pyautogui.locateCenterOnScreen('disc.png', confidence=0.7)
                        pyautogui.doubleClick(disc.x, disc.y, duration=0.5)
                        sleep(1)
                        counter = 0
                        print(counter)
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        sleep(0.5)
                        counter += 1
        else:
                #       Caso não encontrar em um periodo de tempo, finalizar
                print('numero maximo de tentativas excedido')
                counter = 0
                print(counter)
                break

#       Buscar imagem do usuario
while True:
        if counter <= 20:
                print(counter)
                #       Localizar imagem
                try:
                        user = pyautogui.locateCenterOnScreen('usertest.png',confidence=0.9)
                        pyautogui.doubleClick(user.x, user.y, duration=0.5)
                        sleep(1)
                        counter = 0
                        print(counter)
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        sleep(0.5)
                        counter += 1
        else:
                #       Caso não encontrar em um periodo de tempo, finalizar
                print('numero maximo de tentativas excedido')
                counter = 0
                print(counter)
                break       

#       Buscar imagem do input
while True:
        if counter <= 20:
                print(counter)
                #       Localizar imagem
                try:
                        ipt = pyautogui.locateCenterOnScreen('ipt.png',confidence=0.9)
                        pyautogui.doubleClick(ipt.x, ipt.y, duration=0.5)
                        sleep(1)
                        counter = 0
                        print(counter)
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        sleep(0.5)
                        counter += 1
        else:
                #       Caso não encontrar em um periodo de tempo, finalizar
                print('numero maximo de tentativas excedido')
                counter = 0
                print(counter)
                break   

#       Digitar no input
while True:
        if counter <= 20:
                print(counter)
                #       Localizar imagem
                try:
                        #       Buscar mensagem no arquivo de texto e escrever
                        with open('msg.txt', 'r') as filename:
                                for line in filename:
                                        msg = line
                                        pyautogui.write(msg)
                        sleep(1)
                        counter = 0
                        print(counter)
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        sleep(0.5)
                        counter += 1
        else:
                #       Caso não encontrar em um periodo de tempo, finalizar
                print('numero maximo de tentativas excedido')
                counter = 0
                print(counter)
                break

#       Buscar imagem do X e sair do aplicativo
while True:
        if counter <= 20:
                print(counter)
                #       Localizar imagem
                try:
                        ext = pyautogui.locateCenterOnScreen('ext.png', confidence=0.9)
                        pyautogui.doubleClick(ext.x, ext.y, duration=0.5)
                        sleep(1)
                        counter = 0
                        print(counter)
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        sleep(0.5)
                        counter += 1
        else:
                #       Caso não encontrar em um periodo de tempo, finalizar
                print('numero maximo de tentativas excedido')
                counter = 0
                print(counter)
                break   

print('Obrigado por utilizar o BOT cinigalia')
                
#.\env\Scripts\Activate.ps1
# pip install pyautogui pillow
# pip install pyinstaller
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# pyinstaller --onefile -w app.py
# pip install opencv-python