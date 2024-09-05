# INCLUIR NA TABELA CALENDARIO UMA FLAG D (DAY) OU W (WEEK) E UMA FLAG UTIL (S OU N) DEPENDENDO DO CALENDARIO DO JOB SER DAY OU WEEK

# Pega o dia util do mês que essa data representa
import calendar
from datetime import datetime, timedelta

odate = '20240905'
odate = datetime.strptime(odate, '%Y%m%d')
hoje = odate.day

def calcular_dia_util(data):
    # Começa no primeiro dia do mês
    primeiro_dia = datetime(data.year, data.month, 1)
    
    # Contador de dias úteis
    dia_util = 0
    
    # Itera do primeiro dia do mês até o dia da data desejada
    while primeiro_dia <= data:
        # Se não for sábado (5) ou domingo (6), é um dia útil
        if primeiro_dia.weekday() < 5:  # 0 a 4 são dias úteis
            dia_util += 1
        
        # Avança para o próximo dia
        primeiro_dia += timedelta(days=1)
    
    return dia_util

# Exemplo de uso
# data = datetime(2023, 9, 12)  # Alterar para a data desejada
dia_mes_util = calcular_dia_util(odate)
dia_mes_util = ("D"+str(dia_mes_util))
print(dia_mes_util)

print(hoje)

# Obtendo o último dia do mês
ultimo_dia = calendar.monthrange(odate.year, odate.month)[1]
print('L'+str(ultimo_dia - odate.day+1))

from pyspark.sql import SparkSession

# Criando a sessão Spark
spark = SparkSession.builder.appName("Verificar valores com SQL").getOrCreate()

# Exemplo de DataFrame com valores separados por vírgula
data = [("D1,D2,ALL,7,15",), ("D2,30",), ("ALL,15",), ("D3,45",)]
df = spark.createDataFrame(data, ["coluna_x"])

# Exibindo o DataFrame original
print("DataFrame original:")
df.show(truncate=False)

# Registrando o DataFrame como uma tabela temporária para usar SQL
df.createOrReplaceTempView("tabela")

# Consulta SQL usando SPLIT e ARRAY_CONTAINS
query = """
SELECT 
    coluna_x,
    CASE 
        WHEN array_contains(split(coluna_x, ','), 'D1')
        OR array_contains(split(coluna_x, ','), '10')
        OR array_contains(split(coluna_x, ','), 'ALL')
        OR array_contains(split(coluna_x, ','), '7')
        THEN 'OK'
        ELSE 'NOK'
    END AS resultado
FROM tabela
"""

# Executando a consulta
resultado = spark.sql(query)

# Exibindo o resultado final
print("Resultado da consulta:")
resultado.show(truncate=False)