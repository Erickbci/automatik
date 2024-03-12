import pyautogui
from time import sleep
from PySimpleGUI import PySimpleGUI as sg

#       Layout
sg.theme('Reddit')
layout = [
        [sg.Text('Usuário'), sg.Input(key='usuario')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
        [sg.Button('Entrar')]
]

#       Janela
janela = sg.Window('Tela login', layout)

#       Eventos
while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
                break
        if eventos == 'Entrar':
                messages = []
                counter = 0

                #       Interação com usuário
                numberOfLaboratory = int(valores['usuario'])

                quantityOfPieces = int(valores['senha'])
                # print(valores['usuario'])
                # print(valores['senha'])
                # print('entrou')
                break

pyautogui.useImageNotFoundException()



#       Variáveis ambiente
# messages = []
# counter = 0

# #       Interação com usuário
# numberOfLaboratory = int(input("Digite o número do laboratório que deseja realizar a transferencia \n"))

# quantityOfPieces = int(input('Quantidade de peças \n'))

#       Salvar os números conforme a quantidade informada pelo usuário
while True:  
        
        arrayMessagesLength = len(messages)
        if quantityOfPieces - 1>= arrayMessagesLength:
                messages.append(input("Por favor insira o PPID: \n"))
                counter += 1
        else:
                counter = 0
                print('Número de peças informado foi atingido')
                break

#       Buscar imagem icone do Discord
while True:
        if counter <= 20:
                #       Localizar imagem
                try:
                        disc = pyautogui.locateCenterOnScreen('disc.png', confidence=0.7)
                        pyautogui.doubleClick(disc.x, disc.y, duration=0.5)
                        sleep(1)
                        counter = 0
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        print('Procurando imagem...')
                        sleep(0.5)
                        counter += 1
        else:
        #       Caso não encontrar em um periodo de tempo, finalizar
                print("A imgagem DISCORD não foi encontrada a tempo, tente outra vez")
                counter = 0
                break
        

#       Buscar imagem do usuario
while True:
        if counter <= 20:
                #       Localizar imagem
                try:
                        user = pyautogui.locateCenterOnScreen('usertest.png',confidence=0.9)
                        pyautogui.doubleClick(user.x, user.y, duration=0.5)
                        sleep(1)
                        counter = 0
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        print('Procurando imagem...')
                        sleep(0.5)
                        counter += 1
        else:
                #       Caso não encontrar em um periodo de tempo, finalizar
                print("A imgagem USUARIO não foi encontrada a tempo, tente outra vez")
                counter = 0
                break       

#       Buscar imagem do input
while True:
        if counter <= 20:           
                #       Localizar imagem
                try:
                        ipt = pyautogui.locateCenterOnScreen('ipt.png',confidence=0.9)
                        pyautogui.doubleClick(ipt.x, ipt.y, duration=0.5)
                        sleep(1)
                        counter = 0
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        print('Procurando imagem...')
                        sleep(0.5)
                        counter += 1
        else:
                #       Caso não encontrar em um periodo de tempo, finalizar
                print("A imgagem INPUT não foi encontrada a tempo, tente outra vez")
                counter = 0
                break   

#       Digitar no input
while True:
        if counter <= 20:
                #       Localizar imagem
                try:
                        #       Buscar mensagem no arquivo de texto e escrever
                        with open('msg.txt', 'w') as filename:
                                for line in messages:
                                        filename.write(str(line) + '\n')
                                        pyautogui.write(line)
                                        pyautogui.hotkey('enter')
                        sleep(1)
                        counter = 0
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        print('Procurando imagem...')
                        sleep(0.5)
                        counter += 1
        else:
                #       Caso não encontrar em um periodo de tempo, finalizar
                print("O arquivo/texto não foi encontrado a tempo, tente outra vez")
                counter = 0
                break

#       Buscar imagem do X e sair do aplicativo
while True:
        if counter <= 20:
                
                #       Localizar imagem
                try:
                        ext = pyautogui.locateCenterOnScreen('ext.png', confidence=0.9)
                        pyautogui.doubleClick(ext.x, ext.y, duration=0.5)
                        sleep(1)
                        counter = 0
                        break
                #       Repetir o passso enquanto não encontrar
                except pyautogui.ImageNotFoundException:
                        print('Procurando imagem...')
                        sleep(0.5)
                        counter += 1
        else:
                #       Caso não encontrar em um periodo de tempo, finalizar
                print("A imgagem X não foi encontrada a tempo, tente outra vez")
                counter = 0
                break   

print('Obrigado por utilizar o BOT cinigalia')
#.\env\Scripts\Activate.ps1
# pip install pyautogui pillow
# pip install pyinstaller
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# pyinstaller --onefile -w app.py
# pip install PySimpleGUI