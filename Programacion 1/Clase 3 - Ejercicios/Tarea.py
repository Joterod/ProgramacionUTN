"""
TAREA. 

Realizar una función que me permita sumar dos números de las cuatro maneras siguientes.

Una función sumar1 que reciba dos números y retorne el resultado
Una función sumar2 que reciba dos números y no retorne nada (o sea que la función se encargue de mostrar el resultado)
Una función sumar3 que no reciba nada y se encargue de pedir dos números y retornar el resultado
Una función sumar4 que no reciba nada y no retorne nada, por ende se va encargar de pedir los numeros y de mostrar el resultado.
"""

def sumar_uno(primer_numero, segundo_numero):
    """
    Recibe dos números y retorne el resultado
    primer_numero = int
    segundo_numero = int
    """
    return primer_numero + segundo_numero

def sumar_dos(primer_numero, segundo_numero):
    print(primer_numero + segundo_numero)
    
def sumar_tres():
    primer_numero = int(input("Ingrese el primer número"))
    segundo_numero = int(input("Ingrese el segundo número"))
    return primer_numero + segundo_numero

def sumar_cuatro():
    primer_numero = int(input("Ingrese el primer número"))
    segundo_numero = int(input("Ingrese el segundo número"))
    print(primer_numero + segundo_numero)