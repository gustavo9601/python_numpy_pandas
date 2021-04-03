import pandas as pd
import numpy as np
import sys

# Definiendo el formateo decimal
pd.options.display.float_format = '{:,.1f}'.format

df_meteorites = pd.read_csv('../db/Meteorite_Landings.csv')
print(df_meteorites.sample())

# .shape
# retorna filas y columnas del archivo
print("df_meteorites.shape", df_meteorites.shape)

# .describe()
# Resumenm estadistico
print(df_meteorites.describe())
print(df_meteorites.describe(include='all'))

# .info()
# .dtypes() // Informacion de tipo de columna
# Informacion de categoria y tipo
print(df_meteorites.dtypes)
print(df_meteorites.info())
# .convert_dtypes().dtypes
# Trasnformacion de datos mas compresibles (Object => string)
print(df_meteorites.convert_dtypes().dtypes)

# .nunique()
# Hace un distinc de cada valor unico sobre cada columna, retornando la cantidad encontrada
# Sirve para identificar rapidamente valores categoricos
print(df_meteorites.nunique())
# .nunique()
# aplicado a una columna realiza, el distinc y muestra los valores unicos
print(df_meteorites['fall'].nunique())
# .value_counts()
# realiza la agrupacion por valores unicos, mostrando la cantidad
print(df_meteorites['fall'].value_counts())

# Seteando variables string a variables categoricas, para mejorar el performance
print(df_meteorites[['fall', 'nametype']])
df_meteorites[['fall', 'nametype']] = df_meteorites[['fall', 'nametype']].astype('category')
print(df_meteorites.dtypes)

print(df_meteorites['year'])

# Seteando las fechas
# errors='coerce', // si al parsear genera error, colocara un nan
df_meteorites['year'] = pd.to_datetime(
    df_meteorites['year'],
    errors='coerce',
    format='%m/%d/%Y %H:%M:%S %p'
)

# Renombrando una columna sin reasignar
# inplace=True // Reemplaza a la ves que se ejecuta
df_meteorites.rename(columns={'mass (g)': 'mass_update'}, inplace=True)

# Creando una columna en un DF
df_meteorites['nueva_columna'] = 1
print(df_meteorites.head())
# Eliminando una columna
# axis=1 // 1 columna || 0 fila
df_meteorites.drop(['nueva_columna'], axis=1, inplace=True)
# especificando las columnas y filas a liminar
df_meteorites.drop(columns=['id', 'recclass'], index=[0, 2, 4, 6, 8], inplace=True)

# Eliminando los registros con nan
df_meteorites['mass_update'] = df_meteorites['mass_update'].dropna()
print(df_meteorites.head())

# Haciendo una copia full del df
copy_of_meteorites = df_meteorites.copy(deep=True)
