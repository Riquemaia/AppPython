import PySimpleGUI as sg
import pandas as pd

logo = [[sg.Image(r'C:\Users\Henrique\Downloads\logo-cielo-256.png')]]

origem_col = [[sg.T('Source File:', size=(15,1)), sg.In(key='k_path',size=(45,1)), sg.FileBrowse(file_types=(("CSV Files", "*.csv"),),target='k_path')],
            [sg.T('Encoding:', size=(15,1)), sg.In(default_text='UTF-8',key='k_encd',size=(12,1))],
            [sg.T('Delimitador:', size=(15,1)), sg.In(default_text=';',key='k_sep',size=(3,1))],
            [sg.T('Header:', size=(15,1)), sg.Checkbox('', default=True, key='k_header')],
            [sg.Button('Confirmar Origem', key='k_conf_arq')]
                ]

table_col = [[sg.Text('Clique para renomear colunas'), sg.B('+', key='k_rename_col')],
             [sg.Col([[sg.T('Colunas:')]], scrollable=True, key='k_col', size=(540,200))]
                ]

table_col2 = [[sg.Text('Defina o tipo das colunas')],
             [sg.Col([[sg.T('Colunas/Tipos:'), sg.VSeperator(),sg.T('Formato Timestamp no Arquivo (ex: yyyy-MM-dd HH:mm:ss)')]], scrollable=True, key='k_col_type', size=(540,200))]
                ]

table_col3 = [[sg.Text('Inclua novos campos'), sg.B('+', key='k_add_col_novo')],
             [sg.Col([[sg.T('Novo campo:')]], scrollable=True, key='k_col_novo', size=(540,200))]
                ]

table_col4 = [[sg.Text('Reordene os campos'), sg.B('Iniciar', key='k_order_bt'), sg.B('Confirmar Ordenação', key='k_conf_order_bt', visible=False)],
             [sg.Col([[sg.T('Colunas:')]], scrollable=True, key='k_order_col', size=(540,200))]
                ]

tabs_col = [[sg.TabGroup([[sg.Tab('Data Types', table_col2, tooltip='Defina os tipos/colunas'), sg.Tab('Rename Columns', table_col, tooltip='Renomeie as colunas'), sg.Tab('Add Fields', table_col3, tooltip='Inclua novos campos'), sg.Tab('Sort Fields', table_col4, tooltip='Reordenar os campos')]])], [sg.Button('Confirmar Alterações', key='k_conf_alt')]]

dest_col = [[sg.T('File Destination:', size=(15,1)), sg.In(default_text="Destino do parquet no bucket" ,key='k_path_dest',size=(45,1))],
            [sg.T('Name Application:', size=(15,1)), sg.In(key='k_name_app')],
            [sg.T('Write Mode:', size=(15,1)), sg.Combo(values=['overwrite','append'], default_value='Selecione o modo de carga...', size=(15,2), readonly=True, key=f'k_write_mode')],
            [sg.T('Partitioned table:', size=(15,1)), sg.Checkbox('', default=False, key='k_partition', enable_events= True), sg.In(default_text="Digite o campo" ,key='k_name_partit', visible=False)],
            [sg.Button('Confirmar Destino', key='k_conf_dest')]
                ]

button_col = [[sg.Button('Gerar Script', key='k_ger_scrt', font=14, button_color='green')]]

def make_window2():
    layout = [[sg.Push(), sg.Col(logo, element_justification='c'), sg.Push()],
                [sg.Col(origem_col, element_justification='l')], 
                [sg.Col(tabs_col, element_justification='l')],
                [sg.Col(dest_col, element_justification='l')], 
                [sg.Push(),sg.Col(button_col),sg.Push()]
                ]
    return sg.Window('Window 2', layout, finalize=True)

##################################################################

def make_window1():
    layout = [[sg.Col([[sg.Image(r'C:\Users\Henrique\Downloads\logo-cielo-256.png')]])],
                [sg.Col([[sg.Text("Escolha a origem dos dados", font=16)]], element_justification='c')],
                [sg.Col([[sg.Button("Arquivo", key="k_botao_arq", font=14), sg.Button("Database", key="k_botao_db", font=14)]], element_justification='c')]
                ]
    return sg.Window('Window 1', layout, element_justification='c', finalize=True)

##################################################################

logo_sql = [[sg.Image(r'C:\Users\Henrique\Downloads\logo-cielo-256.png')]]

origem_col_sql = [[sg.Multiline('Digite seu script sql...', size=(80,10), horizontal_scroll=True, autoscroll=True)],
                [sg.Button('Confirmar Origem', key='k_conf_arq')]
                ]

table_col_sql = [[sg.Text('Clique para renomear colunas'), sg.B('+', key='k_rename_col')],
             [sg.Col([[sg.T('Colunas:')]], scrollable=True, key='k_col', size=(540,200))]
                ]

table_col2_sql = [[sg.Text('Defina o tipo das colunas')],
             [sg.Col([[sg.T('Colunas/Tipos:'), sg.VSeperator(),sg.T('Formato Timestamp no Arquivo (ex: yyyy-MM-dd HH:mm:ss)')]], scrollable=True, key='k_col_type', size=(540,200))]
                ]

table_col3_sql = [[sg.Text('Inclua novos campos'), sg.B('+', key='k_add_col_novo')],
             [sg.Col([[sg.T('Novo campo:')]], scrollable=True, key='k_col_novo', size=(540,200))]
                ]

table_col4_sql = [[sg.Text('Reordene os campos'), sg.B('Iniciar', key='k_order_bt'), sg.B('Confirmar Ordenação', key='k_conf_order_bt', visible=False)],
             [sg.Col([[sg.T('Colunas:')]], scrollable=True, key='k_order_col', size=(540,200))]
                ]

tabs_col_sql = [[sg.TabGroup([[sg.Tab('Data Types', table_col2_sql, tooltip='Defina os tipos/colunas'), sg.Tab('Rename Columns', table_col_sql, tooltip='Renomeie as colunas'), sg.Tab('Add Fields', table_col3_sql, tooltip='Inclua novos campos'), sg.Tab('Sort Fields', table_col4_sql, tooltip='Reordenar os campos')]])], [sg.Button('Confirmar Alterações', key='k_conf_alt')]]

dest_col_sql = [[sg.T('File Destination:', size=(15,1)), sg.In(default_text="Destino do parquet no bucket" ,key='k_path_dest',size=(45,1))],
            [sg.T('Name Application:', size=(15,1)), sg.In(key='k_name_app')],
            [sg.T('Write Mode:', size=(15,1)), sg.Combo(values=['overwrite','append'], default_value='Selecione o modo de carga...', size=(15,2), readonly=True, key=f'k_write_mode')],
            [sg.T('Partitioned table:', size=(15,1)), sg.Checkbox('', default=False, key='k_partition', enable_events= True), sg.In(default_text="Digite o campo" ,key='k_name_partit', visible=False)],
            [sg.Button('Confirmar Destino', key='k_conf_dest')]
                ]

button_col_sql = [[sg.Button('Gerar Script', key='k_ger_scrt', font=14, button_color='green')]]

def make_window3():
    layout = [[sg.Push(), sg.Col(logo_sql, element_justification='c'), sg.Push()],
                [sg.Col(origem_col_sql, element_justification='l')], 
                [sg.Col(tabs_col_sql, element_justification='l')],
                [sg.Col(dest_col_sql, element_justification='l')], 
                [sg.Push(),sg.Col(button_col_sql),sg.Push()]
                ]
    return sg.Window('Window 3', layout, finalize=True)

##################################################################

window1, window2, window3 = make_window1(), None, None

i=0
h=0
types = ['string','int','long','float','double','timestamp']

while True:
    window, event, values = sg.read_all_windows()

    if window == window1:
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == 'k_botao_arq':
            window1.hide()
            window2 = make_window2()
        if event == 'k_botao_db':
            window1.hide()
            window3 = make_window3()

    if window == window3:
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    if window == window2:
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'k_conf_arq':
            try:
                val_path = values['k_path']
                val_sep = values['k_sep']
                val_header = values['k_header']
                val_encd = values['k_encd']
                df = pd.read_csv(val_path, sep=val_sep)
                column_names = list(df.columns)
                for z in range(len(column_names)):
                    window.extend_layout(window['k_col_type'], [[sg.Push(), sg.T('{}'.format(column_names[z]), key=f'k_col_type_nam{z}'), sg.Combo(values=types, default_value=types[0], size=(25,6), readonly=True, enable_events=True, key=f'k_col_type_val{z}'), sg.In(key=f'k_col_type_fmt{z}')]])
                    window.visibility_changed()
                window['k_col_type'].contents_changed()
            except:
                sg.popup_error('Você deve selecionar um arquivo primeiro!', title='Error')

        elif event == 'k_rename_col':
            try:
                window.extend_layout(window['k_col'], [[sg.Combo(values=column_names, default_value='Selecione a coluna...', size=(25,5), readonly=True, key=f'k_col_nam{i}'), sg.In(key=f'k_col_ren{i}')]])
                window.visibility_changed()
                window['k_col'].contents_changed()
                i += 1
            except:
                sg.popup_error('Você deve selecionar e confirmar um arquivo antes!', title='Error')

        elif event == 'k_add_col_novo':
            window.extend_layout(window['k_col_novo'], [[sg.In(default_text='Nome do campo', key=f'k_col_novo_nam{h}', size=(25,1)), sg.In(default_text='Codigo livre em python' ,key=f'k_col_novo_val{h}')]])
            window.visibility_changed()
            window['k_col_novo'].contents_changed()
            h += 1

        elif event == 'k_conf_alt':
            try:
                list_col_names = []
                list_col_renames = []
                list_col_type_names = []
                list_col_type_vals = []
                list_col_novo_nam = []
                list_col_novo_val = []
                list_col_type_fmt = []
                for x in range(i):
                    col_name= values[f'k_col_nam{x}']
                    col_rename= values[f'k_col_ren{x}']
                    list_col_names.append(col_name)
                    list_col_renames.append(col_rename)
                for t in range(h):
                    col_novo_nam= values[f'k_col_novo_nam{t}']
                    col_novo_val= values[f'k_col_novo_val{t}']
                    list_col_novo_nam.append(col_novo_nam)
                    list_col_novo_val.append(col_novo_val)
                for v in range(len(column_names)):
                    col_type_name= column_names[v]
                    col_type_val= values[f'k_col_type_val{v}']
                    col_type_fmt= values[f'k_col_type_fmt{v}']
                    if col_type_val != 'Selecione o tipo do dado...':
                        list_col_type_names.append(col_type_name)
                        list_col_type_vals.append(col_type_val)
                        list_col_type_fmt.append(col_type_fmt)
                    else:
                        sg.popup_error('Obrigatório: Você deve definir o tipo da coluna {}!'.format(column_names[v]), title='Error')
                sg.popup_ok('Agora ordene os campos na aba "Sort Fields"', title='Aviso')
            except:
                sg.popup_error('Você deve selecionar e confirmar um arquivo antes!', title='Error')  

        elif event == 'k_order_bt':
            try:
                list_ordered_cols = column_names
                if list_col_names:
                    for i in range(len(list_ordered_cols)):
                        for j in range(len(list_col_names)):
                            if list_ordered_cols[i] == list_col_names[j]:
                                list_ordered_cols[i] = list_col_renames[j]
                list_ordered_cols = list_ordered_cols+list_col_novo_nam
                for s in range(len(list_ordered_cols)):
                    window.extend_layout(window['k_order_col'], [[sg.Combo(values=list_ordered_cols, default_value=list_ordered_cols[s], size=(25,5), readonly=True, key=f'k_order_col_nam{s}')]])
                window.visibility_changed()
                window['k_order_col'].contents_changed()
                window['k_conf_order_bt'].update(visible=True)
            except:
                sg.popup_error('Você deve realizar e confirmar as alterações anteriores!', title='Error')

        elif event == 'k_conf_order_bt':
            list_new_ordered_cols = []
            for r in range(len(list_ordered_cols)):
                new_ordered_cols= values[f'k_order_col_nam{r}']
                list_new_ordered_cols.append(new_ordered_cols)

        elif event == 'k_partition':
            if values['k_partition'] == True:
                window['k_name_partit'].update(visible=True)
            else:
                window['k_name_partit'].update(visible=False)

        elif event == 'k_conf_dest':
            try:
                val_path_dest = values['k_path_dest']
                val_name_app = values['k_name_app']
                val_write_mode = values['k_write_mode']
                val_partition = values['k_partition']
                val_name_partit = values['k_name_partit']
            except:
                sg.popup_error('Você deve indicar um caminho destino primeiro!', title='Error')

        elif event == 'k_ger_scrt':
            try:
                f = open("script_python.py","a+")

                config_spark = ["# -*- coding: utf-8 -*-\n",
                    "from pyspark import SparkConf, SparkContext\n",
                    "from pyspark.conf import SparkConf\n",
                    "from pyspark.sql import SparkSession, Dataframe, SQLContext\n",
                    "from pyspark.sql.functions import *\n",
                    "from pyspark.sql.types import *\n",
                    "from datetime import datetime, timedelta, date\n",
                    "import time\n",
                    "import os\n",
                    "import sys\n\n",

                    "spark = SparkSession \\\n",
                    "        .builder \\\n",
                    "        .master('local[*]') \\\n",
                    "        .appname('{}') \\\n".format(val_name_app),
                    "        .config('hive.exec.dynamic.partition.mode', 'nonstrict') \\\n",
                    "        .getOrCreate()\n\n"
                    ]

                f.writelines(config_spark)
                f.write("df = spark.read.options(header='{f_header}', delimiter='{f_sep}', encoding='{f_encd}').csv('{f_path}')\n\n".format(f_sep=val_sep, f_path=val_path, f_header=val_header, f_encd=val_encd))

                for u in range(len(list_col_type_names)):
                    if list_col_type_vals[u] != 'timestamp':
                        f.write("df = df.withColumn('{}',col('{}').cast('{}'))\n".format(list_col_type_names[u], list_col_type_names[u], list_col_type_vals[u]))
                    else:
                        f.write("df = df.withColumn('{}', to_timestamp('{}','{}'))\n".format(list_col_type_names[u], list_col_type_names[u], list_col_type_fmt[u]))
                
                if list_col_names:
                    for y in range(len(list_col_names)):
                        f.write("df = df.withColumnRenamed('{}','{}')\n".format(list_col_names[y], list_col_renames[y]))
                else:
                    pass

                if list_col_novo_nam:
                    for s in range(len(list_col_novo_nam)):
                        f.write("df = df.withColumn('{}',{})\n".format(list_col_novo_nam[s], list_col_novo_val[s]))
                else:
                    pass

                f.write("\ncolunas_ordenadas = {}\n\n".format(list_new_ordered_cols))
                f.write("df = df.select(*colunas_ordenadas)\n\n")

                if val_partition == True:
                    f.write("df.coalesce(1).write.mode('{}').partitionBy('{}').parquet('{}')\n".format(val_write_mode ,val_name_partit ,val_path_dest))
                else:
                    f.write("df.coalesce(1).write.mode('{}').parquet('{}')\n".format(val_write_mode ,val_path_dest))
            except:
                sg.popup_error('Você deve confirmar as alterações anteriores antes!', title='Error')

window.close()

############ ROTEIRO ##################
# 1 - Criar função de campo novo - OK
# 2 - Criar função de ordenar campos
# 3 - Incluir campo de caminho destino da tabela (nome app, caminho dest, write mode, partição) - OK
# 4 - Corrigir campo tipo Timestamp, incluindo format de datahora - OK
# 5 - Criar função de criar a tabela
# 6 - Colocar um Logo e identidade visual

