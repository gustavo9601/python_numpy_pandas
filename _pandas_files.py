import pandas as pd
import numpy as np
import sys

# *********************************************************** #
# *********************************************************** #
# *********************************************************** #
# *********************************************************** #
# Exportar e importar a CSV

data = {
    'Nombres': ['Gus', 'Lau', 'Mar', 'Sergui', 'Migue'],
    'Edades': [24, 22, 54, 21, 10],
    'Pruebas': [1, 2, 3, 5, 10]
}
# columns = [] recibe en un arreglo, el ordenamiento y nombre de columna que queremos mostrar  // el nombre debe ser el mismo que se define en la data
df2 = pd.DataFrame(data, columns=['Nombres', 'Edades'])

# Exportar el dataframe a csv
# columns=[nombres_columnas]  // define que columnas poner en el archivo
# index=False  / le remueve los indices numericos por default
# sep='|'  // Separador del csv
df2.to_csv('files/df2.csv')

# Export el dataframe a xlsx
# sheet_name = "Name of the page" // Especificando el nombre de la hoja
# index=False  / le remueve los indices numericos por default
df2.to_excel('files/test.xlsx', index=False)

# Export el dataframe a json
df2.to_json('files/test.json')

# Export a pickle
df2.to_pickle('files/test.pkl')


# Importamos el csv generado anteriormente
# delimiter='caracter'  // caracter de separacion
# sep='|'  // Separador del csv
# names = ['title1', 'titl2']   // especifica el nombre de las columnas cambiandolo en el df
# header= n_fila  // especifica a partir de que fila empieza a leer
# usecols=['nombre_columnas']  // espefica que columnas se deben leer del archivo
# na_values=['posibles concidencias encontradas'] // reemplaza por NaN cualquier valor que cocuerde con el parametro pasado
# .read_csv('./path/file', delimiter='caracter', header=1, usecols=['col_name'], na_values=['N/A'])
df3 = pd.read_csv('files/df2.csv')

# Importamos desde un excel
pd.read_excel('files/test.xlsx')

# Importamos dede un json
#  type='series' // epepecifica si en serie o df se quiere abrir
pd.read_json('files/test.json')

# Importamos desde in pkl
pd.read_pickle('files/test.pkl')

# Permite mostrar los 5 primeros registros, o si se pasa por parametro el n rows
# .head() | .head(n_rows)
print("df3.head()", df3.head())

# Permite mostrar los 5 ultimos registros, o si se pasa por parametro el n rows
# .tail() | .tail(n_rows)
print("df3.tail()", df3.tail())

# accediendo a los datos de una columna extraida del csv
print(df3.Edades)


# modificando los valores de una columna extradia con apply, mulitplicando por 2 la edad de cada fila
df3.Edades = df3.apply(lambda row: row['Edades'] * 2, axis=1)
print(df3)

####
# Ordenamiento de DF

#Ordenara por indices o filas
#.sort_index() # ascending=False  lo ordena de forma descendente
print("df3.sort_index(ascending=False)", df3.sort_index(ascending=False))

# Ordenar por columna
# .sort_values('nombre_columna') # ascending=False  lo ordena de forma descendente
print(df3.sort_values('Edades'))


####
#  Modificacion de un DF
df_modificacion = pd.DataFrame(np.arange(16).reshape(4,4), columns=list('ABCD'), index=list('abcd'))
print(df_modificacion)

# primero se ingresa por columna y luego a la fila df_modificacion.COLUMNA.FILA
print("df_modificacion.A.b", df_modificacion.A.b)
print("df_modificacion['A']['b']", df_modificacion['A']['b'])
# a la posicion de l matriz le seteamos un valor
df_modificacion['A']['b'] = 900
print(df_modificacion)
# a toda una columna le seteamos os valores
df_modificacion.A = 1000,800,600,200
print(df_modificacion)
# eliminar una columna o una fila en funcion del axis
# .drop('nombre_columna', axis=1|0)  1=columnas 0=filas
df_modificacion = df_modificacion.drop('D', axis=1)
print(df_modificacion)
#  insertando una columna al DF
# .insert(posicion,'nombre_columna', [lista_valores])
df_modificacion.insert(1,'Z', [999,998,997,996])
print(df_modificacion)