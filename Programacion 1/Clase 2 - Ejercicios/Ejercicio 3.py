"""
3.Ingresar dos números mostrar desde el primer número hasta el segundo que 
ingresaron de manera ascendente, en caso de que el primer número sea mayor al segundo 
mostrarlos en orden descendente, si los números son iguales, mostrar sólo ese número.
Por ejemplo: Si ingresaron 5 como primer número y 7 como segundo mostrar (5-6-7), 
si el primer número que ingresaron es 7 y el segundo un 5 mostrar (7-6-5)
"""
primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))
modificador = 1

if primer_numero > segundo_numero:
    modificador = -1
    
for numero in range(primer_numero, segundo_numero + modificador, modificador):
    print(numero)