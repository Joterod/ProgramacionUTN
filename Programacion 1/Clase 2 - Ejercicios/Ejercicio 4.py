suma = 0
contador = 0

for _ in range(5):
    numero = int(input("Ingrese un numero (ponga cero para salir): "))
    if numero == 0:
        break
    else:
        suma += numero
        contador += 1 


if contador != 0:
    promedio = suma / contador
    print(f"La suma de los números ingresados es {suma}")
    print(f"El promedio de los números es {promedio}")