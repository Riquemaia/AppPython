import PySimpleGUI as sg

def make_window():
    logo = [[sg.Image(r'C:\Users\Henrique\Downloads\logo-cielo-256.png')]]

    origem_col = [[sg.T('Source File:', size=(15,1)), sg.In(key='k_path',size=(45,1)), sg.FileBrowse(target='k_path')],
        [sg.Button('Confirmar Origem', key='k_conf_arq')]
    ]

    page_col = [[sg.T('Database:', size=(15,1)), sg.In(default_text='',key='k_db',size=(20,1))],
        [sg.T('Tabela:', size=(15,1)), sg.In(default_text='',key='k_tb',size=(20,1))],
        [sg.Button('Confirmar Info', key='k_conf_info')]
    ]

    button_col = [[sg.Button('Gerar Script', key='k_ger_scrt', font=14, button_color='green')]]

    layout = [[sg.Button('< Voltar', key='k_voltar_jira')],
        [sg.Push(), sg.Col(logo, element_justification='c'), sg.Push()],
        [sg.Col(origem_col, element_justification='l')],
        [sg.Col(page_col, element_justification='l')],
        [sg.Push(),sg.Col(button_col),sg.Push()]
    ]
    return sg.Window('Projeto Maia', layout, finalize=True)