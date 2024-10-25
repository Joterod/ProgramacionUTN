from random import sample, randint

"""Ejercitación Clase 8 (Arreglos Unidimensionales)"""

LISTA = ["López", "Gómez", "Fernández", "Pérez", "Martínez" ]
"""1. Escribir una función que reciba como parámetro una lista de str y cuente la cantidad de elementos con más de cinco caracteres.
Para contar los caracteres de un string también se usa la función len"""

def contar_str_largos(lista):
    contador = 0
    for i in range(len(lista)):
        if len(lista[i]) > 5:
            contador += 1
        else:
            continue
    return contador

# print(contar_str_largos(LISTA))

"""2. Escribir una función que reciba como parámetro una lista de str y retorne una nueva lista con los elementos de más de cinco caracteres.
"""
def exportar_str_largos(lista):
    nueva_lista = []
    for i in range(len(lista)):
        if len(lista[i]) > 5:
            nueva_lista.append(lista[i])
        else:
            continue
    return nueva_lista

# print(exportar_str_largos(LISTA))

"""3. Escribir una función que reciba una lista de strings y devuelva la cantidad de caracteres que tienen en promedio.
"""
def promediar_caracteres(lista):
    total_caracteres = 0

    for i in range(len(lista)):
        total_caracteres += len(lista[i])
    
    promedio = total_caracteres / len(lista)
    return promedio

# print(promediar_caracteres(LISTA))

"""4. Escribir una función que me permita ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Retornar una lista con el/los nombres de la personas con el nombre más corto (tener en cuenta más de un mínimo)
"""
def generar_lista_nombres():
    lista_nombres = [0,0,0,0,0]
    for i in range(len(lista_nombres)):
        lista_nombres[i] = input("Ingrese el nombre de la persona:\n")
    
    return lista_nombres

# print(generar_lista_nombres())

"""5. Escribir una función que reciba una lista de apellidos comunes como esta:
apellidos_comunes = ["López", "Gómez", "Fernández", "Pérez", "Martínez" ]
Ingresar 10 apellidos y guardarlos en otra lista. Contar cuantas veces se repiten los apellidos comunes.

Ejemplo
López se repite 2 veces
Gómez se repite 0 veces
Fernández se repite 1 vez
Pérez se repite 0 veces
Martínez se repite 3 veces
"""
def contar_repeticiones(lista):
    lista_comparación = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(lista_comparación)):
        lista_comparación[i] = input("Ingrese el nombre de la persona:\n")
    
    for i in range(len(lista)):
        contador = 0
        for j in range(len(lista_comparación)):
            if lista[i] == lista_comparación[j]:
                contador += 1
        print(f"{lista[i]} se repite {contador}","vez" if contador == 1 else "veces")

# contar_repeticiones(LISTA)
"""6. Escribir una función que pida una cantidad indeterminada de strings al usuario y las almacene en una lista.
"""
def almacenar_strings():
    cantidad = int(input("Cuantos strings quiere almacenar?\n"))
    lista_nombres = []
    for _ in range(cantidad):
        lista_nombres.append(input("Ingrese su string\n"))
    return lista_nombres

# print(almacenar_strings())
"""7. Escribir una función que tome una lista de letras, forme una palabra con estas y la devuelva.
"""
def formar_string(lista):
    palabra = ""
    for i in range(len(lista)):
        palabra += lista[i]
    return palabra
        
# print(formar_string(["a","b","j","p"]))
"""8. Escribir una función que tome una lista y la ordene aleatoriamente (Investigar qué función de random me permite eso) 
"""
def randomizar_lista(lista):
    nueva_lista = sample(lista, len(lista))
    return nueva_lista

# print(randomizar_lista(LISTA))
"""9.Escribir un programa que me permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de 
todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años). Utilizar listas paralelas.
(Hacer dos funciones, una para la carga de productos y otra para mostrarlos)
"""
def carga_personas ():
    lista_personas= ["","","","",""]
    lista_edades = [0,0,0,0,0]
    for i in range (5):
        lista_personas[i] = input("Ingrese el nombre de la persona\n")
        lista_edades[i] = int(input("Ingrese la edad\n"))
    return lista_personas, lista_edades

def imprimir_mayores(lista_personas, lista_edades):
    nombres_mayores = []
    for i in range(len(lista_personas)):
        if lista_edades[i] > 17:
            nombres_mayores.append(lista_personas[i])
    return nombres_mayores

# listas = carga_personas()
# print(imprimir_mayores(listas[0],listas[1]))

"""10. Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. 
Mostrar la cantidad de productos que tienen un precio mayor al primer producto ingresado.
(Hacer dos funciones, una para la carga de productos y otra para mostrarlos)
"""

def carga_productos ():
    lista_productos= ["","","","",""]
    lista_precios = [0,0,0,0,0]
    for i in range (5):
        lista_productos[i] = input("Ingrese el producto\n")
        lista_precios[i] = int(input("Ingrese el precio\n"))
    return lista_productos, lista_precios

def imprimir_mayores(lista_precios):
    contador = 0
    for i in range(len(lista_precios)):
        if lista_precios[i] > lista_precios[0]:
            contador += 1 
    return contador

# listas = carga_productos()
# print(imprimir_mayores(listas[1]))

"""11. La utn fra necesita un sistema saber la nota promedio más alta entre 5 alumnos de la Materia Programación I. 
Para eso debemos guardar.

Nombre (Ingresa usuario)
Apellido (Ingresa usuario)
Legajo (Ingresa usuario entre 10000 y 99999)
Nota primer parcial (Número aleatorio entre 1 y 10)
Nota segundo parcial (Número aleatorio entre 1 y 10)
Aparte de saber cuál fue esa nota debemos mostrar cuál fue el alumno, en caso de haber más de un alumno con la misma nota promedio mostrar a los dos.
"""
def obtener_promedio():
    lista_nombres = [0,0,0,0,0]
    lista_apellidos = [0,0,0,0,0]
    lista_legajos = [0,0,0,0,0]
    lista_primer_parcial = [0,0,0,0,0]
    lista_segundo_parcial = [0,0,0,0,0]
    lista_promedio_notas = [0,0,0,0,0]
    total_notas = 0
    for i in range(len(lista_nombres)):
        lista_nombres[i] = input("Ingrese el nombre del alumno\n")
        lista_apellidos[i] = input("Ingrese el apellido del alumno\n")
        lista_legajos[i] = int(input("Ingrese el legajo (entre 10000 y 99999)\n"))
        while not 10000 <= lista_legajos[i] <= 99999:
            lista_legajos[i] = int(input("Ingrese el legajo (entre 10000 y 99999)\n"))
        lista_primer_parcial[i] = randint(1,10)
        lista_segundo_parcial[i] = randint(1,10)
        lista_promedio_notas[i] = (lista_primer_parcial[i] + lista_segundo_parcial[i]) / 2
        total_notas += lista_promedio_notas[i]
    promedio = total_notas / len(lista_nombres)

    mejor_promedio = 0

    for i in range(len(lista_nombres)):
        if lista_promedio_notas[i] > promedio:
            mejor_promedio = lista_promedio_notas[i]
    lista_mejor_promedio_nombre = []
    
    for i in range(len(lista_nombres)):
        if lista_promedio_notas[i] == mejor_promedio:
            lista_mejor_promedio_nombre.append(f"{lista_apellidos[i]}, {lista_nombres[i]}, {mejor_promedio}")
    print(lista_promedio_notas)
    return  lista_mejor_promedio_nombre

# print(obtener_promedio())

"""12.  Se necesita saber la ganancia de un supermercado en base a la venta de 5 productos. 
Se tienen los siguientes datos: producto, precio de venta, precio de compra, cantidad de unidades vendidas. 
Se pide mostrar cada producto con sus datos por consola (Una línea por producto) y calcular la ganancia del supermercado.
"""
def calcular_ganancia ():
    lista_productos= ["","","","",""]
    lista_precios_compra = [0,0,0,0,0]
    lista_precios_venta = [0,0,0,0,0]
    lista_unidades_vendidas = [0,0,0,0,0]
    beneficio = 0
    for i in range(len(lista_productos)):
        lista_productos[i] = input("Ingrese el producto\n")
        lista_precios_compra[i] = int(input("Ingrese el precio al que se compro\n"))
        lista_precios_venta[i] = int(input("Ingrese el precio de venta\n"))
        lista_unidades_vendidas[i] = int(input("Ingrese la cantidad de ventas de este producto:"))
        beneficio += (lista_precios_venta[i] - lista_precios_compra[i]) * lista_unidades_vendidas[i]

    for i in range(len(lista_productos)):
        print(f"Producto {lista_productos[i]}: se compro a {lista_precios_compra[i]}, se vendio a {lista_precios_venta[i]} y se vendieron {lista_unidades_vendidas[i]} unidades")
    print(beneficio)
    return 0

# calcular_ganancia()