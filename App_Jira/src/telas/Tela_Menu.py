import PySimpleGUI as sg

def make_window():
    layout = [[sg.Col([[sg.Image(r'C:\Users\Henrique\Downloads\logo-cielo-256.png')]])],
                [sg.Col([[sg.Text("Escolha sua funcionalidade", font=20)]], element_justification='c')],
                [sg.Col([[sg.Button("Doc. Confluence", key="k_botao_arq", font=14), sg.Button("Doc. KT", key="k_botao_db", font=14)]], element_justification='c')]
                ]
    return sg.Window('Projeto Maia', layout, element_justification='c', finalize=True)