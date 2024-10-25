import random
"""
Imaginemos que nos piden un sistema en el que tenemos que almacenar productos

Identificador Unico entre 11111 y 99999 random
NOmbre
Precio
Cantidad stock


1. Ingresar 3 productos
2. Mostrar todos los productos
3. Buscar un producto por codigo unico
4. Salir del sistema
"""
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


I_ID = 0
I_NOMBRE = 1
I_PRECIO = 2
I_STOCK = 3

# 1. Ingresar_tres_productos.

matriz_productos = inicializar_matriz(3,4,0)

#Hacer la carga
# mostrar_matriz(matriz_productos)

# for fil in range(len(matriz_productos)):
#     id = random.randint(11111,99999)
#     nombre = input("Ingrese el nombre del producto\n")
#     precio = float(input("Ingrese el precio\n"))
#     stock = int(input("Ingrese el stock disponible\n"))
#     # ACA PUEDEN IR VALIDACIONES

#     matriz_productos[fil][I_ID] = id
#     matriz_productos[fil][I_NOMBRE] = nombre
#     matriz_productos[fil][I_PRECIO] = precio
#     matriz_productos[fil][I_STOCK] = stock

MATRIZ_PRUEBA =[
    [28370, "Laptop Dell XPS", 73.45, 24],
    [49250, "Smartphone Samsung Galaxy", 28.13, 35],
    [16730, "Auriculares Bose QuietComfort", 59.92, 12],
    [80510, "Cámara Canon EOS", 15.49, 42],
    [39640, "Smartwatch Apple Watch", 48.76, 20],
    [57320, "Tablet iPad Pro", 67.34, 30],
    [68920, "Monitor LG Ultrawide", 89.23, 8],
    [91430, "Teclado Mecánico Razer", 55.14, 15],
    [27180, "Mouse Inalámbrico Logitech", 22.78, 40],
    [10580, "Impresora HP LaserJet", 10.89, 50]
]

#2. Mostrar todos los productos

print("\nMUESTRO TODOS LOS PRODUCTOS\n")

for fil in range(len(MATRIZ_PRUEBA)):
    print(f"ID: {MATRIZ_PRUEBA[fil][I_ID]}")
    print(f"Producto: {MATRIZ_PRUEBA[fil][I_NOMBRE]}")
    print(f"Precio: {MATRIZ_PRUEBA[fil][I_PRECIO]}")
    print(f"Stock: {MATRIZ_PRUEBA[fil][I_STOCK]}\n")

#3. Buscar un producto
    def buscar_producto():
        busqueda = int(input("Ingrese el id que quiere buscar:\n"))
        busqueda_flag = 0
        for fil in range(len(MATRIZ_PRUEBA)):
            if MATRIZ_PRUEBA[fil][I_ID] == busqueda:
                busqueda_flag = 1
                mensaje = "Se encontro lo buscado\nID: {MATRIZ_PRUEBA[fil][I_ID]}\nProducto: {MATRIZ_PRUEBA[fil][I_NOMBRE]\nPrecio: {MATRIZ_PRUEBA[fil][I_PRECIO]}\nStock: {MATRIZ_PRUEBA[fil][I_STOCK]}\n"
                break
            else:
                mensaje ="No se encontro lo buscado\n"
        return mensaje