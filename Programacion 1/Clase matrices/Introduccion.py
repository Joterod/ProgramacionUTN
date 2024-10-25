""" Un array bidimensional es una estructyura de datos que contiene elementos en filas y columnas formando una tabla, se lo conoce como matrices.
A las matrices en python se las representa como listas anidadas

En las matrices el primer numero se refiere a las filas y el segundo a las columnas.
"""
# 3x2
matriz_a = [
    [1,5],
    [-3,6],
    [2,1],
]
#2x3
matriz_b = [
    [4,3,9],
    [-1,2,-5]
]
matriz_c = [
    [4,7,1],
    [-2,5,9],
    [5,4,-4]
]
#para acceder a las filas se puede indexar [] y si se indexa 2 veces [][] se esta apuntando a una columna especifica.

for fil in range(len(matriz_c)):
    for col in range(len(matriz_c[fil])):
        print(matriz_c[fil][col], end=" ")
    print("")

