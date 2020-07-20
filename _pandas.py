# pip install pandas

import pandas as pd
import numpy as np

# serie  => similar a un arreglo de una dimension, que permite generar el indice de cada posicion numerico o string
# dataframe => similar a una matriz

# .Series([lista], [indice])
# crea una lista con indice configurable
serie1 = pd.Series([1, 2, 3, 4])
print("serie1", serie1)

serie2 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
print("serie2", serie2)

# acceso por posicion
# [posicion] / .iloc[posicion]
# [posicion_string] / .loc[posicion_string]
print("serie1[0]", serie1[0])
print("serie1.iloc[0]", serie1.iloc[0])
print("serie2['c']", serie2['c'])

# .data_range('YYYYMMDD', parametros)
# genera peridodos de fecha a partir de una fecha inicial
series_fechas_dias = pd.date_range('20200101', periods=5)
series_fechas_meses = pd.date_range('20200101', periods=5, freq='M')
print("series_fechas_dias", series_fechas_dias)
print("series_fechas_meses", series_fechas_meses)


# permite crear matricez y colocarles nombre a sus columnas y setear tambien el nombre de las filas para su acceso
df1 = pd.DataFrame(np.random.randn(4,2), columns=list('AB'))
print("df1", df1)


# Genera un data frame similar  aun excel page
# usa los nombres de las columnas iguales al del diccionario data
data = {
    'Nombres' : ['Gus', 'Lau', 'Mar'],
    'Edades': [24,22,54]
}

df2 = pd.DataFrame(data, columns=['Nombres', 'Edades'])
print(df2)

# exportar el dataframe a csv
df2.to_csv('df2.csv')


# importamos el csv generado anteriormente
df3 = pd.read_csv('df2.csv')
print("df3", df3)