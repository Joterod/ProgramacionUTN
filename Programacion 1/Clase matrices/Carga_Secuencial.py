"""Carga secuencial de matriz"""

def inicializar_matriz(filas:int, columnas:int, valor_inicial:any) -> list:
    matriz = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz)->None:
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(matriz[fil][col], end=" ")
        print("")
    return None

matriz = inicializar_matriz(3,3,0)

mostrar_matriz(matriz)
for fil in range(len(matriz)):
    for col in range(len(matriz[fil])):
        numero = int(input(f"Ingrese un numero (fila:{fil}, columna:{col})"))
        matriz[fil][col] = numero
        mostrar_matriz(matriz)