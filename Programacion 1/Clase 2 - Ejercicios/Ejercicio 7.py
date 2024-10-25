numero = int(input("Ingrese un numero: "))

for i in range(2, numero):
    primo = True
    for posible_divisor in range(2, i):
        if i % posible_divisor == 0:
            primo = False
            break
    if primo:
        print(i)