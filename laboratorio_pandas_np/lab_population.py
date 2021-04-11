import pandas as pd
import numpy as np

# Set format display values in PD
pd.options.display.float_format = '{:,.1f}'.format

df_population = pd.read_csv('./../db/poblacion.csv')
print(df_population.shape)
print(df_population.describe)

# Seteando la columna como categorical
df_population['year'] = pd.Categorical(df_population['year'])
print(df_population.dtypes)

# Creando una Serie o indice como filtro
idx_filtro = df_population['Country'].isin(['Aruba', 'Colombia'])

df_population_filtered = df_population[idx_filtro]
print(df_population_filtered.describe)

# Seteando los indices del DF
# .sort_index(ascending = [True, False, True]) // Indica el orden de ascendencia para cada columna seteanda como index
df_population_filtered = df_population_filtered.set_index(['Country', 'year']).sort_index()
print(df_population_filtered.describe)

# Sleccionado por un indice
print(df_population_filtered.loc['Colombia', :])

# Seteando el index
df_population = df_population.set_index(['Country', 'year']).sort_index(ascending = [True, False])
print(df_population.describe)

# Acceduebdi a traves de ubduces a un valor
print(df_population['pop']['Colombia'])

# Operaciones sobre indices
# level='indice', se especifica a que nivel se requiere la aplicacion de la operacion o funcion
print(df_population.sum(level='year'))


# Pivoteando un indice de filas a columnas
# unstack('year') | ['col1', 'col2'] // pivotea las filas a columnas
print(df_population_filtered.unstack(['year']))



df_population_2 = pd.read_csv('./../db/poblacion.csv')
# Formateando los strings
df_population_2['Country'] = df_population_2['Country'].str.lower()
# Consultando por conincidencias
# .str.contains('col') // devuelve true o false
print(df_population_2['Country'].str.contains('col'))

# en lugar de que regrese valores booleanos metemos la funcion en corchetes y todas
# las filas donde el valor sea True va ha devolver el valor de la fila
print(df_population_2[['Country', 'year']][df_population_2['Country'].str.contains( 'col' )])