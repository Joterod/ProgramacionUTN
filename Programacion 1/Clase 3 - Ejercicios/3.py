""""
3.Crear una función que verifique si un número es par o no, devuelve True si es par, y False si es impar
"""

def verificar_paridad(numero):
    """
    Funcion que verifica si el numero en cuestión es divisible por 2 y retorna un booleano según sea o no
    numero: Número para verificar si es par o no (int)
    """
    return numero % 2 == 0

print(verificar_paridad(5))
print(verificar_paridad(4))