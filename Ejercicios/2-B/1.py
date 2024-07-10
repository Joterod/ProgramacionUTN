numero = 2
total = 0

while numero <10:
    total += numero
    numero +=2

## otra alternativa

numero = 0
total = 0

while numero <10:
    if numero % 2 == 0:
        total += numero
        print(numero)
    numero +=1
print(total)