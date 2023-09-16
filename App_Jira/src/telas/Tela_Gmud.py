import PySimpleGUI as sg

def make_window():
    logo = [[sg.Image(r'C:\Users\Henrique\Downloads\logo-cielo-256.png')]]

    origem_col = [[sg.T('Source File:', size=(15,1)), sg.In(key='k_path_gmud',size=(45,1)), sg.FileBrowse(target='k_path_gmud')],
                  [sg.Button('Confirmar Origem', key='k_conf_arq_gmud')]]
    
    ft_col = [[sg.T('Parametros do Job File Transfer')],
              [sg.Col([[sg.T('Colunas:')],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col1', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col2', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col3', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col4', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col5', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col6', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col7', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col8', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col9', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col10', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col11', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col12', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col13', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col14', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col15', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col16', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col17', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col18', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col19', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col20', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col21', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col22', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col23', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col24', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col25', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col26', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col27', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col28', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col29', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_ft_col30', size=(30,1))]
                       ], scrollable=True, key='k_col_ft', size=(600,300))]]
    
    conn_col = [[sg.T('Parametros do Job Connect')],
              [sg.Col([[sg.T('Colunas:')],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col1', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col2', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col3', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col4', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col5', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col6', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col7', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col8', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col9', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col10', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col11', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col12', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col13', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col14', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col15', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col16', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col17', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col18', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col19', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col20', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col21', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col22', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col23', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col24', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col25', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col26', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col27', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col28', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col29', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col30', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col31', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_conn_col32', size=(30,1))]
                       ], scrollable=True, key='k_col_ft', size=(600,300))]]
    
    aws_sf_col = [[sg.T('Parametros do Job AWS Step Function')],
              [sg.Col([[sg.T('Colunas:')],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col1', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col2', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col3', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col4', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col5', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col6', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col7', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col8', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col9', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col10', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col11', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col12', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col13', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col14', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col15', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col16', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col17', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col18', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col19', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col20', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col21', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col22', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col23', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col24', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col25', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col26', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col27', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col28', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col29', size=(30,1))],
                       [sg.T(''), sg.In(default_text='', key='k_gmud_aws_sf_col30', size=(30,1))]
                       ], scrollable=True, key='k_col_ft', size=(600,300))]]
    
    tabs_col = [[sg.TabGroup([[sg.Tab('File Transfer', ft_col), sg.Tab('Connect', conn_col), sg.Tab('AWS Step Func.', aws_sf_col)]])], [sg.Button('Confirmar Jobs', key='k_conf_jobs')]]

    button_col = [[sg.Button('Gerar GMUD', key='k_ger_scrt_gmud', font=14, button_color='green')]]

    layout = [[sg.Button('< Voltar', key='k_voltar_jira')],
                [sg.Push(), sg.Col(logo, element_justification='c'), sg.Push()],
                [sg.Col(origem_col, element_justification='l')], 
                [sg.Col(tabs_col, element_justification='l')],
                [sg.Push(),sg.Col(button_col),sg.Push()]
                ]
    return sg.Window('Projeto Maia', layout, finalize=True)