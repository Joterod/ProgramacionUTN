"""Carga aleatoria de matriz"""

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
""" SE TIENE QUE ELEGIR DONDE GUARDAR EL DATO"""
matriz = inicializar_matriz(3,3,0)

print("ANTES DE LA CARGA")
mostrar_matriz(matriz)

seguir = "S"

while seguir == "S":
    fila = int(input("Ingrese el indice de la fila:\n"))
    while not 0 <= fila <= len(matriz):
        fila = int(input("Ingrese el indice de la fila:\n"))
    columna = int(input("Ingrese el indice de la columna\n"))
    while not 0 <= columna <= len(matriz[fila]):
        columna = int(input("Ingrese el indice de la columna\n"))
    numero = int(input("Ingrese el numero:\n"))
    
    matriz[fila][columna] = numero
    
    seguir = input("Desea seguir? ingrese S/N")


print("Despues DE LA CARGA")
mostrar_matriz(matriz)