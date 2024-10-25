from random import randint
import os

#Constantes -> para fecilitar el uso de eso números.

ELEMENTOS = {1:"PIEDRA", 2:"PAPEL", 3:"TIJERA"}

MAYOR = 1
MENOR = 2

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('clear')

#PEDIR DATOS
def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    print(f"{mensaje}")
    numero = input(f"Ingrese un numero entre {minimo} y {maximo}\n")
    while not numero.isnumeric():
        numero = input(f"Ingrese un numero entre {minimo} y {maximo}\n")
    numero = int(numero)
    while not minimo <= numero <= maximo and numero == '':
        print(f"{mensaje_error}{numero}")
        numero = int(input(f"Ingrese un numero entre {minimo} y {maximo}\n"))
    return numero

#RANKINGS
def calcular_maximo(numero_uno:int,numero_dos:int) -> int:
    if numero_uno > numero_dos:
        retorno = numero_uno
    else :
        retorno = numero_dos
    return retorno

def calcular_porcentaje(cantidad_victorias:int,cantidad_derrotas:int)->float:
    cantidad_partidas = cantidad_derrotas + cantidad_victorias
    if cantidad_partidas != 0:
        retorno = (cantidad_victorias / cantidad_partidas) * 100
    else:
        retorno = 0.0
    return retorno

#JUEGOS EN GENERAL
def generar_respuesta_maquina(minimo:int,maximo:int) -> int:
    return randint(minimo, maximo)

#PIEDRA PAPEL O TIJERA
def verificar_ganador_ronda(respuesta_jugador:int,respuesta_maquina:int) -> str:
    if respuesta_maquina == respuesta_jugador:
        resultado = "Empate"
    elif respuesta_jugador == 'PIEDRA' and respuesta_maquina == 'TIJERA':
        resultado = "Victoria"
    elif respuesta_jugador == "PAPEL" and respuesta_maquina == 'PIEDRA':
        resultado = "Victoria"
    elif respuesta_jugador == 'TIJERA' and respuesta_maquina == 'PAPEL':
        resultado = "Victoria"
    else:
        resultado = "Derrota"
    return resultado

def verificar_ganador_partida(aciertos_jugador:int,aciertos_maquina:int) -> str:
    if aciertos_jugador > aciertos_maquina:
        ganador_partida = "El jugador ha ganado la partida"
    elif aciertos_maquina > aciertos_jugador:
        ganador_partida = "La computadora ganó la partida"
    else:
        ganador_partida = "Es un empate"
    return ganador_partida


def verificar_estado_partida(aciertos_jugador:int,aciertos_maquina:int,ronda_actual:int, maximo_rondas) -> bool:
    diferencia = abs(aciertos_jugador - aciertos_maquina)
    rondas_restantes = maximo_rondas - ronda_actual
    if ronda_actual < maximo_rondas:
        
        retorno = diferencia <= rondas_restantes
    else:
        retorno = aciertos_jugador == aciertos_maquina
    return retorno

def obtener_elemento(respuesta:int) -> str:
    return ELEMENTOS[respuesta]

def jugar_piedra_papel_tijera() -> str:
    aciertos_jugador = 0
    aciertos_maquina = 0
    contador_rondas = 0
    
    print("Bienvenido a la partida de Piedra Papel o Tijera")

    while verificar_estado_partida(aciertos_jugador,aciertos_maquina,contador_rondas,3):
        contador_rondas +=1
        print(f"Ronda: {contador_rondas}")
        elemento_jugador_int = pedir_numero(f"Elegí tu elemento:\n1. Piedra\n2. Papel\n3. Tijera\n",f"Error, elegí un numero entre 1 y 3:\n",1,3)
        elemento_jugador = obtener_elemento(elemento_jugador_int)
        elemento_computadora = obtener_elemento(randint(1,3))
        resultado_ronda = verificar_ganador_ronda(elemento_jugador,elemento_computadora)
        if resultado_ronda == "Victoria":
            aciertos_jugador += 1
        elif resultado_ronda == "Derrota":
            aciertos_maquina += 1
        else:
            pass
        print(f"Elegiste {elemento_jugador}, la computadora eligió {elemento_computadora}")
        print(f"{resultado_ronda}!!")
        #NO BORRAR
        limpiar_consola()
        
    ganador = verificar_ganador_partida(aciertos_jugador,aciertos_maquina)
    return ganador
        

#ADIVINA EL NUMERO

def mostrar_mensaje_final(puntaje_final:int)->None:
    if puntaje_final == 0:
        mensaje_final = "Se ve que no eres bueno adivinando, más suerte la próxima"
    elif 1 <= puntaje_final <= 3:
        mensaje_final = "Buen trabajo adivinando"
    elif 4 <= puntaje_final <= 5:
        mensaje_final = "Excelente eres muy bueno adivinando"
    else:
        mensaje_final = "WOW, Usted es psiquico"
    print(mensaje_final)

def jugar_adivina_numero() -> int:
    contador_intentos = 3
    puntaje_final = 0
    
    while(contador_intentos != 0):
        #Pista debo reutilizar funciones anteriores que use en el de piedra papel tijera no hacer todo de cero.
        numero_jugador = pedir_numero("Su opcion: ",f"Opcion invalida ingrese números entre 1-2\nSu opcion:",1,9)
        numero_computadora = generar_respuesta_maquina(1,9)
        print(f"El numero es {numero_computadora}")
        
        if numero_jugador == numero_computadora:
            puntaje_final += 1
        else:
            contador_intentos -= 1
        print(f"Intentos restantes: {contador_intentos}")
        #NO BORRAR
        limpiar_consola()
    mostrar_mensaje_final(puntaje_final)
    return puntaje_final


#MAYOR MENOR

def verificar_cartas(carta:int, carta_posterior:int,eleccion_jugador:int) -> str:    
    if carta == carta_posterior:
        mensaje = f"Salio la misma carta, se baraja de nuevo\n"
    elif carta < carta_posterior and eleccion_jugador == 1:
        mensaje = f"La segunda carta es mayor, Bien hecho\n"
    elif carta > carta_posterior and eleccion_jugador == 2:
        mensaje = f"La segunda carta es menor, Bien hecho\n"
    else:
        mensaje = f"Perdiste el juego"
        
    return mensaje
        
def jugar_mayor_menor():
    puntuaje_final = 0 
    while(True):
        carta = generar_respuesta_maquina(1,12)
        print(f"La primera carta es {carta}")
        eleccion_jugador = pedir_numero(f"Elija 1 para Mayor o 2 para menor:\n","Error, elija 1 o 2",1 ,2 )
        carta_posterior = generar_respuesta_maquina(1,12)
        print(f"La segunda carta es {carta_posterior}")
        mensaje = verificar_cartas(carta,carta_posterior, eleccion_jugador)
        print(mensaje)
        #NO BORRAR
        limpiar_consola()
        if mensaje =="Salio la misma carta, se baraja de nuevo":
            continue
        elif mensaje == "Perdiste el juego":
            break
        else:
            puntuaje_final += 1
    print(f"El puntaje final es: {puntuaje_final}")
    return puntuaje_final

# Jugar Penales
def relatar_penal(eleccion_jugador, eleccion_computadora, accion):
    if eleccion_jugador == 1:
        if accion == "Patear":
            j_mensaje = "Pateaste a la izquierda"
        else:
            j_mensaje = "Te tiras a la izquierda"
    elif eleccion_jugador == 2:
        if accion == "Patear":
            j_mensaje = "Pateaste al centro"
        else:
            j_mensaje = "Te quedas parado en el medio"
    else:
        if accion == "Patear":
            j_mensaje = "Pateaste a la derecha"
        else:
            j_mensaje = "Te tiras a la derecha"


    if eleccion_computadora == 1:
        if accion == "Atajar":
            c_mensaje = "La maquina patea a la izquierda"
        else:
            c_mensaje = "La maquina se tira a la izquierda"
    elif eleccion_computadora == 2:
        if accion == "Atajar":
            c_mensaje = "La maquina patea al centro"
        else:
            c_mensaje = "La maquina se queda parada en el medio"
    else:
        if accion == "Atajar":
            c_mensaje = "La maquina patea a la derecha"
        else:
            c_mensaje = "La maquina se tira a la derecha"
    mensaje_final = f"{j_mensaje}\n{c_mensaje}"
    return mensaje_final


def patear_penal():
    patear_penal_jugador = pedir_numero(f"A donde pateas?:\n1.Izquierda\n2.Centro\n3.Derecha","Error, elegi entre 1 y 3",1,3)
    atajar_penal_computadora = generar_respuesta_maquina(1,3)
    relato = relatar_penal(patear_penal_jugador,atajar_penal_computadora,"Patear")
    print(relato)
    if patear_penal_jugador == atajar_penal_computadora:
        resultado = "ATAJADO"
    else:
        resultado = "GOL"
        
    print(resultado)
    return resultado

def atajar_penal():
    atajar_penal_jugador = pedir_numero(f"A donde te tiras?:\n1.Izquierda\n2.Centro\n3.Derecha","Error, elegi entre 1 y 3",1,3)
    patear_penal_computadora = generar_respuesta_maquina(1,3)
    relato = relatar_penal(atajar_penal_jugador,patear_penal_computadora,"Atajar")
    print(relato)
    if atajar_penal_jugador == patear_penal_computadora:
        resultado = "ATAJADO"
    else:
        resultado = "GOL"
    print(resultado)
    return resultado

def obtener_marcador(goles_jugador,goles_maquina):
    marcador = f"Jugador :{goles_jugador} - Máquina:{goles_maquina}"
    return marcador

def jugar_penales():
    goles_jugador = 0
    goles_maquina = 0
    rondas = 0
    eleccion_jugador = pedir_numero(f"Elegí cara o cruz\n1.Cara o 2.Cruz\n",f"Error, elegi un numero entre 1 y 2\n",1,2)
    moneda = generar_respuesta_maquina(1,2)
    print("Salio cara" if moneda==1 else "Salio cruz")

    while verificar_estado_partida(goles_jugador,goles_maquina,rondas,5):
        rondas += 1 
        print(f"Ronda {rondas}")
        if eleccion_jugador == moneda:
            resultado_patear = patear_penal()
            if resultado_patear == "GOL":
                goles_jugador += 1
            limpiar_consola()
            print(obtener_marcador(goles_jugador,goles_maquina))

            if verificar_estado_partida(goles_jugador,goles_maquina,rondas,5):
                resultado_atajar = atajar_penal()
                if resultado_atajar == "GOL":
                    goles_maquina += 1
            limpiar_consola()
            print(obtener_marcador(goles_jugador,goles_maquina))
        else:
            resultado_atajar = atajar_penal()
            if resultado_atajar == "GOL":
                goles_maquina += 1
            limpiar_consola()
            print(obtener_marcador(goles_jugador,goles_maquina))
            if verificar_estado_partida(goles_jugador,goles_maquina,rondas,5):
                resultado_patear = patear_penal()
                if resultado_patear == "GOL":
                    goles_jugador += 1
            limpiar_consola()
            print(obtener_marcador(goles_jugador,goles_maquina))
    
    while goles_jugador == goles_maquina:
        rondas += 1
        print(f"Ronda {rondas} - Muerte súbita")

        if eleccion_jugador == moneda:
            resultado_patear = patear_penal()
            if resultado_patear == "GOL":
                goles_jugador += 1
            limpiar_consola()
            print(obtener_marcador(goles_jugador, goles_maquina))

            resultado_atajar = atajar_penal()
            if resultado_atajar == "GOL":
                goles_maquina += 1
            limpiar_consola()
            print(obtener_marcador(goles_jugador, goles_maquina))

        else:
            resultado_atajar = atajar_penal()
            if resultado_atajar == "GOL":
                goles_maquina += 1
            limpiar_consola()
            print(obtener_marcador(goles_jugador, goles_maquina))

            resultado_patear = patear_penal()
            if resultado_patear == "GOL":
                goles_jugador += 1
            limpiar_consola()
            print(obtener_marcador(goles_jugador, goles_maquina))
    if goles_jugador > goles_maquina:
        retorno = "El jugador ganó por penales"
    else:
        retorno = "Perdiste la tanda de penales."
        print(retorno)
    return retorno