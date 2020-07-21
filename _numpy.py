# pip install numpy

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


# .arange(valores) crea un arreglo de datos
# (valor_inicial, valor_final, salto)
a1 = np.arange(2, 10, 2)
print("a1", a1)

# .shape(arreglo) devuelve en una tupla las filas y columnas del arreglo
forma_a1 = np.shape(a1)
print("forma_a1", forma_a1)

# .zeros(cantidad)  devuelve un arreglo de una fila con solo 0, en funcion del la cantidad
# .zeros((filas, columnas))  devuelve una matriz de ceros, en funcion de la tupla pasada (filas, columans)
a_zeros = np.zeros(10)
print("a_zeros", a_zeros)

a_zeros_matriz = np.zeros((2, 3))
print("a_zeros_matriz", a_zeros_matriz)

# .ones(cantidad) mismo que zeros, solo que la rellena de unos
a_ones = np.ones(10)
print("a_ones", a_ones)

# .full(tupla(filas, columnas), valor_repetir)
# lo mismo que .zeros pero con un valor por default
a_valores = np.full((2, 3), 10)
print("a_valores", a_valores)

# .eye(numero_filas_columnas)
# genera un cuadrado, en funcion del valor de cantidad numero filas y columnas, con un 1 en diagonal
a_cuadrado = np.eye(5)
print("a_cuadrado", a_cuadrado)

# ******************************************************
# Muy utiles al generar arreglos aleatorios
# ******************************************************
# .random.random(tupla(numero_filas, numero_columnas))
# generea una matriz de numeros decimales random en funcion del numero y filas seleccionados
a_random = np.random.random((2, 10))  # .random(cantidad)
print("a_random", a_random)

# .random,randint(valor_inicial, valor_final, (cantidad_filas, cantidad_columnas))
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
Copia por referencia => es una asignacion temporal de una variable a otra, pero al modificar en la segunda asginacion.
modificara los valores de la primer variable
a = b

Copia por valor => en la asginacion genera una copia del valor, permitiendo que en la nueva asignacion no modifique los valores
de la primer variable
nueva_variable = arrelgo.copy()

"""

# Accediendo a posiciones de un arreglo
a_acceso = np.array([10, 20, 30, 40, 50, 60, 70])
print("a_acceso", a_acceso)

# accede desde la posicion 1 a la 5 de 2 en 2
print("a_acceso[1:5:2]", a_acceso[1:5:2])

# accede a las posiciones que se le pasan como argumento en una lista
lista_indices = [2, 5]
print("a_acceso[[2,5]]", a_acceso[lista_indices])



matriz_1 = np.random.randint(1,10,(5,5))
print("matriz_1", matriz_1)
# accediendo a la misma posicion indicandola con [][] o separa por ,
print("matriz_1[1][1]", matriz_1[1][1])
print("matriz_1[1,1]", matriz_1[1,1])

# accediendo a rangos dentro de la misma fila
# accede a las fila 1, de la columna 1 a la 4
print("matriz_1[1][1:4]", matriz_1[1][1:4])
print("matriz_1[1, 1:4]", matriz_1[1, 1:4])

# accediendo a indices a partir de una lista
print("matriz_1[1][[0,2,3]]", matriz_1[1][[0,2,3]])
print("matriz_1[1, [0,2,3]]", matriz_1[1, [0,2,3]])



# trasnforma una matriz a un arreglo de 1 sola dimension
a_arreglo1dm_from_matriz = np.ravel(matriz_1)
print("a_arreglo1dm_from_matriz", a_arreglo1dm_from_matriz)

# genera una copia del arreglo
a_copy_arreglo = a_arreglo1dm_from_matriz.flatten()
print("a_copy_arreglo", a_copy_arreglo)