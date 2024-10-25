"""
1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales (numero:int) -> int:

5 + 4 + 3 + 2 + 1 = 15

"""

def sumar_naturales(numero:int) -> int:
    if numero > 1:
        retorno = sumar_naturales(numero-1)
        resultado = numero + retorno
    else:
        resultado = 1
    return resultado

"""
2. Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia (base:int , exponente:int) -> int:

"""
def calcular_potencia (base:int , exponente:int) -> int:
    if exponente > 1:
        retorno = calcular_potencia(base, exponente - 1)
        resultado = base * retorno
    else:
        resultado = base
    
    return resultado


"""
3. Realizar una función para calcular el número de Fibonacci (investigar que es) de un número ingresado por consola. La función deberá seguir el siguiente prototipo:
	def calcular_fibonacci (numero:int) -> int:
La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:
"""
def calcular_fibonacci (numero:int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
    
