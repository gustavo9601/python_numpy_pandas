# pip install numpy

import sys
import numpy as np

"""
Tipos de datos, para Numpy
Bool	?
byte (Signed)	b
byte (unsigned)	B
integer (Signed)	i
integer (unsigned)	u
float	f
complex	c
timedelta	m
datetime	M
Objects	O
Unicode	U

"""

# dype='caracter' especificara el contenido del arreglo
a_flotante = np.array([1, 2, 3, 4], dtype='f')
print("a_flotante", a_flotante)
print("a_flotante type", a_flotante.dtype)
# cambiando el tipo de dato a todo el array
a_flotante_a_entero = a_flotante.astype(np.int8)
print("a_flotante_a_entero", a_flotante_a_entero)

# .arange(valores) crea un arreglo de datos
# (valor_inicial, valor_final, salto)
a1 = np.arange(2, 10, 2)
print("a1", a1)

# .shape(arreglo) devuelve en una tupla las filas y columnas del arreglo
forma_a1 = np.shape(a1)
print("forma_a1", forma_a1)

# la funcion .shape tambien permite reoganizar los datos, asignandole en una tupla la nueva estructura (n_filas, ncolumnas)
a1.shape = (2, 2)
print("a1.shape = (2,2)", a1)

# .zeros(cantidad)  devuelve un arreglo de una fila con solo 0, en funcion del la cantidad
# .zeros((filas, columnas))  devuelve una matriz de ceros, en funcion de la tupla pasada (filas, columans)
a_zeros = np.zeros(10)
print("a_zeros", a_zeros)

a_zeros_matriz = np.zeros((2, 3))
print("a_zeros_matriz", a_zeros_matriz)

# .ones(cantidad) mismo que zeros, solo que la rellena de unos
a_ones = np.ones(10)
print("a_ones", a_ones)
# .ones((filas, columnas)) al igual que zeros puede generar una matriz
a_ones_matriz = np.ones((2, 10))

# .full(tupla(filas, columnas), valor_repetir)
# lo mismo que .zeros pero con un valor por default
a_valores = np.full((2, 3), 10)
print("a_valores", a_valores)

# .eye(numero_filas_columnas)
# genera un cuadrado, en funcion del valor de cantidad numero filas y columnas, con un 1 en diagonal
a_eye = np.eye(5)
print("a_eye", a_eye)

# ******************************************************
# Muy utiles al generar arreglos aleatorios
# ******************************************************
# .random.random(tupla(numero_filas, numero_columnas))
# generea una matriz de numeros decimales random en funcion del numero y filas seleccionados
a_random = np.random.random((2, 10))  # .random(cantidad)
print("a_random", a_random)

# .random.randint(valor_inicial, valor_final, (cantidad_filas, cantidad_columnas))
# permite crear arreglos con valores random definidendo el rango
a_random_especific = np.random.randint(0, 25, (5, 6))
print("a_random_especific", a_random_especific)

# .linspace(valor_inicial, valor_final, cantidad_elementos)
# similar a ramdom.randint pero para ese caso no son aletorios utiliza el rango y la cantidad para seguir la secuencia generada
a_linspace = np.linspace(1, 10, 10)
print("a_linspace", a_linspace)

# arreglo.ndim
# devuelve el numero de dimensiones
print("a_random.ndim", a_random.ndim)

# arreglo.size
# devuelve el tamaño del arreglo o cantidad de posiciones
print("a_random.size", a_random.size)

# arreglo.itemsize
# devuelve el tamaño en bytes de cada una de las posiciones
print("a_random.itemsize", a_random.itemsize)

# .array(lista/tupla) parsea a array una lista o tupla
# .array([], []) si se pasan varias listas genera una matriz dependiendo la cantidad de valores en cada lista
l1 = [1, 2, 3, 4]
a_lista_to_array = np.array(l1)
print("a_lista_to_array", a_lista_to_array)

# .sort(arreglo)
# ordena el arreglo pasado por parametro
a_organizar = np.array([1, 32, 3, 2, 1, 2, 88, 900])
a_organizar = np.sort(a_organizar)
print("a_organizar", a_organizar)

# .argsort(arreglo)
# devuelve los indices con la nueva organizacion
a_indeces_organizar = np.array([10, 20, 3, 2, 1, 100, 22])
a_indeces_organizar = np.argsort(a_indeces_organizar)
print("a_indeces_organizar", a_indeces_organizar)

# np permite realizar operaciones matematicas en columnas de 2 o mas arreglos
a_valor_sum = np.array([1, 2, 3, 4])
b_valor_sum = np.array([5, 6, 7, 8])
a_sum_columna = a_valor_sum + b_valor_sum
print("a_sum_columna", a_sum_columna)

# multiplica todos los valores * 10
print("a_valor_sum * 10", a_valor_sum * 10)

# mas operaciones aplicadas a cada elemento
print("((a_valor_sum * 10) - 50) / 2", ((a_valor_sum * 10) - 50) / 2)

"""
Copia por referencia => es una asignacion temporal de una variable a otra, pero al modificar en la segunda asignacion.
modificara los valores de la primer variable
a = b

Copia por valor => en la asginacion genera una copia del valor, permitiendo que en la nueva asignacion no modifique los valores
de la primer variable
nueva_variable = arrelgo.copy()

# retorna la numero en la memoria
id(variable)   

# devuelve unas banderas propias de los arreglos
# sirve para ver el valor OWNDATA: si es True es por que una variable inicial, si es False es por que es otra variable pero por referencia
# arreglo.flags


# is permite comparar si son el mismo objeto
arreglo1 is arreglo2

"""


# Accediendo a posiciones de un arreglo
a_acceso = np.array([10, 20, 30, 40, 50, 60, 70])
print("a_acceso", a_acceso)

# accede desde la posicion 1 a la 5 de 2 en 2
print("a_acceso[1:5:2]", a_acceso[1:5:2])

# accede a las posiciones que se le pasan como argumento en una lista
lista_indices = [2, 5]
print("a_acceso[[2,5]]", a_acceso[lista_indices])

# .copy()
nueva_variable_copy = a_acceso.copy()
print("nueva_variable_copy", nueva_variable_copy)

# .random.randinit(val_inicial, val_final -1 , (n_filas, n_columnas))
matriz_1 = np.random.randint(1, 10, (5, 5))
print("matriz_1", matriz_1)

# accediendo a la misma posicion indicandola con [][] o separa por ,
print("matriz_1[1][1]", matriz_1[1][1])
print("matriz_1[1,1]", matriz_1[1, 1])

# accediendo a rangos dentro de la misma fila
# accede a las fila 1, de la columna 1 a la 4
print("matriz_1[1][1:4]", matriz_1[1][1:4])
print("matriz_1[1, 1:4]", matriz_1[1, 1:4])

# accediendo a indices a partir de una lista
print("matriz_1[1][[0,2,3]]", matriz_1[1][[0, 2, 3]])
print("matriz_1[1, [0,2,3]]", matriz_1[1, [0, 2, 3]])

# trasnforma una matriz a un arreglo de 1 sola dimension
a_arreglo1dm_from_matriz = np.ravel(matriz_1)
print("a_arreglo1dm_from_matriz", a_arreglo1dm_from_matriz)

# genera una copia del arreglo
a_copy_arreglo = a_arreglo1dm_from_matriz.flatten()
print("a_copy_arreglo", a_copy_arreglo)

# np.arange(0, 10) / /arreglo de 0 hasta 9
a_modificar = np.arange(0, 10)
print("a_modificar", a_modificar)

# modifica en las posiciones de 0:3 por valor 20
a_modificar[0:4] = 20
print("a_modificar[0:4] = 20 => ", a_modificar)

# modifica en las posiciones de especificas 4,6,7 pasando una lista com oindice
a_modificar[[4, 6, 7]] = 100
print("a_modificar[[4,6,7]] = 100 => ", a_modificar)

# modificando posiciones pasando una lista como valor
a_modificar[[4, 6, 7]] = [900, 1000, 1001]
print("a_modificar[[4,6,7]] = [900,1000,1001] => ", a_modificar)

# añadiendo un valor al arreglo
a_modificar = np.append(a_modificar, 9999)
print("np.append(a_modificar, 9999) =>", a_modificar)

# eliminado una posicion del arreglo
a_modificar = np.delete(a_modificar, 0)
print("np.delete(a_modificar, 0) =>", a_modificar)

a_3_dimensiones = np.arange(0, 30)
# cambiar la dimension
# .shape = (2,3,5) => .shape(n_matrices, n_filas_por_matriz, n_columnas_por_matriz)
a_3_dimensiones.shape = (2, 3, 5)
print("a_3_dimensiones", a_3_dimensiones)
print("a_3_dimensiones.ndim", a_3_dimensiones.ndim)

# .reshape( (n_filas, n_columnas) )
# modifica el tamaño y organizacion de una matriz generando un nuevo arreglo y no modificando el actual
print("a_3_dimensiones.reshape((3,10))", a_3_dimensiones.reshape((3, 10)))

# squeeze(matriz) // ajusta la matriz a las posiciones necesarias, eliminando vacios
a_con_squeeze = np.squeeze(a_3_dimensiones)
print("a_con_squeeze", a_con_squeeze)

# arreglo.T
# arreglo.transpose()
# permite volvar el orden de columnas hacia filas y filas hacia columnas
a_transposicion = np.arange(0, 10).reshape(2, 5)
print("a_transposicion", a_transposicion)
print("a_transposicion.T", a_transposicion.T)

"""
Metodos propios de arreglos
"""

# np.arange(start, end, step)
a_operaciones = np.arange(0, 10)
print("a_operaciones", a_operaciones)
# .sum()
# suma todos los elementos
print("a_operaciones.sum()", a_operaciones.sum())

# .min() 0 // fila | 1 // columnas
# devuelve el elemento menor
print("a_operaciones.min()", a_operaciones.min())
print("indice min a_operaciones.argmin()", a_operaciones.argmin())


# .max() 0 // fila | 1 // columnas
# devuelve el elemento mayor
print("a_operaciones.max()", a_operaciones.max())
matriz_max = np.random.randint(1, 50, (2, 10))
print(matriz_max)
print('maximo por fila', matriz_max.max(1))
print('maximo por columna', matriz_max.max(0))
# argmax al igual que max, recibe fila y columnas
print('indice del valor maximo del array', matriz_max.argmax())


# .ptp() 0 // fila | 1 // columnas
# pick to pick, devuelve la diferencia entre el valor mayor y menor
print('ptp ', a_operaciones.ptp())

# .std()
# devuelve la desviacion estandar del arreglo
print("a_operaciones.std()", a_operaciones.std())

# .mean()
# devuelve la media del arreglo
print("a_operaciones.mean()", a_operaciones.mean())

# .median() # 0 // columna | 1 // fila
# mediana del arreglo
print("np.median", np.median(a_operaciones))


"""
Ordenamiento de arreglos
"""
a_ordenar = np.random.randint(1, 101, 50)
print("a_ordenar", a_ordenar)

# .sort()
# ordena el arreglo de forma ascendete
print("a_ordenar.sort()", a_ordenar.sort())

# [::-1]
# ordena el arreglo de forma descendente
print("a_ordenar[::-1]", a_ordenar[::-1])


# percentile
print("np.percentile", np.percentile(a_ordenar, 50))

"""
Funciones para ejecutar en cada posicion del arreglo sin tener que iterarlo
"""
a_funciones = np.random.randint(0, 11, 10)
print("a_funciones", a_funciones)


def mulitplicar_x_11(val):
    return val * 11


# se debe vectorizar la funcion
funcion_multiplicar_x_11_vectorizada = np.vectorize(mulitplicar_x_11)

# una ves vectorizada se le puede pasar a la nueva variable vector el arreglo
print("funcion_multiplicar_x_11_vectorizada(a_funciones) => ", funcion_multiplicar_x_11_vectorizada(a_funciones))

"""
Valores logicos sobre arreglos, con operadores relacionales
"""

a_logicos = np.arange(0, 11)
print("a_logicos", a_logicos)

# arreglo < numero
# permite trasformar a boooleanos los valores del arreglo compadaro, y segun sea la condicion retornara True o False por cada posicion
print("a_logicos", a_logicos < 5)

# filtrar un arreglo, pasando en ves de indice una expresion booleana
# arreglo[arreglo expresion_lofica  valor]
print("a_logicos[a_logicos < 5]",
      a_logicos[a_logicos < 5])  # obtendra todos los valores del arreglo que sean menores a 5

# retornara los valores mayores a 2 y menores a 6
# Operadores de relacion
# and  =>  &
# or  =>  |

print("a_logicos[(a_logicos >2 ) & (a_logicos < 6)] => ", a_logicos[
    (a_logicos > 2) & (a_logicos < 6)])  # obtendra todos los valores del arreglo que sean menores a 5 y mayores a 2

"""
Comparacion de arreglos con expresiones logicas
"""

a_1 = np.random.randint(1, 5, 10)
a_2 = np.random.randint(1, 5, 10)
print("a_1", a_1)
print("a_2", a_2)

# devolvera un arreglo con las mismas posiciones, pero en los valores ira un booleano que representara
# el valor devuelto despues de evaluar la misma posicion en ambos arreglos
print("a_1 > a_2", a_1 > a_2)
# devolvera los valores que esten en ambos arreglos para la misma posicion
print("a_1[a_1 == a_2]", a_1[a_1 == a_2])
# devolvera los valores que esten que estan en un arreglo y en el otro no para la misma posicion
print("a_1[a_1 != a_2]", a_1[a_1 != a_2])

"""
Exportando e importando archivos de NP
"""

a_data_file = np.arange(0, 31)
print("a_data_file", a_data_file)
# exportando un archivo los datos
np.savetxt('./files/file-np.txt', a_data_file)
# importando en una variable la data de un archivo
a_upload_file = np.loadtxt('./files/file-np.txt')
print("a_upload_file", a_upload_file)

# guardando en un archivo csv una matriz, especificando el delimiador
a_data_matriz = np.random.randint(0, 101, (10, 3))
print("a_data_matriz", a_data_matriz)
np.savetxt('./files/files-np.csv', a_data_matriz, delimiter=';')

a_data_matriz_upload = np.loadtxt('./files/files-np.csv', delimiter=';')
print("a_data_matriz_upload ", a_data_matriz_upload)

# guardando la matriz en un archivo binario comprimido, con ext .npz
np.savez('./files/files-np.npz', a_data_matriz)
# obtenidno la informacion del archivo binario
a_data_matriz_upload_binary = np.load('./files/files-np.npz')
print("a_data_matriz_upload_binary",
      a_data_matriz_upload_binary['arr_0'])  # se debe acceder a la posicion ['arr_0'], al obtenerlo desde el binario

# leyendo informacion de un archivo, que no esta dado para lectura
# si en  el archivo hya comentarios los ignorara al giual que las lineas vaciasrandint
data_txt = np.genfromtxt('./files/pruebas_formato.txt', usecols=[1, 2], skip_header=1, delimiter=',', skip_footer=1)
print("data_txt", data_txt)




# np.concatenate()  | 0 // fila | 1 // columna
array_a = np.random.randint(1,10,(1,10))
array_b = np.linspace(1, 10, 10).reshape(1,10)

print("array_a.ndim", array_a.ndim)
print("array_b.ndim", array_b.ndim)
array_concat_a_b = np.concatenate((array_a, array_b), axis=0)
print("array_concat_a_b", array_concat_a_b)


# Condiciones

array_condiciones = np.linspace(1,100,100, dtype='int8')

# Imprime el array convertido a boleano lo que pase la condicion
array_mayor_50 = array_condiciones > 50
print("array_mayor_50", array_mayor_50)

# Usando un arreglo de boleanos para filtrar otro, solo retornara los true
print("array_condiciones > 50", array_condiciones[array_mayor_50])
print("array_condiciones > 90", array_condiciones[array_condiciones > 90])

# Condicion multiple
print("array_condiciones > 90 & < 95", array_condiciones[(array_condiciones > 90) & (array_condiciones < 95)])

# Modificando valores en funcion de una condicion como filtro
array_condiciones[array_condiciones < 5] = 4
print("array_condiciones modificando < 5", array_condiciones)

# Impares
print("array_condiciones pares", array_condiciones[array_condiciones % 2 == 0])
print("array_condiciones impares", array_condiciones[array_condiciones % 2 != 0])


# Producto punto
matriz_1 = np.random.randint(1,10,(5,10))
matriz_2 = np.random.randint(1,100,(5,10))
# se transpone ya que el # de columnas de M1 debe concocard con el numero de filas de M2
print(np.matmul(matriz_1, matriz_2.T))
print(np.dot(matriz_1, matriz_2.T))


# .unique()
# Deja los elementos unicos en el array, y si se pasa el conteo de counts, devuelve una tupla con los valores unicos y la cantidad de repetidos
unique, ocurrence = np.unique(array_condiciones, return_counts=True)
print("unique", unique)
print("ocurrence", ocurrence)


print(np.array([[1,2,3],[4,5,6],[7,8,9]]).ndim)