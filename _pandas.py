# pip install pandas
import numpy as np
import numpy as np
import pandas as pd

"""
Pandas => Panel Data
"""

import pandas as pd
import numpy as np
from devtools import debug
import sys

# sys.exit()

print("Version pandas >>>>", pd.__version__)
# serie  => arreglo de una dimencion, que permite generar el indice de cada posicion numerico o string, funciona todas las funciones del arreglo
# dataframe => similar a una matriz extendida, como una hoja de excel, para almacenar el nombre de las filas y columnas

# .Series([lista], [indice])
# crea una lista con indice configurable
serie1 = pd.Series([1, 2, 3, 4])
print("serie1", serie1)

# especificamos los indices para cada posicion
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
# devuelve los valores de la Serie o el DF a un arreglo de np
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
                   columns=['COLUM_A', 'COLUM_B', 'COLUM_C', 'COLUM_D', 'COLUM_E'],  # Nombres columnas
                   index=['ROW_A', 'ROW_B', 'ROW_C'])  # Nombres Filas para que no sean numericas
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

# =============================================
# slicing de un df como un array
print(df3)
print("df3[0:3]", df3[0:3])

# =============================================
# seleccion de columnas
print(df3)
print("df3[0:3]", df3[['A_COLUMN', 'B', 'C']])

# ==============================================
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
print("df3.loc[df3.A_COLUMN > 10]",
      df3.loc[df3.A_COLUMN > 10, ['A_COLUMN', 'E']].sort_values('A_COLUMN', ascending=False).head(2))
# Filtro sobre una varias columnas que complan la condicion
print("df3[(df3['A_COLUMN'] >= 15) & (df3['A_COLUMN'] <= 50)] ", df3[(df3['A_COLUMN'] >= 15) & (df3['A_COLUMN'] <= 50)])
# Otra forma de ejecutar el query
print("df3.query('A_COLUMN > 50')", df3.query('A_COLUMN > 50'))
print("df3.query('A_COLUMN > 50 & B < 65')", df3.query('A_COLUMN > 50 & B < 65'))

# accediendo a una fila por position entero
# .iloc[posicion_indice]
print("df3.iloc[0]", df3.iloc[0])

# Obteniendo un rango de filas, por un rango de indices
print("df3.iloc[0:2]", df3.iloc[0:2])

# Obteniendo un rango de filas, por un rango de indices, indicando que columnas mostrar pero pasando la posicion de la columna en una lista
print("df3.iloc[0:2]", df3.iloc[0:2, [0]])

# Obteniendo desde el inicio hasta la fila 2, y desde la columna 2 al final
print("df3.iloc[:2 , 2:]", df3.iloc[:2, 2:])

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

# setean pandas para que para que todo los que se importe sin valor sea nan
pd.options.mode.use_inf_as_na = True
df = pd.DataFrame(diccionario_df_calificaciones)

# Permite asignar un valor a los valores nan
print("df.fillna(0)", df.fillna(0))

# Permite eliminar para la o las columnas los valores nan
print("df[['usuarios']].dropna()", df[['usuarios']].dropna())

# todo lo que sea nan, lo reemplazara por el siguiente valor no nan
print("df.fillna(method='ffill')", df.fillna(method="ffill"))

# todo lo que sea nan, lo reemplazara por el anterior valor no nan
print("df.fillna(method='bfill'", df.fillna(method="bfill"))

# ===============================================================
# Eliminando filas y columnas

# Eliminando columnas // axis = 0 Filas | 1 Columnas
# inplace=True // modifica por referencia el df
print("df.drop('usuarios', axis=1)", df.drop('usuarios', axis=1))
print("df.drop(2, axis=0)", df.drop(2, axis=0))
print("df.drop([0, 2], axis=0)", df.drop([0, 2], axis=0))
# drop_duplicates()  // eliminar duplicados
# keep='last'  // last | first  // controla cual deja o cual elimina
print("df.drop_duplicates", df.drop_duplicates(keep='last'))

# ===============================================================
# Añadir Columnas

# Añadiendo columna con nan
df['Nueva_columna_nan'] = np.nan
print("df columna nan", df)

df['Calificaciones_al_cuadrado'] = df['calificaciones'] ** 2
print("df columna calificaciones ** 2 ")
print(df)

new_column = np.arange(0, df.shape[0])
df['Nueva_columna_arange'] = new_column
print("df columna arange")
print(df)

# Añadir filas

print('Añadiendo el mismo df en si al final')
print(df.append(df))
print('Añadiendo una fila desde dict')
diccionario_df_calificaciones_row = {
    'usuarios': 'Oscar',
    'calificaciones': 10,
    'edades': np.nan,
    'Nueva_columna_nan': 4,
    'Calificaciones_al_cuadrado': 100,
    'Nueva_columna_arange': np.nan
}
df = df.append(diccionario_df_calificaciones_row, ignore_index=True)
print(df)

print('Rellenando valores nan')
print(df.fillna(500))
print('Rellenando valores nan especifica columna')
print(df['Nueva_columna_arange'].fillna(1000))

# interpolate // en valores numericos hace una inferencia en los valores de la columna
print('df interpolate')
print(df.interpolate())

# ==========================================
# Filtros
# ~ // se usa para negar la condicion en el filtro
filtro_1 = df['calificaciones'] > 8  # Genera una serie de booleanos
print("filtro_1", filtro_1)
filtro_2 = df['usuarios'].str.contains("G")
print("filtro_2", filtro_2)
print('Aplicando los filtros')
print(df[filtro_1 & filtro_2])

# ===================================
# Building functions informacion

# .info() // informacion relevante del dataset
print("df.info()", df.info())
# .describe() // datos estadisticos de las columnas numericas
print("df.describe()", df.describe())
# .head(n) // primeros registros
print("df.head()", df.head())
# .tail(n) // ultimos registros
print("df.tail()", df.tail())
# .memory_usage(deep=True)  // Informacion sobre la memoria que consume el dataset
print("df.memory_usage()", df.memory_usage(deep=True))
# .value_counts()  // agrupa y cuenta las veces que se repite
print("df['usuarios'].value_counts()", df['usuarios'].value_counts())

# .skew()  // saber el sesgo de los campos numericos
"""
Si γ 1 > 0 la distribución es asimétrica positiva o a la derecha.
Si γ 1 < 0 la distribución es asimétrica negativa o a la izquierda.
"""
print("df.skew()", df['Calificaciones_al_cuadrado'].skew())

# =================================================
# Cambiar el tipo de dato
# .astype('string')  // tipo
df['usuarios'] = df['usuarios'].astype('string')
print(df['usuarios'])

# ===============================================
# Group by & funciones de agregacion

"""
.count()
.mean()
.sum()
.min()
.max()
"""
print(df.groupby('usuarios').count())
# mas de un nivel de agrupacion
print(df.groupby(['usuarios', 'edades']).count())
# .reset_index()  // deja el indice normal, y quita el de la columna usuario como indice
print(df.groupby('usuarios').count().reset_index())
# varias funciones de agregacion por cada una de las columnas
print(df.groupby('usuarios').agg(['min', 'max', 'sum', 'mean']))
# especificando la columna y las funciones a aplicar
print(df.groupby('usuarios').agg({'edades': ['mean', 'max'], 'Calificaciones_al_cuadrado': ['min', 'max']}))
# ejecutando funciones lamda o propias sobre la agrupacion
print(df.groupby('usuarios').agg({'edades': lambda x: [i + 20 for i in x]}))

# ===============================================
# Buscar b | Join | Cruzar df
data_1 = {
    'key': ['1', '2', '3'],
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2'],
    'C': ['C0', 'C1', 'C2'],
}

data_2 = {
    'key': ['1', '2', '4'],
    'A': ['A4', 'A5', 'A6'],
    'B': ['B4', 'B5', 'B6'],
    'C': ['C4', 'C5', 'C6'],
}

df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

# merge // es un inner join
# on='' llave de relacion
print(df_1.merge(df_2, on='key'))
# especificando cual es la llave en el df izquierda y cual en el de la derecha
# left_on='key', right_on='key'
print(df_1.merge(df_2, left_on='key', right_on='key'))
# how = left | right | inner  // especifica el tipo de cruce a ejecutar
print(df_1.merge(df_2, left_on='key', right_on='key', how='left'))

# Concatenar | añadir los valores por el axis // 0 filas | 1 columnas
# .concat([df1, df2 ....], axis=0)
print(pd.concat([df_1, df_2], axis=0))
print(pd.concat([df_1, df_2], axis=1))
# ignore_index=True // permite no tener en cuenta los indices y genera unos nuevos
print(pd.concat([df_1, df_2], axis=0, ignore_index=True))

# Join - Index match

# Se especifica cual va a ser el key

izq = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']},
    index=['k0', 'k1', 'k2'])

der = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']},
    index=['k0', 'k2', 'k3'])

print(izq.index)
print(der)
# how= inner | left | right | outer // todos los datos
print(izq.join(der, how='inner'))

# ===============================================
# Pivot Table  // Similar a tabla dinamica
diccionario_df_calificaciones = {
    'usuarios': ['Gustavi', 'Meliza', 'Martha'],
    'generos': ['hombre', 'mujer', 'mujer'],
    'calificaciones': [10, 8, 9],
    'edades': [24, 22, 54],
}

df_pv = pd.DataFrame(diccionario_df_calificaciones)
print(df_pv.pivot_table(index='usuarios', columns='generos', values='calificaciones', aggfunc='sum'))


# ===============================================
# Melt -> dinamizar de columnas a filas, con dos nuevas columnas para especificar la antigua columna y el valor que traía.
print(df_pv[['usuarios', 'edades']])
print('========== Dinamizacion con Melt =============')
print(df_pv[['usuarios', 'edades']].melt())
print('========== Dinamizacion con Melt =============')
# Simplemente, podemos seleccionar las columnas que no quiero hacer melt usando el parámetro id_vars.
print(df_pv.melt(id_vars='usuarios', value_vars='edades'))


# =========================================
# Apply  // permite ejecutar operaciones sobre el DF
# axies = 0 fillas | 1 columnas

print('========== Apply =================')
diccionario_df_calificaciones = {
    'usuarios': ['Gustavi', 'Meliza', 'Martha'],
    'generos': ['hombre', 'mujer', 'mujer'],
    'calificaciones': [10, 8, 9],
    'edades': [24, 22, 54],
}
df_apply = pd.DataFrame(diccionario_df_calificaciones)

def pow_value(value: int, pow: int = 2) -> int:
    return value ** pow

print('Pow function apply')
df_apply['edades_pow'] = df_apply['edades'].apply(pow_value)
df_apply['edades_pow_lambda'] = df_apply['edades'].apply(lambda x: x ** 2)
df_apply['edades_pow_3_condition'] = df_apply.apply(lambda columns: columns['edades'] ** 3 if columns['generos'] == 'mujer' else columns['edades'], axis=1)

print(df_apply)
