"""
4.Crear una función que verifique si un primo o no, devuelve True si es primo, False si no lo es
"""

def verificar_primo(numero):
    """
    Verifica si el numero ingresado es primo o no, y retorna un booleano dependiendo el caso.
    numero = Número que se quiere saber si es primo o no. (int)
    """
    primo = True

    if numero < 2:
        primo = False
    else:
        for posible_divisor in range(2, numero):
            if numero % posible_divisor == 0:
                primo = False
                break
    return primo

for i in range(100):
    print(i , verificar_primo(i))