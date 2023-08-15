import PySimpleGUI as sg
import pandas as pd
from atlassian import Confluence

auth_token = "ATATT3xFfGF0INvqH51-oP835sHbbQRZfXwenQJ5uJk5_HwzYp6yz--yRiTw5Ked1Jq86tcoaGnvEw7o5pVnvpFiSNU2C2r1Zgo5_i9_8oBOP8AL4vH5G-TTKZCXjs4P1XBqKBXj8lhrggFBzARfAf3ZbKEFcskrnDTgzprig5lb9ZHNgach7w4=D9039919"

confluence = Confluence(
    url='https://henriquemaia.atlassian.net/',
    username="henriquedacostamaia@gmail.com",
    password=auth_token,
    verify_ssl = True,
    cloud=True)

logo = [[sg.Image(r'C:\Users\Henrique\Downloads\logo-cielo-256.png')]]

origem_col = [[sg.T('Source File:', size=(15,1)), sg.In(key='k_path',size=(45,1)), sg.FileBrowse(target='k_path')],
    [sg.Button('Confirmar Origem', key='k_conf_arq')]
]

page_col = [[sg.T('Database:', size=(15,1)), sg.In(default_text='',key='k_db',size=(20,1))],
    [sg.T('Tabela:', size=(15,1)), sg.In(default_text='',key='k_tb',size=(20,1))],
    [sg.Button('Confirmar Info', key='k_conf_info')]
]

button_col = [[sg.Button('Gerar Script', key='k_ger_scrt', font=14, button_color='green')]]

layout = [[sg.Push(), sg.Col(logo, element_justification='c'), sg.Push()],
    [sg.Col(origem_col, element_justification='l')],
    [sg.Col(page_col, element_justification='l')],
    [sg.Push(),sg.Col(button_col),sg.Push()]
]

sg.Window('Projeto Maia', layout, finalize=True)
resp_db = False

while True:
    window, event, values = sg.read_all_windows()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'k_conf_arq':
        try:
            val_path = values['k_path']
            df = pd.read_excel(val_path, engine="openpyxl")
            database = df['Database'][1]
            tabela = df['Tabela'][1]
            window['k_db'].update(database)
            window['k_tb'].update(tabela)
        except:
            sg.popup_error('Dicionario de Dados invalido!', title='Error')
    elif event == 'k_conf_info':
        try:
            database_final = values['k_db']
            tabela_final = values['k_tb']
            resp_db = confluence.page_exists("SD", database_final, type=None)
            if resp_db == False or database_final == '':
                sg.popup_error('Database não encontrado no Jira ou em branco!\nDeve solicitar a criação antes.', title='Error')
            else:
                sg.popup_ok('Database encontrado!\nPode seguir com a criação da pagina.')
                db_id = confluence.get_page_id("SD", database_final)
        except:
            sg.popup_error('Você deve selecionar um arquivo primeiro!', title='Error')
    elif event == 'k_ger_scrt':
        if resp_db == True:
            body = '<p>This page was created with Python!</p>'
            try:
                df = df[['Campos','Descricao']]
                confluence.create_page("SD", tabela_final, body, parent_id=db_id, type='page', representation='storage', editor='v2', full_width=False)
                sg.popup_ok('Pagina criada com sucesso!')
            except:
                sg.popup_error('Ocorreu um erro ao criar a pagina!', title='Error')
        else:
            sg.popup_error('Não autorizado!\nPreencha corretamente os campos anteriores.', title='Error')


# # teste html
# colunas_html = []
# for i in range(len(df)):
#     col_html = f"""<tr><td class="confluenceTd">{df.loc[i,'Campos']}<p /></td><td class="confluenceTd">{df.loc[i,'Descricao']}<p /></td></tr>"""
#     colunas_html.append(col_html)
# colunas_html = ''.join(colunas_html)
# colunas_html
