import pandas as pd
import numpy as np

# Set format display values in PD
# Se especifica que el maximo de decimales
pd.options.display.float_format = '{:,.2f}'.format
np.set_printoptions(precision=2)

# np.random.rand(filas,columnas)
# Genera numeros aletarios entre 0 y 1
x1 = np.random.rand(2, 5) * 100
print(x1)

x2 = np.random.rand(2, 5) * -100
print(x2)

# np.concatenate([matriz1, matriz2], axis=0)
# permite concatenar multiples matrices
# axis = 0 filas | 1 columnas
x_concatenate = np.concatenate([x1, x2], axis=0)
print(x_concatenate)

serie1 = pd.Series(x1[0], index=['a', 'b', 'c', 'd', 'e'])
print(serie1)

serie2 = pd.Series(x2[0], index=['c', 'd', 'e', 'f', 'g'])
print(serie2)

# pd.concat([serie1, serie2], axis=0)
# permite concatenar series
# axis=0 filas | 1 columnas
series_concat = pd.concat([serie1, serie2])
print(series_concat)

dataframe_1 = pd.DataFrame(np.random.rand(3, 2) * 10, columns=['a', 'b'])
print(dataframe_1)

dataframe_2 = pd.DataFrame(np.random.rand(3, 2) * -10, columns=['a', 'b'], index=[2, 3, 4])
print(dataframe_2)

# pd.concat([dataframe_1, dataframe_2], axis=0)
# concatena
# axis=0 filas | 1 colomunas
dataframes_concat = pd.concat([dataframe_1, dataframe_2], axis=0)
print(dataframes_concat)

# Otra forma de concatenar dataframe
other_way_concat = dataframe_1.append(dataframe_2)
print(other_way_concat)

# Trasnponiendo un DF
print(other_way_concat.T)

# ////////////////////////////////
# Merge

df_left = pd.DataFrame(
    {'X': ['x0', 'x1', 'x2', 'x3'],
     'W': ['w0', 'w1', 'w2', 'w3'],
     'Y': ['y0', 'y1', 'y2', 'y3']},
    index=[0, 1, 2, 3])

df_right = pd.DataFrame(
    {'Z': ['z2', 'z3', 'z4', 'z5'],
     'A': ['a2', 'a3', 'a4', 'a5'],
     'Y': ['y2', 'y3', 'y4', 'y5']},
    index=[2, 3, 4, 5])

# .merge(pd1, pd2)
# hace el match por el indice que tengan en comun
print(pd.merge(df_left, df_right))

# Especificando que tipo de union se requiere y por que llave indice se debe hacer el cruce
print(pd.merge(df_left, df_right, how = 'inner', on = 'Y'))