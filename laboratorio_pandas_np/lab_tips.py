import pandas as pd
import numpy as np
import seaborn as sns

print("pd.__version__", pd.__version__)

# Formateo de decimales
pd.options.display.float_format = '{:,.3f}'.format

df_tips = sns.load_dataset('tips')
print(df_tips.head())

print(df_tips.describe(include='all'))

# Conteo de datos por columna
print(df_tips['day'].value_counts())

# Agrupacion por columna y aplicando la media
print(df_tips.groupby('sex').mean())

# Creando una nueva columna con operaciones entre columna
df_tips['prct_tip'] = df_tips['tip'] / df_tips['total_bill']
print(df_tips.tail())

# Agrupacion por columna, pivoteando otras columnas y aplicando funciones
print(df_tips.groupby('sex')[['total_bill', 'prct_tip']].describe())


# Aplicando funciones a columnas
def mean_eur2usd(x):
    y = np.mean(x) * 1.12
    return y


# Agrupacion por una columna, pivoteando otras columnas aplicando funciones
print(df_tips.groupby('sex')[['total_bill', 'prct_tip']].apply(mean_eur2usd))
# Agrupacion por mas de una columna, pivoteando otras columnas aplicando funciones
print(df_tips.groupby(['sex', 'time'])[['total_bill', 'prct_tip']].apply(mean_eur2usd))
# Agrupacion por mas de una columna, aplicando una lambda
print(df_tips.groupby(['sex', 'time'])[['total_bill', 'prct_tip']].apply(lambda x: np.mean(x) * 1.12))

# Agrupacion por mas de una columna, aplicando mas de una funcion
print(df_tips.groupby(['sex', 'time'])[['total_bill', 'prct_tip']].aggregate([np.mean, np.max, np.sum]))

# Usando un diccionario para definir todas las funciones a aplicar a la agrupacion
dict_agg = {
    'tip': [min, max],
    'total_bill': [np.mean, mean_eur2usd],
    'prct_tip': [lambda x: np.mean(x) * 1.12, np.sum]
}

print(df_tips.groupby(['sex', 'time'])[['tip', 'total_bill', 'prct_tip', ]].aggregate(dict_agg))


# Filtrando agrupacion por una funcion
def f_filter(x):
    return mean_eur2usd(x['total_bill'].mean()) > 20


# Agrupa por mas de una columna, y retorna los resultados que cumplan con el filtro
df_filtered = df_tips.groupby(['sex', 'time']).filter(f_filter)
print(df_filtered.shape)

# Contando registros a partir de la agrupacion
print(df_filtered.groupby(['sex', 'time']).count())

# Creando una columna con el valor 1, que servira para hacer conteos en las agrupaciones
df_tips['ones'] = 1
print(df_tips.head())
# Usando la columna de ones para sumar en la agrupacion, suponiendo que 1 registro equivale a un dato valido
df_g = df_tips.groupby(['sex', 'smoker'])[['ones']].sum()
print(df_g)

# Usando la agrupacion formada, y aplicando sobre alguno de los niveles de la agurpacion una funcion
# Para este caso se esta sacando el porcentaje de participacion
print(df_g.groupby(level=0).apply(lambda x: x.sum() * 100))

# Segmentacion de datos , agrupando en rangos un valor numerico haciendolo categorico
# bins = [rangos a cortar la agrupacion]
df_tips['bin_total'] = pd.cut(df_tips['total_bill'], bins=[3, 18, 35, 60])
print(df_tips.head())

# Conteo de los valores que pertenecen dentro de cada rango
print(pd.cut(df_tips['total_bill'], bins=[3, 18, 35, 60]).value_counts())

# Agrupando por mas de una columna, usando la columna ones para el conteo
print(df_tips.groupby(['time', 'bin_total'])[['ones']].count())

# Misma operacion de agrupacion, pero obteniendo la participacion por el nivel 0 de agrupacion
df_partipacion = df_tips.groupby(['time', 'bin_total'])[['ones']].count().groupby(level=0).apply(
    lambda x:
    x / x.sum() * 100
)
print(df_partipacion)

"""
TABLAS PIVOTE
"""
print(df_tips.groupby(['sex', 'time'])[['total_bill']].mean())

# Añadinedo indices numericos al dataframe
df_gp = df_tips.groupby(['sex', 'time'])[['total_bill']].mean().reset_index()
print(df_gp)

# Usando la tabla pivote
# pivot_table(values=['valores a operar'], index=[filas o nivel de agrupacion], columns=[columnas a pivotear], aggfunc=[funciones a operar])
# Si no se especifica el valor de aggfunc realizara la media por default
print(df_gp.pivot_table(values='total_bill', index='sex', columns='time'))
print(df_tips.pivot_table(values='total_bill', index='sex', columns='time'))

df_pivot = df_tips.pivot_table(values=['total_bill', 'bin_total'], index=['sex'], columns=['time'], aggfunc=[np.median, np.std])
print(df_pivot)

# .unstack() Transformando el dataframe columnas a filas
# .reset_index() Genera indices numericos
print(df_pivot.unstack().reset_index())
