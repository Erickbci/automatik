import pyautogui
from time import sleep

pyautogui.click(991, 541,duration=0.4)
pyautogui.write('erick')

pyautogui.click(988, 563,duration=0.4)
pyautogui.write('erick')

pyautogui.click(869, 595,duration=0.4)

with open('produtos.txt', 'r') as filename:
        for line in filename:
                produto = line.split(',')[0]
                quantidade = line.split(',')[1]
                preco = line.split(',')[2]

                pyautogui.click(709, 530,duration=0.4)
                pyautogui.write(produto)
                
                pyautogui.click(707, 555,duration=0.4)
                pyautogui.write(quantidade)

                pyautogui.click(713, 580,duration=0.4)
                pyautogui.write(preco)
                
                pyautogui.click(593, 733,duration=0.4)
                sleep(1)
# automacao em py
                
#.\env\Scripts\Activate.ps1
# pip install pyautogui pillow
# pip install pyinstaller
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# pyinstaller --onefile -w app.py