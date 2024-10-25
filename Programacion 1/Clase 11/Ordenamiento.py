lista = [5,3,1,9,7]

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i] < lista[j]:
            numero_izq = lista[i]
            lista[i] = lista[j]
            lista[j] = numero_izq
print(lista)