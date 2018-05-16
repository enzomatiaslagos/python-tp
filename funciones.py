import random

def numeroJugadores():
    """Devulve cantidad de jugadores"""
    seguir = True
    while seguir:
        cantJugadores = int(input("Cantidad de jugadores:"))
        if 2 <= cantJugadores <= 10:
            seguir = False
        else:
            print("Cantidad incorrecta, vuelva a ingresar cantidad de jugadores.")
    return cantJugadores

def jugadores(cantJugadores):
    """Devuelve diccionario con el nombre de los jugadores y su orden de juego (que fue dado de manera aleatoria)"""
    nombreJugadores = []
    while len(nombreJugadores) != cantJugadores:
        nombreJugadores.append(str(input("Ingrese nombre y apellido:")).upper())
    orden = range(1, cantJugadores + 1)
    import random
    nombresAleatorios = random.sample(nombreJugadores,
                                      cantJugadores)  # Da un orden aleatorio en que fueron ingresados los nombres
    jugadoresYSuOrden = dict(zip(nombresAleatorios, orden))
    for clave, valor in jugadoresYSuOrden.items():
        print("El jugador", clave, "jugara en la posicion", valor)
    return jugadoresYSuOrden

def listaNombres(jugadoresYSuOrden):
    nombres = list(jugadoresYSuOrden.keys())
    return nombres

def largoPalabra():
    seguir = True
    while seguir:
        largo = int(input("Ingrese largo de la palabra, mayor a 5, con la que quiere jugar:"))
        if largo >= 5:
            seguir = False
        else:
            print("Ingrese otro largo, no existen palabras para el largo ingresado.")
    return largo

def asignacionPalabra(listaJugadores,listaPalabras,largo):
    jugadoresYPalabra = {}
    palabrasDelLargo = []
    for palabra in listaPalabras:
        if len(palabra) == largo:
            palabrasDelLargo.append(palabra)
    for nombre in listaJugadores:
        jugadoresYPalabra[nombre] = random.choice(palabrasDelLargo)
    return jugadoresYPalabra

def palabra_a_adivinar(jugadoresYPalabra,largo):
    diccionario = {}
    lista_aciertos = []
    for i in range[largo]:
        lista_aciertos.append("-")
    for jugadores in jugadoresYPalabra:
        diccionario[jugadores] = [jugadoresYPalabra[jugadores],lista_aciertos,0,0,0,[]]
        """posiciones={nombre:palabra,palabra_adivinada,puntos,aciertos,desaciertos,letras_ingresadas}"""
    return diccionario

def ingreso_letra(letras_anteriores):
    letra=input("Ingrese letra:")
    continuar = True
    while continuar == True:
        if letra.isdigit()!= True:
            letra = input("Error, ingrese una letra valida: ")
        elif letra in letras_anteriores:
            letra=input("Por favor, ingrese una letra que no haya intentado anteriormente:")
        else:
            continuar = False
    return (letra)

def diccionario_a_variable(diccionario,jugador):
    palabra = diccionario[jugador][0]
    lista_aciertos = diccionario[jugador][1]
    puntos = diccionario[jugador][2]
    intentos = diccionario[jugador][3]
    desaciertos = diccionario[jugador][4]
    letras_ingresadas = diccionario[jugador][5]
    return palabra,lista_aciertos,puntos,intentos,desaciertos,letras_ingresadas


def posicion_adivinada(palabra,letra,lista_aciertos):
    lista_palabra = []
    largo_palabra = len[lista_palabra]
    for caracter in palabra:
        lista_palabra.append(caracter)
    if letra in lista_palabra:
        for i in range[largo_palabra]:
            if letra == lista_palabra[i]:
                lista_aciertos.insert(i,letra)
    print(lista_aciertos)
    return lista_aciertos

def ganador(palabra,lista_aciertos):
    lista_palabra = []
    for caracter in palabra:
        lista_palabra.append(caracter)
    if lista_palabra == lista_aciertos:
        return True
    else:
        return False

def gana_maquina(diccionario,cantidad):
    maquina = 0
    for clave in diccionario:
        if diccionario[clave][3]==8 or diccionario[clave][4]==7:
            maquina += 1
    if maquina == cantidad:
        return True
    else:
        return False

def aciertos_o_desaciertos(letra,palabra):
    if letra in palabra:
        return True
    else:
        return False

def suma_puntos(puntos,letra,palabra,lista_aciertos):
    if letra in palabra:
        puntos+=1
    elif ganador(palabra,lista_aciertos):
        puntos += 30
    else:
        puntos-=2
    return puntos

def diccionario_resultados(lista_nombres):
    diccionario = {}
    for nombres in lista_nombres:
        diccionario[nombres] = [0,0,0]
    return diccionario

def autoriza_jugar(desaciertos,aciertos):
    intentos = desaciertos + aciertos
    if (desaciertos == 7 or intentos == 8):
        return False
    else:
        return True
#creo diccionario para cuando el ganador es un jugador
def diccionario_ganador_jugador(clave,diccionario_jugadores):
    dicc_otros_jugadores = {}
    for jugador in diccionario_jugadores:
        if jugador != clave:
            dicc_otros_jugadores[jugador] = [diccionario_jugadores[jugador][2],diccionario_jugadores[jugador][3],diccionario_jugadores[jugador][4]]
    return dicc_otros_jugadores

def diccionario_gana_maquina(diccionario_jugadores):
    dicc_resultados = {}
    for jugador in diccionario_jugadores:
        dicc_resultados[jugador] = [diccionario_jugadores[jugador][2],diccionario_jugadores[jugador][3],diccionario_jugadores[jugador][4]]
    return dicc_resultados

def creacion_diccionario_resultados(diccionario_jugadores):
    dicc_resultados = {}
    for jugador in diccionario_jugadores:
        dicc_resultados[jugador] = [0,0,0]
    return dicc_resultados
cantidad = numeroJugadores()
dicc_jugadores_orden = jugadores(cantidad)
lista_nombres = listaNombres(dicc_jugadores_orden)
"""diccionario_palabra = JOACO"""
largo = largoPalabra()
"""validacion joaco para jugar"""
jugadores_palabra = asignacionPalabra(listaNombres(),"""joaco""",largo)
diccionario_jugadores = palabra_a_adivinar(jugadores_palabra,largo)
dicc_resultados = creacion_diccionario_resultados()
seguir = True
gana = False

while seguir:
    dicc_ganador = {}
    dicc_ordenar = {}
    dicc_gana_maquina = {}
    while gana_maquina(diccionario_jugadores,cantidad) == False and gana == False:
        for clave in diccionario_jugadores:
            if gana == False:
                palabra,lista_aciertos, puntos, aciertos, desaciertos, letras_anteriores = diccionario_a_variable(diccionario_jugadores,clave)
                vuelve_jugar = True
                while autoriza_jugar(desaciertos,aciertos) and vuelve_jugar:
                    letra = ingreso_letra(letras_anteriores)
                    letras_anteriores.append(letra)
                    lista_aciertos = posicion_adivinada(palabra,letra,lista_aciertos)
                    suma_puntos(puntos,letra,palabra)
                    if aciertos_o_desaciertos(letra,palabra) == False:
                        vuelve_jugar = False
                        desaciertos += 1
                    else:
                        aciertos += 1
                        if ganador(palabra,lista_aciertos):
                            vuelve_jugar = False
                            gana = True
                            print("el ganador es: ", clave)
                            dicc_ganador[clave] = [puntos,aciertos,desaciertos]
                            dicc_ordenar = diccionario_ganador_jugador(clave,diccionario_jugadores)

    if gana_maquina(diccionario_jugadores,cantidad):
        dicc_gana_maquina = diccionario_gana_maquina(diccionario_jugadores)
        dicc_resultados.update(dicc_gana_maquina)
    else:
        dicc_resultados.update(dicc_ganador)
        dicc_resultados.update(dicc_ordenar)
    print(dicc_resultados)




