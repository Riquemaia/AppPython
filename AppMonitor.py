import PySimpleGUI as sg
import os
from datetime import datetime
from pathlib import Path
import pandas as pd
import shutil 
import subprocess

id_sz = 10
tab_sz = 20
data_sz = 15
tam_sz = 8

df = pd.read_excel(r"D:\Estudos_Python\tabelas.xlsx")
table_list = df['TABELA'].tolist()
json_list = df['JSON'].tolist()
python_list = df['PYTHON'].tolist()
sql_list = df['SQL'].tolist()

class TelaPython:
    def __init__(self):
        sg.theme('Dark Blue 3')
        # input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(1)]
        header =  [[sg.Text('ID',size=(id_sz,1),pad=(0,0), text_color='black'),sg.Text('Tabela',size=(tab_sz,1),pad=(0,0),text_color='black'),sg.Text('Data',size=(data_sz,1),pad=(0,0),text_color='black')]]

        input_rows1 = [
                    [sg.Text('...',key='ids',size=(id_sz,1),pad=(0,0)),sg.Text('...',key='tabelas',size=(tab_sz,1),pad=(0,0)),sg.Text('...',key='datas',size=(data_sz,1),pad=(0,0))],
                    [sg.Combo(table_list, default_value='Selecione a tabela...', key='proc',size=(30,len(table_list))),sg.Button('Selecionar', key='selec', font='Arial 12')],
                    [sg.Input('Escolher data...',key='out_data',size=(data_sz,1),pad=(0,0)),sg.CalendarButton('Calendario',key='date', target='out_data',format = "%Y-%m-%d",font='Arial 12')],
                    [sg.Button('Executar', key='exec', font='Arial 12')],
                    [sg.Text('Informações do Processo:')],
                    [sg.Output(size=(45,6),key='saida')],
                    [sg.Text('Create by Henrique Maia', font='Arial 8', text_color='black')]
            ]

        layout = header + input_rows1
        self.window = sg.Window('Projeto Maia', layout, font='Courier 18')

    def Iniciar(self):
        while True:
            self.event, self.values = self.window.read()
            if  self.event == 'selec':
                try:
                    x = self.window['proc'].get()
                    x = table_list.index(x)
                    self.window['saida'].update('Tabela selecionada!')
                    self.window['ids'].update(x)
                    self.window['tabelas'].update(table_list[x])
                    self.window['datas'].update(self.values['out_data'])
                except:
                    print('Você deve selecionar uma tabela!')
            json_selec = json_list[x]
            python_selec = python_list[x]
            sql_selec = sql_list[x]
            if self.event == 'exec':
                print(json_selec)
                print(python_selec)
                print(sql_selec)
                subprocess.call(['bash','Shell.sh',json_selec,python_selec,sql_selec])
            
            if self.event == sg.WINDOW_CLOSED:
                break
tela = TelaPython()
tela.Iniciar()