import pandas as pd
import numpy as np
import seaborn as sns

print("version pandas >>", pd.__version__)

df_diamonds = sns.load_dataset('diamonds')
print(df_diamonds.shape)

# .groupby('cut').mean()
# agrupa por los indices por parametro, y aplica la media
print(df_diamonds.groupby(['cut']).mean())

# Aplicando la agrpacion a una sola columna
print(df_diamonds.groupby(['cut'])['carat'].count())
print(df_diamonds.groupby(['cut'])['price'].mean().to_frame())


def mean_kilo(x):
    return np.mean(x) / 1000

# Aplicando funciones personalizadas sobre la agrupaciones
# .aggregate([])
# recibe todas las funciones a ejecutar sobre la agurpacion, y estas definiaran la cantidad de columnas calculadas
print(df_diamonds.groupby(['cut', 'color'])['price'].aggregate(['min', np.mean, 'max', mean_kilo]).head(10))

# Creando un diccionario con las operaciones que se requieren aplicar a la agrupaciones
# caract => name columna
# esto creara columnas calculadas
dict_aggregate = {
    'carat' : [min, max],
    'price' : [np.mean, mean_kilo]
}
print(df_diamonds.groupby(['cut', 'color']).aggregate(dict_aggregate).head(10))

# Filtrando los datos de agrupacion
def f_filter(x):
    return mean_kilo(x['price']) > 4
print(df_diamonds.groupby(['cut', 'color']).filter(f_filter).head(10))


# Datos estadisticos para todas las columnas
print(df_diamonds.describe(include='all'))

# Cantidad de valores por columna
print(df_diamonds['cut'].value_counts())


# Cantidad de valores por columna en porcentajes
print(df_diamonds['cut'].value_counts() / df_diamonds['cut'].value_counts().sum() * 100)

# Describe en columnas especificas de la agrupacion
print(df_diamonds.groupby(['clarity'])[['price']].describe())


# *Aplicando solo una funcion se usa APPLY si se requiere aplicar multiples funciones se usa AGGREGATE*
print(df_diamonds.groupby(['clarity'])[['price', 'x']].apply(np.sum))
print(df_diamonds.groupby(['clarity'])[['price', 'x']].apply(lambda x : np.mean(x) * 1.12))