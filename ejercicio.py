import random

sueldos = [0,0,0,0,0,0,0,0,0,0]
acumulador_sueldos = 0

for i in range(len(sueldos)):
   numero = random.randint(350000, 1250000)
   acumulador_sueldos += numero
   sueldos[i] = numero

sueldo_promedio = acumulador_sueldos / len(sueldos)

superan_promedio = 0

for i in range(len(sueldos)):
    if sueldos[i] > sueldo_promedio:
        superan_promedio += 1

porcentaje = (superan_promedio / len(sueldos)) * 100


print(sueldos)
print(sueldo_promedio)
print(porcentaje)