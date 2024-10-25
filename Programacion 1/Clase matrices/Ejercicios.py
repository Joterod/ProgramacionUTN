def validar_tipo_matriz(matriz_a:list,matriz_b:list) -> bool:
    if type(matriz_a == list) and type(matriz_b) == list:
        retorno = True
    else:
        retorno = False
    
    return retorno

def validar_largo_matriz(matriz_a:list,matriz_b:list) -> bool:
    """Funcion que chequea el largo de las matrices"""
    
    contador_fila_a = 0
    contador_fila_b = 0
    contador_columnas_a = 0
    contador_columnas_b = 0
    
    for fil in range(len(matriz_a)):
        contador_fila_a += 1
        for col in range(len(matriz_a[fil])):
            contador_columnas_a += 1
    for fil in range(len(matriz_b)):
        contador_fila_b += 1
        for col in range(len(matriz_b[fil])):
            contador_columnas_b += 1
    if contador_fila_a == contador_fila_b:
        return contador_columnas_a == contador_columnas_b
    else:
        return False

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

MATRIZ_A = [
    [1,5],
    [-3,6],
    [2,1],
]

MATRIZ_B = [
    [3,6],
    [2,-5],
    [1, 3],
]

MATRIZ_C = [
    [4,7,1],
    [-2,5,9],
    [5,4,-4]
]

"""
1.1. Realizar una función que permita realizar la suma entre dos matrices, recibirá una matriz_a y una matriz_b y 
devuelve una matriz resultante con la suma de las mismas.
Tanto la matriz A como la matriz B deben tener la misma cantidad de filas y columnas, validar que eso ocurra 
(Podemos hacer otra función que se encargue de esto) , caso contrario retornar una lista vacía en caso de que no se cumpla.
"""



def sumar_matrices(matriz_a:list, matriz_b:list)->list:
    if validar_largo_matriz(matriz_a,matriz_b) and validar_tipo_matriz(matriz_a,matriz_b):
        matriz_sumada = inicializar_matriz(len(matriz_a),len(matriz_a[0]),0)
        for fil in range(len(matriz_a)):
            for col in range(len(matriz_a[fil])):
                matriz_sumada[fil][col] = matriz_a[fil][col] + matriz_b[fil][col]
        return matriz_sumada
    else:
        print("Las validaciones no son correctas, verifique las matrices que ingresó")
        return []

# mostrar_matriz(sumar_matrices(MATRIZ_A,MATRIZ_B))

"""
2. Realizar una función que permita realizar el producto (multiplicación) de una matriz por un escalar (número entero) , 
la función deberá recibir la matriz a la que se le quiera realizar el producto, el número entero que multiplique a está matriz, 
la función devuelve una matriz nueva con el resultado de la multiplicación.
"""
def multiplicar_matriz(matriz:list,escalar:int)->list:
    if validar_tipo_matriz(matriz,matriz):
        matriz_multiplicada = inicializar_matriz(len(matriz),len(matriz[0]),0)
        for fil in range(len(matriz)):
            for col in range(len(matriz[fil])):
                matriz_multiplicada[fil][col] = matriz[fil][col] * escalar
        return matriz_multiplicada
    else:
        print("Las validaciones no son correctas, verifique las matrices que ingresó")
        return []

# mostrar_matriz(multiplicar_matriz(MATRIZ_A,2))

"""
3. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz opuesta
"""
def obtener_matriz_opuesta(matriz:list)->list:
    if validar_tipo_matriz(matriz,matriz):
        matriz_opuesta = inicializar_matriz(len(matriz),len(matriz[0]),0)
        for fil in range(len(matriz)):
            for col in range(len(matriz[fil])):
                matriz_opuesta[fil][col] = matriz[fil][col] * -1
        return matriz_opuesta
    else:
        print("Las validaciones no son correctas, verifique las matrices que ingresó")
        return []
    
# mostrar_matriz(MATRIZ_A)
# print("-"*5)
# mostrar_matriz(obtener_matriz_opuesta(MATRIZ_A))

"""
4. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz traspuesta (Donde las columnas y las filas se intercambian)
"""

def obtener_matriz_traspuesta(matriz:list)->list:
    if validar_tipo_matriz(matriz,matriz):
        matriz_traspuesta = inicializar_matriz(len(matriz),len(matriz[0]),0)
        for fil in range(len(matriz)):
            for col in range(len(matriz[fil])):
                matriz_traspuesta[fil][col] = matriz[col][fil] 
        return matriz_traspuesta

# mostrar_matriz(MATRIZ_C)
# print("-"*5)
# mostrar_matriz(obtener_matriz_traspuesta(MATRIZ_C))

"""
5. Realizar una función que permita realizar la multiplicación entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante 
con el producto de las mismas.
Para que se pueda hacer una multiplicación entre dos matrices la cantidad de columnas de la matriz A debe ser igual a la cantidad de 
filas de la matriz B , si no se cumple devolver una lista vacía.
Además el tamaño de la matriz resultante debe ser equivalente a la cantidad de filas de la matriz A y la cantidad de columnas de la matriz B
"""

def multiplicar_matrices(matriz_a, matriz_b):
    largo_filas = len(matriz_a)
    largo_columnas = len(matriz_b[0])
    matriz_final = inicializar_matriz(largo_filas,largo_columnas,0)
    for fil in range(len(matriz_final)):
        for col in range(len(matriz_final)):
            matriz_final[fil][col] = matriz_a[fil][col] * matriz_b[col][fil]

mostrar_matriz(multiplicar_matrices(MATRIZ_A, MATRIZ_B))