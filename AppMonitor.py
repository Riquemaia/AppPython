from turtle import left
import PySimpleGUI as sg
import os
from datetime import datetime
from pathlib import Path
import pandas as pd
import shutil 
import subprocess

id_sz = 5
tab_sz = 20
data_sz = 15
tam_sz = 8
font_sz = 'Arial 14'
font_bt = 'Arial 12'

df = pd.read_excel(r"D:\Estudos_Python\tabelas.xlsx")
table_list = df['TABELA'].tolist()
json_list = df['JSON'].tolist()
python_list = df['PYTHON'].tolist()
sql_list = df['SQL'].tolist()
filter_list = df['FILTER'].tolist()

class TelaPython:
    def __init__(self):
        sg.theme('Dark Blue 3')
        # input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(1)]

        inputs = [
                    [sg.Image(r'C:\Users\Henrique\Pictures\cielo.png')],
                    [sg.Text('Informações do Processo:',text_color='white',font=font_sz)],
                    [sg.Text('Tabela:',text_color='white',font=font_sz),sg.Combo(table_list, default_value='Selecione a tabela...', key='proc',size=(25,len(table_list)),font=font_sz)],
                    [sg.Text('Data:',text_color='white',font=font_sz),sg.Input('Selecionar data...',key='out_data',size=(data_sz,1),pad=(0,0),text_color='black',font=font_sz),sg.CalendarButton('Calendario',key='date', target='out_data',format = "%Y-%m-%d",font='Arial 10')],
                    [sg.Button('Confirmar', key='selec', font=font_bt)]
            ]

        description =  [
                [sg.Text('ID',size=(id_sz,1),pad=(0,0), text_color='black',font=font_sz),sg.Text('Tabela',size=(tab_sz,1),pad=(0,0),text_color='black',font=font_sz),sg.Text('Data',size=(data_sz,1),pad=(0,0),text_color='black',font=font_sz)],
                [sg.Text('...',key='ids',size=(id_sz,1),pad=(0,0),font=font_sz),sg.Text('...',key='tabelas',size=(tab_sz,1),pad=(0,0),font=font_sz),sg.Text('...',key='datas',size=(data_sz,1),pad=(0,0),font=font_sz)],
                [sg.Button('Executar', key='exec', font=font_bt),sg.Button('Executar tudo', key='exec_all', font=font_bt)],
                [sg.Output(size=(45,10),key='saida',font=font_bt)],
            ]

        layout = [[sg.Column(inputs, element_justification='c'), sg.VSeperator(),sg.Column(description, element_justification='c')]]
        # layout = header + input_rows1
        self.window = sg.Window('Projeto Maia', layout, font='Courier 18', resizable=True)

    def Iniciar(self):
        while True:
            self.event, self.values = self.window.read()
            if  self.event == 'selec':
                self.window['saida'].update('')
                try:
                    x = self.window['proc'].get()
                    x = table_list.index(x)
                    self.window['ids'].update(x)
                    self.window['tabelas'].update(table_list[x])
                    self.window['datas'].update(self.values['out_data'])
                    json_selec = json_list[x]
                    python_selec = python_list[x]
                    sql_selec = sql_list[x]
                    filter_selec = filter_list[x]
                    if self.values['out_data'] == 'Selecionar data...':
                        print("Você deve selecionar uma data!")
                    else:
                        data_selec = self.values['out_data']
                        self.window['saida'].update('Tabela selecionada!')
                except:
                    print('Você deve selecionar uma tabela!')
            if self.event == 'exec':
                try:
                    self.window['saida'].update('')
                    print(json_selec)
                    print(python_selec)
                    print(sql_selec)
                    print(data_selec)
                    print(filter_selec)
                    # subprocess.call(['bash','Shell_padrao.sh',json_selec,python_selec,sql_selec,filter_selec,data_selec])
                except:
                    print('Você deve confirmar as informações antes de executar!')
            if self.event == 'exec_all':
                self.window['saida'].update('')
                for x in range(len(table_list)):
                    json_selec = json_list[x]
                    python_selec = python_list[x]
                    sql_selec = sql_list[x]
                    filter_selec = filter_list[x]
                    print(json_selec)
                    print(python_selec)
                    print(sql_selec)
                    print(data_selec)
                    print(filter_selec)
                    # subprocess.call(['bash','Shell_padrao.sh',json_selec,python_selec,sql_selec,filter_selec,data_selec])
            if self.event == sg.WINDOW_CLOSED:
                break
tela = TelaPython()
tela.Iniciar()