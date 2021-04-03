# pip install pandas

"""
Pandas => Panel Data
"""

import pandas as pd
import numpy as np
import sys
# sys.exit()

print("Version pandas >>>>", pd.__version__)
# serie  => arreglo de una dimencion, que permite generar el indice de cada posicion numerico o string, funciona todas las funciones del arreglo
# dataframe => similar a una matriz extendida, como una hoja de excel, para almacenar el nombre de las filas y columnas

# .Series([lista], [indice])
# crea una lista con indice configurable
serie1 = pd.Series([1, 2, 3, 4])
print("serie1", serie1)

# especificamos los dicndes para cada posiocion
serie2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print("serie2", serie2)

# accediendo a la serie, pasando una lista como busqueda
print("serie2[['a', 'd']]", serie2[['a', 'd']])



# Creando una serie a partir de un diccionario, para que venga con los indices y valor
diccionario1 = {
    'a': 100,
    'b': 200,
    'c': 300
}

serie_from_diccionario = pd.Series(diccionario1)
print("serie_from_diccionario", serie_from_diccionario)

# diccionario desde valores generados por np
serie_from_np = pd.Series(np.arange(0, 5), index=['a', 'b', 'c', 'd', 'e'])
print("serie_from_np", serie_from_np)


# devuelve tamaño de la serie
print("serie_from_diccionario.shape", serie_from_diccionario.shape)
# devuelve los inidces
print("serie_from_diccionario.index", serie_from_diccionario.index)
# devuelve los valores
print("serie_from_diccionario.values", serie_from_diccionario.values)
# trasnforma los indices a arreglo
print("serie_from_np.index.tolist()", serie_from_np.index.tolist())
# Colocando nombre al indice
serie_from_np.index.name = 'Indices Manual'
print("serie_from_np con nombres en columnas", serie_from_np)

# operaciones al igual que un arreglo
print("serie_from_np *10", serie_from_np * 10)
# filtros con operadores logicos al ser tambien un arreglo de una dimension
print("serie_from_np[serie_from_np > 2]", serie_from_np[serie_from_np > 2])
# filtro puntual por varias posiciones
print("serie_from_np[['a', 'd']]", serie_from_np[['a', 'd']])

# serie generada con NaN nulos
serie_con_nulos = pd.Series([1, 2, 3, np.NaN, 5, 6, np.NaN, 7])
print("serie_con_nulos", serie_con_nulos)
# validando si la serie tiene nulos
# pd.isNull(serie) devuelve otra serie en funcion de cada posicion devolvera true si es null en caso contrario false
print("pd.isnull(serie_con_nulos)", pd.isnull(serie_con_nulos))

# Eliminando valores nulos de una serie
# serie.dropna()   # genera una nueva serie, por ello se debe reasignar
serie_con_nulos = serie_con_nulos.dropna()
print("serie_con_nulos.dropna()", serie_con_nulos)

# Seleccionado los elementos que nos son nulos
# serie.notnull() // devuelve una Serie con booleanos identificando cuales no son nulos como True,
# al ser pasado como parametro permite filtrar la serie a los que tengan True
print("serie_con_nulos[serie_con_nulos.notnull()]", serie_con_nulos[serie_con_nulos.notnull()])

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

# *********************************************************** #
# *********************************************************** #
# *********************************************************** #
# *********************************************************** #
# Dataframes

# Accediendo de forma directa
# Primero se accede a columna ['nameColumn'] || .nameColum Luego se accede a la fila u operaciones

# permite crear matricez y colocarles nombre a sus columnas y setear tambien el nombre de las filas para su acceso con indices
# list() parsea a una lista el iterable
# df1 = pd.DataFrame(np.random.randn(4, 2), columns=['A','B'])
df1 = pd.DataFrame(np.random.randn(4, 2), columns=list('AB'))
print("df1", df1)

# creando un dataframe a partir de un diccionario
# los keys del diccionario representaran las columnas, y los values las filas
usuarios_diccionario = {
    'nombre': ['gus', 'mel', 'mar'],
    'notas': [9, 10, 8],
    'edad': [25, 26, 30],
    'aprobado': [True, False, True]
}
# index=[lista con indices]
df_from_diccionario = pd.DataFrame(usuarios_diccionario)
print("df_from_diccionario", df_from_diccionario)

# acceder al dataframe, estilo arreglo, pero pasando el idice, o como un objeto
# df_from_diccionario.nombre
print("df_from_diccionario['nombre']", df_from_diccionario['nombre'])
# obteniendo los valores de una columna, los retorna com ouna lista
# dataframe.nombreColumna.values
print("df_from_diccionario.edad.values", df_from_diccionario.edad.values)

# Obteniendo el nombre de las columnas
print("df_from_diccionario.colums", df_from_diccionario.columns)
# Obteniendo los indices
print("df_from_diccionario.index", df_from_diccionario.index)
# Obteniendo los solos los valores como arreglo matriz
print("df_from_diccionario.values", df_from_diccionario.values)

# Genera un data frame similar  aun excel page
# usa los nombres de las columnas iguales al del diccionario data
data = {
    'Nombres': ['Gus', 'Lau', 'Mar', 'Sergui', 'Migue'],
    'Edades': [24, 22, 54, 21, 10],
    'Pruebas': [1, 2, 3, 5, 10]
}
# columns = [] recibe en un arreglo, el ordenamiento y nombre de columna que queremos mostrar  // el nombre debe ser el mismo que se define en la data
df2 = pd.DataFrame(data, columns=['Nombres', 'Edades'])
print(df2)

# pd from np, asginando nombres a las columnas con columns=[] y a los indices con index=[]
df3 = pd.DataFrame(np.random.randint(0, 101, (3, 5)),
                   columns=['COLUM_A', 'COLUM_B', 'COLUM_C', 'COLUM_D', 'COLUM_E'],   # Nombres columnas
                   index=['ROW_A', 'ROW_B', 'ROW_C'])   # Nombres Filas para que no sean numericas
print(df3)
# Modiciadno el nombre de las columnas, en la misma posicion logica
df3.columns = 'A', 'B', 'C', 'D', 'E'
print(df3)
# Modiciadno el nombre de los indices, en la misma posicion logica
df3.index = 'a', 'b', 'c'
print(df3)
# Modificando puntualmente una columna o indice
# .rename(columna={en diccionario pasa como key el valor actual, y como valor el dato a reemplazar}, index={})
# se debe realizar la asginacion de nuevo, ya que no modifica el valor por referencia
df3 = df3.rename(index={'a': 'A_ROW'}, columns={'A': 'A_COLUMN'})
print(df3)

# Accedemos al DF con la misms caracteristicas de una matriz en np
# accediendo en forma de objeto o arreglo a una columna
print("df3['A_COLUMN']", df3['A_COLUMN'])
print("df3.A_COLUMN", df3.A_COLUMN)
# mismo filtros en forma de arreglo
print("df3.A_COLUMN[df3.A_COLUMN > 50]", df3.A_COLUMN[df3.A_COLUMN > 50])
# Accediendo a una posicion fija
print(df3['A_COLUMN']['A_ROW'])

#==============================================
# accediendo a una fila por string
# .loc['nombre_fila_indice']
print(df3)
print("df3.loc['A_ROW']", df3.loc['A_ROW'])
# accediendo a un rango de filas por rango de indices
print("df3.loc['b':'c']", df3.loc['b':'c'])
# accediendo a un rango de filas por rango de indices Y Obteniendo una o mas columnas, pasando en una lista el nombre de columnas
print("df3.loc['b':'c',['A_COLUMN']]", df3.loc['b':'c', ['A_COLUMN']])
# listando todos las filas en base auna condicion por columna
print("df3.loc[df3.A_COLUMN > 50]", df3.loc[df3.A_COLUMN > 50])
# listando todos las filas en base auna condicion por columna, y especificando en una lista el nombre de columnas a mostrar
print("df3.loc[df3.A_COLUMN > 50]", df3.loc[df3.A_COLUMN > 50, ['A_COLUMN', 'E']])
# listando todos las filas en base auna condicion por columna, y especificando en una lista el nombre de columnas a mostrar
# y con sort_values('nombre columna') ordenamos acedentemente por columa, y con head(n_filas) especificamos el numero de filas a mostrar
print("df3.loc[df3.A_COLUMN > 10]", df3.loc[df3.A_COLUMN > 10, ['A_COLUMN', 'E']].sort_values('A_COLUMN', ascending=False).head(2))
# Filtro sobre una varias columnas que complan la condicion
print("df3[(df3['A_COLUMN'] >= 15) & (df3['A_COLUMN'] <= 50)] ", df3[(df3['A_COLUMN'] >= 15) & (df3['A_COLUMN'] <= 50)] )
# Otra forma de ejecutar el query
print("df3.query('A_COLUMN > 50')", df3.query('A_COLUMN > 50'))
print("df3.query('A_COLUMN > 50 & B < 65')", df3.query('A_COLUMN > 50 & B < 65'))


# accediendo a una fila por posicion entero
# .iloc[posicion_indice]
print("df3.iloc[0]", df3.iloc[0])

# Ontemniendo un rango de filas, por un rango de indices
print("df3.iloc[0:2]", df3.iloc[0:2])

# Ontemniendo un rango de filas, por un rango de indices, idnciando que columnas mostrar pero pasando la posicion de la columna en una lista
print("df3.iloc[0:2]", df3.iloc[0:2 , [0]])


##########################
# Aplicando funciones sobre un DF
diccionario_df_calificaciones = {
    'usuarios': ['Gustavi', 'Meliza', 'Martha'],
    'calificaciones': [10, 8, 9],
    'edades': [24, 22, 54],
}

df_calificaciones = pd.DataFrame(diccionario_df_calificaciones)
print(df_calificaciones)

# .apply(function, axis=1|0)
# funcion => retornara el valor, a evaluar por cada iteracion // En base a la modificacion se retornara una serie
# axis = 0|1 indicara si recorre fila a fila o columna por columna, 1 => fila | 0 => columna
# row['edades'] en cada iteracion retorna una fila, por ende accedemos de esa forma y le sumamos + 1 a cada valor
df_calificaciones['edades'] = df_calificaciones.apply(lambda row: row['edades'] + 1, axis=1)
print(df_calificaciones)




