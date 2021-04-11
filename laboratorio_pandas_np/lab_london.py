import pandas as pd
import numpy as np

print("version pandas >>", pd.__version__)

db_london = pd.read_csv('./../db/london_merged.csv')

# .shape
# Obtiene la cantidad de filas y columnas
print(".shape >>", db_london.shape)

# .dtypes
# devuelve los tipos de las columnas
print(".dtypes >>", db_london.dtypes)

# Formateando el formato a fecha
# si la columna contiene valores correctos de fechas, pandas pueden formatear sin errores
db_london['timestamp'] = pd.to_datetime(db_london['timestamp'])

# Añadiendo una columna apartir de otra
db_london['hour'] = db_london['timestamp'].dt.hour
print(db_london.describe)

# Reasignando a partir de un filtro de filas y columnas
# db_london.iloc[:, 1:]
# : // todas las filas
# 1: todas las columnas a partir de la posicion 1, es decir que omite la posicion 0
db_london = db_london.iloc[:, 1:]
print(db_london.describe)

# Aplicando funciones matematicas a una columnas de DF
db_london['wind_speed'] = np.sin(db_london['wind_speed'] ** 2) + 10
print(db_london.describe)

# Operaciones entre columnas
db_london['dif_t1_t2'] = db_london['t1'] - db_london['t2']
print(db_london.describe)

# Operacion entre columnas y relleno por default
# db_london['t1'].iloc[::2].sub(db_london['t2'], fill_value = 10)
# db_london['t1'] // seleccion de la columna t1
# .iloc[::2] // seleccion de las filas de 2 en 2
# .sub(value) // resta el valor por parametro
# db_london['t2'], fill_value = 10 // Columna y relleno por defecto de no encontrarse
"""
add()
sub() | subtract()
mul() | multiply()
div() | divide()
mod()
pow()
.dot() // producto punto
"""
db_london['dif_t1_t2_pares'] = db_london['t1'].iloc[::2].sub(db_london['t2'], fill_value=10)
print(db_london.describe)


# Aplicando funciones al DF
def func_1(x):
    y = x ** 2 + 1
    return y


# .apply(function or lamda)
# permite aplicar una funcion para la columna seleccionada
db_london['hour'] = db_london['hour'].apply(func_1)
print(db_london.describe)


def func_2(x, a=20, b=-100):
    y = x ** 2 + a * x + b
    return y


# args=(values) // se esepficia en tupla los valores a pasar a la funcion posicionalmebte
# a=100, b=-520 // se especifican los valores de la funcion por nombre de variable
db_london['hour'] = db_london['hour'].apply(func_2, a=100, b=-520)
print(db_london.describe)

# lamda x : x + 273
# Para cada valor de la columna representado en x se le pasara 273
db_london['t1'] = db_london['t1'].apply(lambda x : x + 273)
print(db_london.describe)

# Calculos por filas y columnas
# .mean() // media
# axis=0 // 0 filas || 1 columnas

print(db_london.apply(lambda x : x.mean(), axis=0))

"""
Además de apply, también se pueden usar las funciones applymap y map, dependiendo de la necesidad.

apply() se utiliza para aplicar una función a lo largo de un eje (columna o fila).
applymap() se usa para aplicar una función a todos los elementos del DataFrame
map() se usa para sustituir cada valor de una fila por otro valor.
Un ejemplo del uso de map() sería:
"""
print(db_london['wind_speed'].map('The wind speed is {}'.format))