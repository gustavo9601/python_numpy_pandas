import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.3f}'.format

df_coronavirus = pd.read_csv('./../db/covid_19_data.csv')
print(df_coronavirus.shape)
print(df_coronavirus.head())

# Seteando el tipo tipo a columna
df_coronavirus['ObservationDate'] = pd.to_datetime(df_coronavirus['ObservationDate'])
print(df_coronavirus.dtypes)

# Eliminando columna
df_coronavirus = df_coronavirus.drop(['SNo'], axis=1)
print(df_coronavirus.head())

# Agrupe por una columna, y aplique para los campos numericos operaciones
df_coronavirus_time = df_coronavirus.groupby(['ObservationDate']).sum()
print(df_coronavirus_time)

print(df_coronavirus.groupby(['ObservationDate', 'Country/Region']).sum())

# Rellenando los valores nulos
df_coronavirus_time = df_coronavirus_time.fillna({'Confirmed': 555.0, 'Deaths': 17.0, 'Recovered': 28.0})
print(df_coronavirus_time.head(5))

# Acumulando los valores en cada iteracion de las filas
# .cumsum()
print(df_coronavirus_time.cumsum().head(5))

# Realizando agrupacion de dias y aplicando operaciones acumuladas
# resample('7D')
# 7D => 7 dias de rango
# W-Sun => Cada domingo
# M => Mensual
print(df_coronavirus_time.resample('7D').sum())
print(df_coronavirus_time.resample('M').sum())
print(df_coronavirus_time.resample('M').count())

# 12h => Rango de 12 Horas
# min_count=1 => El minimo valor para sumar sera 1
# Lo que significa que se generaran horas nulas
print(df_coronavirus_time.resample('12h').sum(min_count=1))

# Permite rellenar los valores null o nan por un valor que marque crecimiento lineal
# Entre el valor proximo encontrado y el inicio (Util cuando son valores acumulados)
# .interpolate()
df_coronavirus_cum = df_coronavirus_time.interpolate()

# Agrupandp por una columna, aplicando operaciones en una columna
# Obteniendo los maximos ordenados descendentemente
print(df_coronavirus.groupby(['Country/Region'])['Confirmed'].max().sort_values(ascending=False))
print("Pivot table")
print(df_coronavirus.pivot_table(values=['Confirmed'], index=['Country/Region'], aggfunc=[np.max]))

# Tip para obtener como lista los nombres de las columnas del df
print(list(df_coronavirus))

# Agrupacion por 2 columnas
# Una de ellas usando la funcion .Grouper que permite realizar una sobreagrupacion sobre el campo seleccionado por frecuencia
# pd.Grouper(key='columna', freq='intervalor de tiempo')
df_coronavirus_time_grouper = df_coronavirus.groupby(['Country/Region',
                                                      pd.Grouper(key='ObservationDate', freq='1D')]).sum()

print(df_coronavirus_time_grouper)

# Seleccionando los valores filtrando por una columna
df_france = df_coronavirus_time_grouper.loc['France', :]
print(df_france)

df_france.plot(figsize=(10, 7), title='CODV-19 FRANCE')
plt.xlabel('Date')
plt.ylabel('People')
plt.show()

# Obteniendio los maximos, en intervalos de Meses
df_monthly = df_france.resample('M').max()
print(df_monthly)
df_monthly.plot(kind='bar')
plt.show()
