contador = 0
suma = 0

while contador <5:
    numero = int(input(f"Ingrese un número:\n"))
    suma += numero
    contador +=1

promedio = suma / 5
print(suma, promedio)
