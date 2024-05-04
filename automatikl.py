from tkinter import *
from tkinter import ttk

win= Tk()

win.geometry("700x350")
#tamanho fixo
win.resizable(0, 0)
def show_msg():
   print('foda mlk')

Label(win, text= "Welcome Folks!", font= ('Aerial 17 bold italic')).pack(pady= 30)

#botao pra executar a funcao
ttk.Button(win, text= "Click Here", command=show_msg, )
win.mainloop()