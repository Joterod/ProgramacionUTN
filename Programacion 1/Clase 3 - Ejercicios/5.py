"""
5.Crear una función qué encuentre el máximo entre tres números. 
Debe aceptar tres argumentos y retornar el número más grande.
"""

def elegir_maximo(primer_numero, segundo_numero, tercer_numero):
    """
    Recibe 3 números y retorna el mayor de los tres
    primer_numero = int    
    segundo_numero = int
    tercer_numero = int
    """
    mayor = primer_numero
    if mayor < segundo_numero:
        mayor = segundo_numero
        if mayor < tercer_numero:
            mayor = tercer_numero
    return mayor

print(elegir_maximo(1,1,1))
print(elegir_maximo(3,2,1))
print(elegir_maximo(1,3,2))