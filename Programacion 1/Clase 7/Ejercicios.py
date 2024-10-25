from random import randint

lista = [randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
lista_neg = [randint(-1000,1000),randint(-1000,1000),randint(-1000,1000),randint(-1000,1000),randint(-1000,1000)]

"""
1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
"""

def promedio_lista(lista):
    largo_lista = len(lista)
    total = 0
    for i in range(largo_lista):
        total += lista[i]

    promedio = total / largo_lista
    return promedio

#print(f"{lista}\n{promedio_lista(lista)}")

"""
2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos. En caso de no haber números positivos validar división por cero
"""

def promedio_con_neg(lista):
    largo_lista = len(lista)
    total = 0
    contador_positivos = 0
    for i in range(largo_lista):
        if lista[i] > 0:
            total += lista[i]
            contador_positivos += 1
        else:
            continue
    

    if contador_positivos == 0:
        promedio = 0
    else :
        promedio = total / contador_positivos
    
    return promedio

#print(f"{lista_neg}\n{promedio_con_neg(lista_neg)}")

"""
3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro
"""
def obtener_producto(lista):
    largo_lista = len(lista)
    total = 1
    for i in range(largo_lista):
        total = total * lista[i]
    return total

#print(f"{lista}\n{obtener_producto(lista)}")

"""
4.Escribir una función que reciba como parámetros una lista de enteros 
y retorne el índice del valor máximo encontrado (retornar un sólo índice,
en caso de que haya más de un máximo el primero)
"""
def obtener_indice_maximo(lista):
    largo_lista = len(lista)
    mayor = 0
    indice_mayor = 0
    for i in range(largo_lista):
        if lista[i] > mayor:
            mayor = lista[i]
            indice_mayor = i
        else: 
            continue
    return indice_mayor

#print(f"{lista}\n{obtener_indice_maximo(lista)}")

"""
5. Escribir una función que reciba como parámetros una lista de enteros y muestre el 
índice del valor máximo encontrado (no se tienen en cuenta si hay más de un máximo) Reutilizar la función anterior.
"""
def obtener_valor_maximo(lista):
    indice = obtener_indice_maximo(lista)
    return indice, lista[indice]

#print(f"{lista}\n{obtener_valor_maximo(lista)}")

"""
6. Escribir una función que reciba como parámetros una lista de enteros y 
retorne todos los índices del valor máximo encontrado (Puede haber más de uno)
"""

def obtener_indices_maximos(lista):
    largo_lista = len(lista)
    mayor = None
    indices_mayores = []
    for i in range(largo_lista):
        if mayor == None:
            mayor = lista[i]
        if lista[i] > mayor:
            mayor = lista[i]
            indices_mayores = [i]
        elif lista[i] == mayor:
            indices_mayores.append(i)
    return indices_mayores

#print(f"{lista}\n{obtener_indices_maximos(lista)}")

"""
7. Escribir una función que reciba como parámetros una lista de enteros y 
muestre la posición del valor máximo encontrado. Reutilizar la función anterior.
"""
def obtener_valores_maximos(lista):
    indices = obtener_indices_maximos(lista)
    return indices, lista[indices[0]]

#print(f"{lista}\n{obtener_valores_maximos(lista)}")

"""
Definir y cargar una lista con 10 sueldos enteros aleatorios (utilizar random), entre ARS 350.000 y ARS 1.250.000. 
Calcular el porcentaje de personas que superan el salario promedio de estos mismos.
"""
sueldos = [0,0,0,0,0,0,0,0,0,0]

def obtener_porcentaje_sueldos():
    total = 0
    sueldos_mayores = 0
    for i in range(len(sueldos)):
        sueldos[i] = randint(350000,1250000)

    for i in range(len(sueldos)):
        total += sueldos[i]
    promedio = total / len(sueldos)

    for i in range(len(sueldos)):
        if sueldos[i] > promedio:
            sueldos_mayores += 1

    porcentaje = (sueldos_mayores/len(sueldos)) * 100
    return porcentaje

#print(f"{obtener_porcentaje_sueldos()}")
