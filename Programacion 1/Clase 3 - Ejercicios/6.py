"""
6.Crear una función qué encuentre el mínimo entre tres números. Debe aceptar tres argumentos y retornar el número más chico.
"""

def elegir_minimo(primer_numero, segundo_numero, tercer_numero):
    """
    Recibe 3 números y retorna el menor de los tres
    primer_numero = int    
    segundo_numero = int
    tercer_numero = int
    """
    menor = primer_numero
    if menor > segundo_numero:
        menor = segundo_numero
        if menor > tercer_numero:
            menor = tercer_numero
    return menor


print(elegir_minimo(1,1,1))
print(elegir_minimo(3,2,1))
print(elegir_minimo(1,3,2))