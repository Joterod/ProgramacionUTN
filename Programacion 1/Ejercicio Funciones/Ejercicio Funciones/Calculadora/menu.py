import os
from funciones import *

def menu():
    primer_numero_flag = False
    segundo_numero_flag = False
    operaciones_flag = False
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        opcion = int(input("Su opcion: "))
        if opcion == 1:
            primer_numero_flag = True
            primer_numero = int(input("Ingrese el Primer Operando:\n"))
        elif opcion == 2:
            segundo_numero_flag = True 
            segundo_numero = int(input("Ingrese el Segundo Operando:\n"))
        elif opcion == 3:
            operaciones_flag = True
            if primer_numero_flag and segundo_numero_flag:
                suma_informe = suma(primer_numero,segundo_numero)
                resta_informe = resta(primer_numero,segundo_numero)
                division_informe = division(primer_numero,segundo_numero)
                multiplicacion_informe = multiplicacion(primer_numero,segundo_numero)
                potencia_informe = potencia(primer_numero,segundo_numero)
                resto_informe = resto(primer_numero,segundo_numero)
                factorial_informe_a = factorial(primer_numero)
                factorial_informe_b = factorial(segundo_numero)
                informes = [suma_informe,resta_informe,division_informe, multiplicacion_informe,potencia_informe,resto_informe,factorial_informe_a, factorial_informe_b]
            else:
                print("Se debe ingresar ambos operandos para solicitar las operaciones.")
            print("Calculo todas las operaciones")
        elif opcion == 4:
            if not operaciones_flag:
                print("No se puede ingresar a los informes sin hacer las operaciones antes")
            else:
                for informe in informes:
                    print(informe)
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        input("Pulse boton para continuar...")
        os.system('clear')

    
    
menu()
