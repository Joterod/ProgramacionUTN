numero = int(input("Ingrese un numero: "))
primo = True

while numero > 2:
    numero = int(input("Ingrese un numero mayor a 1"))
for posible_divisor in range(2, numero):
    if numero % posible_divisor == 0:
        primo = False
        break

if primo:
    print("El numero es primo.")
else:
    print("El numero no es primo.")    