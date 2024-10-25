matriz = [
    [4,7,1],
    [-2,5,9],
    [5,4,-4]
]

# Buscamos el numero ingreseado
numero = int(input("Ingrese un numero:\n"))
bandera = False
for fil in range(len(matriz)):
    for col in range(len(matriz[fil])):
        if matriz[fil][col] == numero:
            mensaje = "Se encontro"
            print(mensaje)
            bandera = True
            break
    if bandera:
        break
if not bandera:
    print("No se encontró")