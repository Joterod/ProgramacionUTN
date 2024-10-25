"""
2.Crear una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.
"""

def calcular_area_rectangulo(base, altura):
    """ 
    Función que calcula el área de un rectángulo
    base = Base del rectángulo, en CM (int)
    altura = Altura del rectángulo, en CM (int)
    """
    area = base * altura
    return area

print(calcular_area_rectangulo(4,2))