import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_climate = pd.read_csv('./../db/GlobalLandTemperaturesByCountry.csv')
print(df_climate.shape)
print(df_climate.head())

# .info()
# Resumen del df y consumo de memoria
print(df_climate.info())

# Acceder a los valores unicos de una columna
print(df_climate['Country'].unique())

# Seteando columna de tipo tiempo
df_climate['date'] = pd.to_datetime(df_climate['dt'])
print(df_climate.dtypes)

# Creando una serie como filtro
idx_filtro = df_climate['date'] > pd.to_datetime('1970-01-01')
df_climate = df_climate[idx_filtro]
print(df_climate.shape)

# Agrupacion por columnas y por fechas usando frecuencias o intervalor
# pd.Grouper(key='COLUMNA', freq='Rango')

apply_functions = {
    'AverageTemperature' : [np.mean, np.median]
}

df_avg = df_climate.groupby(['Country',
                    pd.Grouper(key='date', freq='1Y')]).aggregate(apply_functions)
print(df_avg)

# Filtro de filas, devolviendo otra columna agrupada
print(df_avg.loc['Mexico']['AverageTemperature'])

# Un df a partir de una agrupacion, generando un id numerico
df_t_med = df_avg['AverageTemperature'][['median']].reset_index()
print(df_t_med.head(5))

# Extrayendo partes de fecha a partir de un tipo date
df_t_med['year'] = df_t_med['date'].dt.year
print(df_t_med.head(5))

# Renombrando columnas
# columns={'current_name_column':'new_name_column'}
# inplace=True // modifica el mismo dataframe
df_t_med.rename(columns={'median':'median_temperature'}, inplace=True)
print(df_t_med.head(5))

# Tabla pivote
# values=['median_temperature'] // valor a calcular
#  index=['year'] // filas o agrupacion
# columns=['Country'] // columnas a pivotear horizontalmente
df_t_pivot = df_t_med.pivot_table(values=['median_temperature'], index=['year'], columns=['Country'])
print(df_t_pivot)

# Generando un grafico de caja de bigotes o boxplot
# .sample(value) // Escoge aletariamente la cantidad de registros especificados
df_t_pivot_sample = df_t_pivot.T.sample(2).T.boxplot()
plt.show()

