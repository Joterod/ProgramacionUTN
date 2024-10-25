"""
1.Crear una función que reciba dos números (acumulador y contador) y calcule el promedio, 
en caso de que haya división por cero imprimir un mensaje de error y retornar 0.
"""

def calcular_promedio(acumulador, contador):
    """
    Calcula el promedio dividiendo la suma de los objetos por la cantidad de objetos.
    acumulador: Suma de todos los numeros (int)
    contador: Cantidad de numeros (int)
    """
    if contador == 0:
        print("ERROR no hay objetos, no hay nada para promediar")
        return 0
    else:
        promedio = acumulador / contador
        return promedio
    
    
print(calcular_promedio(53,0))