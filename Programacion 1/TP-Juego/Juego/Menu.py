from Funciones import *

def ejecutar_menu():
    cantidad_victorias_jugador = 0
    cantidad_victorias_maquina = 0
    puntaje_maximo_adivina_numero = 0
    puntaje_maximo_mayor_menor = 0
    puntaje_final_adivina_numero = 0
    puntaje_final_mayor_menor = 0
    victorias_jugador_penales = 0
    victorias_computadora_penales = 0
    
    while(True):
        print(f"SALA DE JUEGOS\n1.Jugar al Piedra Papel o Tijera\n2.Jugar al Adivina el Número\n3.Jugar al Mayor/Menor\n4.Penales\n5.Mostrar Rankings\n5.Salir")
        
        opcion = pedir_numero("Su opcion: ",f"Opcion invalida ingrese números entre 1-5\nSu opcion:",1,5)
        
        if opcion == 1:
            ganador = jugar_piedra_papel_tijera()
            if ganador == "El jugador ha ganado la partida":
                cantidad_victorias_jugador += 1
            else:
                cantidad_victorias_maquina += 1
            print(ganador)
        elif opcion == 2:
            puntaje_final_adivina_numero = jugar_adivina_numero()
        elif opcion == 3:
            puntaje_final_mayor_menor = jugar_mayor_menor()
        elif opcion == 4:
            ganador_penales = jugar_penales()
            if ganador_penales == "El jugador ganó por penales":
                victorias_jugador_penales += 1
            else:
                victorias_computadora_penales += 1
        elif opcion == 5:
            puntaje_maximo_adivina_numero = calcular_maximo(puntaje_maximo_adivina_numero,puntaje_final_adivina_numero)
            puntaje_maximo_mayor_menor = calcular_maximo(puntaje_maximo_mayor_menor, puntaje_final_mayor_menor)
            cantidad_partidas = cantidad_victorias_jugador + cantidad_victorias_maquina
            porcentaje_ppt = calcular_porcentaje(cantidad_victorias_jugador, cantidad_partidas)
            porcentaje_penales = calcular_porcentaje(victorias_jugador_penales, victorias_computadora_penales)

            print("Rankings")
            print(f"Adivinar el numero: {puntaje_maximo_adivina_numero}\nPiedra, papel o tijera: Se gano el %{porcentaje_ppt}\nMayor o menor: {puntaje_maximo_mayor_menor}\nPenales: {porcentaje_penales}")
        elif opcion == 6:
            print("Saliendo...")
            break
        limpiar_consola()
    
ejecutar_menu()
