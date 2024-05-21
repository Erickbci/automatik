from tkinter import *
from tkinter import ttk
import datetime
import pandas as pd

data_atual = datetime.datetime.now()

ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day

data_atual = datetime.date(ano_atual, mes_atual, dia_atual) 
numero_semana = data_atual.isocalendar()[1]

etiquetaCompleta = f'52SpartnumberBRPD{ano_atual}{numero_semana}C'

dataFrameBase = pd.read_excel('base.xlsx')

df = pd.read_excel('teste.xlsx')

df = df.iloc[0:0]

def contador(inicio, fim):
    for i in range(inicio, fim + 1):
        yield f"{i:03d}" if i < 100 else str(i)

#ultima_linha_com_valor = dataFrameBase.iloc[-1]
#valor = ultima_linha_com_valor['partnumber2']
coluna = 'partnumber2'
ultimo_indice_com_valor = dataFrameBase[coluna].last_valid_index()

ultimo_valor = dataFrameBase.at[ultimo_indice_com_valor, coluna]
lastValue = ultimo_valor[-3:]

quantidadeDoUsuario = 7 # trocar pelo valor retornado do usuario

def format_string(num_str):
   num = int(num_str)
   if num < 100:
      if num % 10 == 0:
         return num_str.lstrip('0')
      else: 
         return num_str.lstrip('00')
   else:
         return num_str

newLastValue = format_string(lastValue)
strToInt = int(newLastValue)
inicioParametro = strToInt + 1

fimParametro = inicioParametro + quantidadeDoUsuario
 
for sequenciaAtual in contador(inicioParametro, fimParametro):
    t5s = etiquetaCompleta + sequenciaAtual
    df.loc[len(df), 'etiqueta'] = t5s
    print(t5s)
    # adicionar t5s (tag 52S) na planilha 'base'

df.to_excel("teste.xlsx", index=False)

dataFrameBase.to_excel('base.xlsx', index=False)