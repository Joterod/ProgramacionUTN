import random  

def inicializar_matriz(filas:int, columnas:int, valor_inicial:any) -> list:
    matriz = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def mostrar_notas(matriz)->None:
    """
    Funcion que imprime de manera legible las notas de los participantes.
    """
    for col in range(len(matriz[0])):
        promedio = (matriz[0][col] + matriz[1][col] + matriz[2][col]) / 3
        print(f'Participante: {col+1}')
        print(f'Nota Jurado 1: {matriz[0][col]}')
        print(f'Nota Jurado 2: {matriz[1][col]}')
        print(f'Nota Jurado 3: {matriz[2][col]}')
        print(f"Promedio: {promedio:.2f}")
        print('-'*10)
    return None

def calificar_bailarines(matriz_inicial:list, automatico:bool=False)->list:
    '''
    Función que recibe una matriz inicializada en ceros y genera otra de las mismas dimensiones y solicita ingreso de numeros para cada matriz.
    '''
    matriz_puntajes = matriz_inicial
    
    for fil in range(len(matriz_inicial)):
        for col in range(len(matriz_inicial[fil])):
            if automatico:
                matriz_puntajes[fil][col] = random.randint(1,10)
            else:
                matriz_puntajes[fil][col] = int(input(f"Ingrese el puntaje que el juez {fil + 1} dio al bailarín {col + 1} entre 1 y 10"))
                while not 0 < matriz_puntajes[fil][col] < 11:
                    matriz_puntajes[fil][col] = int(input(f"ERROR.Ingrese el puntaje que el juez {fil + 1} dio al bailarín {col + 1} entre 1 y 10"))
    return matriz_puntajes

def ordenar_puntajes_jurado(lista:list, jurado:int=0)->list:
    """
    Esta funcion ordena la lista provista con burbujeo de mayor a menor
    """
    largo = len(lista[jurado])
    for i in range(largo-1):
        for j in range(largo-1-i):
            valor_a = lista[jurado][j]
            valor_b = lista[jurado][j+1]
            if valor_a < valor_b:
                auxiliar = lista[jurado][j]
                lista[jurado][j] = lista[jurado][j+1]
                lista[jurado][j+1] = auxiliar
    return lista[jurado]

def buscar_triple_siete(matriz:list)->str:
    """
    Esta función se encarga de encontrar y mostrar los participantes con puntaje 7 de parte de los 3 jueces"
    """
    informe = ''
    for col in range(len(matriz[0])):
        if matriz[0][col] == 7 and matriz[1][col] == 7 and matriz[2][col] == 7:
            informe += f"Participante Nro {col + 1} tiene triple 7\n"
        if informe == '':
            informe = 'No se encontró ningún participante con tres sietes'
    return informe

def mostrar_bailarines_aplazados(matriz:list)->str:
    """
    Esta función muestra los bailarines aplazados por el jurado nro 3
    """
    informe = ''
    for col in range(len(matriz[0])):
        if matriz[2][col] < 4:
            informe += f"Participante Nro {col + 1} fue aplazado por el juez nro 3\n"
    return informe


def mostrar_top3(matriz):
    lista_promedios = [0,0,0,0,0,0,0,0,0,0]
    for col in range(len(matriz[0])):
        promedio = (matriz[0][col] + matriz[1][col] + matriz[2][col]) / 3
        lista_promedios[col] = promedio
        
    lista_promedios = ordenar_puntajes_jurado(lista_promedios,0)
    return "No llegue a terminarlo"

def verificar_ganador():
    print('no lo termine')

def menu_inicial():
    matriz_inicial = inicializar_matriz(3,10,0)
    flag_matriz = 0
    menu = True
    while menu == True:
        print('Bienvenidos al menú de la competencia de baile.')
        opcion = int(input(
            f'Ingrese la opcion de menu que quiere elegir:\n1.Calificar bailarines\n2.Mostrar notas\n3.Ordenar Bailarines JN°2\n4.Triple 7\n5.Jurado Malo\n6.TOP3\n7.Verificar Ganador\n8.Salir\n'
            ))
        match opcion:
            case 1:
                flag_matriz = 1
                matriz_puntajes = calificar_bailarines(matriz_inicial, True)
            case 2:
                if flag_matriz == 1:
                    mostrar_notas(matriz_puntajes)
                else:
                    print('No puedes acceder a este menu sin generar primero la matriz')
            case 3:
                if flag_matriz == 1:
                    puntajes_ordenados = (ordenar_jurado_dos(matriz_puntajes,2))
                    print(puntajes_ordenados)
                else:
                    print('No puedes acceder a este menu sin generar primero la matriz')
            case 4:
                if flag_matriz == 1:
                    triple_siete = (buscar_triple_siete(matriz_puntajes))
                    print(triple_siete)
                else:
                    print('No puedes acceder a este menu sin generar primero la matriz')
            case 5:
                if flag_matriz == 1:
                    bailarines_aplazados = mostrar_bailarines_aplazados(matriz_puntajes)
                    print(bailarines_aplazados)
                else:
                    print('No puedes acceder a este menu sin generar primero la matriz')
            case 6:
                mostrar_top3()
            case 7:
                verificar_ganador()
            case 8:
                menu = False
            case _:
                print("Elegiste una opción no valida")

'''
EJECUCIÓN
'''

menu_inicial()