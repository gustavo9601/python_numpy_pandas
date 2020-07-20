# pip install numpy

import numpy as np

# .arange(valores) crea un arreglo de datos
# (valor_inicial, valor_final, salto)
a1 = np.arange(2,10,2)
print("a1", a1)

# .shape(arreglo) devuelve en una tupla las filas y columnas del arreglo
forma_a1 = np.shape(a1)
print("forma_a1",forma_a1)

# .zeros(cantidad)  devuelve un arreglo de una fila con solo 0, en funcion del la cantidad
# .zeros((filas, columnas))  devuelve una matriz de ceros, en funcion de la tupla pasada (filas, columans)
a_zeros = np.zeros(10)
print("a_zeros", a_zeros)

a_zeros_matriz = np.zeros((2,3))
print("a_zeros_matriz", a_zeros_matriz)

# .full(tupla(filas, columnas), valor_repetir)
# lo mismo que .zeros pero con un valor por default
a_valores = np.full((2,3), 10)
print("a_valores", a_valores)

# .eye(numero_filas_columnas)
# genera un cuadrado, en funcion del valor de cantidad numero filas y columnas, con un 1 en diagonal
a_cuadrado = np.eye(5)
print("a_cuadrado", a_cuadrado)

# .random.random(tupla(numero_filas, numero_columnas))
# generea una matriz de numeros decimales random en funcion del numero y filas seleccionados
a_random = np.random.random((2,10))
print("a_random", a_random)


# .array(lista/tupla) parsea a array una lista o tupla
# .array([], []) si se pasan varias listas genera una matriz dependiendo la cantidad de valores en cada lista
l1 = [1,2,3,4]
a_lista_to_array = np.array(l1)
print("a_lista_to_array", a_lista_to_array)


# .sort(arreglo)
# ordena el arreglo pasado por parametro
a_organizar = np.array([1,32,3,2,1,2,88,900])
a_organizar = np.sort(a_organizar)
print("a_organizar", a_organizar)


# .argsort(arreglo)
# devuelve los indices con la nueva organizacion
a_indeces_organizar = np.array([10,20,3,2,1,100,22])
a_indeces_organizar = np.argsort(a_indeces_organizar)
print("a_indeces_organizar", a_indeces_organizar)


# np permite realizar operaciones matematicas en columnas de 2 o mas arreglos
a_valor_sum = np.array([1,2,3,4])
b_valor_sum = np.array([5,6,7,8])
a_sum_columna = a_valor_sum + b_valor_sum
print("a_sum_columna", a_sum_columna)

"""
Copia por referencia => es una asignacion temporal de una variable a otra, pero al modificar en la segunda asginacion.
modificara los valores de la primer variable
a = b

Copia por valor => en la asginacion genera una copia del valor, permitiendo que en la nueva asignacion no modifique los valores
de la primer variable
nueva_variable = arrelgo.copy()

"""