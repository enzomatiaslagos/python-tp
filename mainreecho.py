import funciones

print("Cargando juego")
diccionarioPalabrasCant = funciones.diccionario(funciones.listavalida(funciones.elimina_caracteres(funciones.remplazarAcentos(funciones.textoNuevo(funciones.obtener_texto())))))
print("Juego cargado")
cantidad = funciones.numeroJugadores()
dicc_jugadores_orden = funciones.jugadores(cantidad)
jugadores_palabra,largo = funciones.diccionario_lista_jugadores(dicc_jugadores_orden,diccionarioPalabrasCant)
diccionario_jugadores = funciones.palabra_a_adivinar(jugadores_palabra, largo)
dicc_resultados = funciones.creacion_diccionario_resultados(jugadores_palabra)
nuevo_orden = {}
seguir = True
partida = 0
while seguir:

    dicc_ganador = {}
    dicc_perdedores = {}
    no_gana =  True
    partida += 1

    if partida > 1:

        jugadores_palabra, largo = funciones.diccionario_lista_jugadores(nuevo_orden,
                                                                             diccionarioPalabrasCant)
        diccionario_jugadores = funciones.palabra_a_adivinar(jugadores_palabra, largo)

    while funciones.gana_maquina(diccionario_jugadores,cantidad) == False and no_gana:

        for clave in diccionario_jugadores:

            palabra,lista_aciertos, puntos, aciertos, desaciertos, letras_anteriores,intentos = funciones.diccionario_a_variable(diccionario_jugadores,clave)
            vuelve_jugar = True
            if no_gana:
                while funciones.autoriza_jugar(desaciertos,intentos) and vuelve_jugar:
                    print("")
                    print("turno de: ",clave," tiene ", aciertos,"aciertos y ",desaciertos,"desaciertos")
                    print("palabra: ",lista_aciertos,"usted uso", letras_anteriores)
                    letra = funciones.ingreso_letra(letras_anteriores)
                    letras_anteriores.append(letra)
                    lista_aciertos = funciones.posicion_adivinada(palabra,letra,lista_aciertos)
                    puntos = funciones.suma_puntos(puntos,letra,palabra,lista_aciertos)

                    if funciones.aciertos_o_desaciertos(letra,palabra):

                        aciertos = funciones.suma_cantidad_de_caractes(aciertos,letra,palabra)

                        if funciones.ganador(palabra, lista_aciertos):
                            vuelve_jugar = False
                            no_gana = False
                            print("El ganador es: ", clave)
                            dicc_ganador[clave] = [puntos, aciertos, desaciertos]
                            dicc_perdedores = funciones.diccionario_ganador_jugador(clave, diccionario_jugadores)

                    else:

                        vuelve_jugar = False
                        desaciertos += 1

                    intentos += 1

        funciones.variable_a_diccionario(palabra,lista_aciertos, puntos, aciertos, desaciertos,
                                                  letras_anteriores,intentos, clave, diccionario_jugadores)

    if funciones.gana_maquina(diccionario_jugadores, cantidad):
        print("Han perdido todos los jugadores, gano la maquina.")
        dicc_perdedores = funciones.diccionario_gana_maquina(diccionario_jugadores)
        dicc_resultados = funciones.diccionario_suma_resultados(dicc_perdedores,dicc_resultados)

    else:

        dicc_resultados = funciones.diccionario_suma_resultados(dicc_ganador,dicc_resultados)
        dicc_perdedores = funciones.diccionario_suma_resultados(dicc_perdedores,dicc_resultados)

    funciones.impresion_de_resultados(dicc_resultados,partida)

    seguir = int(input("desea jugar otra partida escriba 0, si desea terminar escriba 1: "))

    if seguir == 0:
        seguir = True
        if funciones.gana_maquina(diccionario_jugadores,cantidad):
            nuevo_orden = dict(sorted(dicc_resultados.items(), key=lambda x: x[1], reverse=True))
        else:
            nuevo_orden = funciones.nuevo_orden_gana_jugador(dicc_ganador,dicc_perdedores,dicc_resultados)
    else:
        seguir = False

