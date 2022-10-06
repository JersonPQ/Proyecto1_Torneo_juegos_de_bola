###########################################
##                                       ##
##              funciones                ##
##                                       ##
###########################################


# función para el menú de configuración de torneo
def config_torneo(datos):
    print("\n\n\n     Torneos de bola\n")
    print("  Configuración del torneo\n")

    configuracion_torneo = datos

    # asignación de nombre y validación que nombre de torneo sea entre 10 y 40 caracteres
    while True:
        nombre = str(input("Nombre del torneo: "))

        if 10 <= len(nombre) <= 40:
            break
        else:
            print("ERROR: Nombre de torneo debe tener entre 10 y 40 carácteres.")

            if len(nombre) > 40:
                print("Se ha excedido por", len(nombre) - 40, "caracteres.\n")
            elif len(nombre) < 10:
                print("Le ha hecho falta", 10 - len(nombre), "caracteres.\n")

    # asignación de equipos participantes y validación que cantidad equipos participantes sea un número entero par >= 2
    while True:
        try:
            cant_equip_participante = int(input("Cantidad de equipos participantes: "))

            if cant_equip_participante % 2 == 0 and cant_equip_participante >= 2:
                break
            else:
                print("ERROR: Valor ingresado debe ser un número entero par mayor o igual que 2.\n")

        except ValueError:
            print("ERROR: Valor ingresado debe ser un número entero par mayor o igual que 2.\n")

    # asignación de equipos que clasifican y validación que cantidad equipos que clasifican sea >= 1 y < que equipos
    # que participan
    while True:
        try:
            cant_equip_clasif_direct = int(input("Cantidad de equipos que clasifican directamente: "))

            if 1 <= cant_equip_clasif_direct < cant_equip_participante:
                break
            else:
                print(
                    "ERROR: Valor ingresado debe ser un número entero mayor o igual que 1 y, menor que la cantidad de \
                    equipos participantes.\n")

        except ValueError:
            print(
                "ERROR: Valor ingresado debe ser un número entero mayor o igual que 1 y, menor que la cantidad de \
                equipos participantes.\n")

            # asignación de puntos ganado por partido ganado y validación que puntos por partido ganado debe ser
            # entero >= 1
    while True:
        try:
            puntos_gan_partido_gan = int(input("Puntos ganados por cada partido ganado: "))

            if puntos_gan_partido_gan >= 1:
                break
            else:
                print("ERROR: Valor ingresado debe ser un número entero mayor o igual que 1.\n")

        except ValueError:
            print("ERROR: Valor ingresado debe ser un número entero mayor o igual que 1.\n")

    # asignación de puntos por partido empatado y validación que puntos por partido empatado debe ser entero >= 0 y
    # menor que puntos por partido ganado
    while True:
        try:
            puntos_gan_partido_empatado = int(input("Puntos ganados por cada partido empatado: "))

            if 0 <= puntos_gan_partido_empatado < puntos_gan_partido_gan:
                break
            else:
                print(
                    "ERROR: Valor ingresado debe ser un número entero mayor o igual que 0 y, menor que puntos ganados \
                    por partido ganado.\n")

        except ValueError:
            print(
                "ERROR: Valor ingresado debe ser un número entero mayor o igual que 0 y, menor que puntos ganados por \
                partido ganado.\n")

    while True:
        opcion_ingresada_config_torneo = input("\nOPCIÓN       <C> CANCELAR    <A> ACEPTAR ")

        # en caso de presionar "A" se guardan los datos ingresados
        if opcion_ingresada_config_torneo == "A":
            if configuracion_torneo != []:  # en caso de configuración no está vacía elimina todos los datos para
                del configuracion_torneo[:]  # volver a ingresarlos

            configuracion_torneo.insert(0, nombre)
            configuracion_torneo.insert(1, cant_equip_participante)
            configuracion_torneo.insert(2, cant_equip_clasif_direct)
            configuracion_torneo.insert(3, puntos_gan_partido_gan)
            configuracion_torneo.insert(4, puntos_gan_partido_empatado)

            # verificación de que todos los datos solicitados se registraron con éxito
            if len(configuracion_torneo) == 5:
                print("\n¡Configuración de torneo registrada con éxito!\n")
                print("Ver detalles a continuación:\n")
                print("Nombre de torneo:", nombre)
                print("Cantidad de equipos participantes:", cant_equip_participante)
                print("Cantidad de equipos que clasifican directamente:", cant_equip_clasif_direct)
                print("Cantidad de puntos ganados por partido ganado:", puntos_gan_partido_gan)
                print("Cantidad de puntos ganados por partido empatado:", puntos_gan_partido_empatado, "\n")
            else:
                print("\nConfiguración de torneo no se ha podido registrar con éxito\n")
            break
        # en caso de ingresar "C" se omiten los datos ingresados y no se guardan
        elif opcion_ingresada_config_torneo == "C":
            break
        else:
            print("ERROR: Valor ingresado debe ser \"C\" o \"A\".\n")

    # retorna lista
    return configuracion_torneo


# función para el menú de agregar equipo en registro de equipos
def agregar_equipo(lista, cant_equip_participantes):
    lista_equipos = lista

    # while para el menú
    while True:
        if len(lista_equipos) < cant_equip_participantes:  # valida que no se agreguen mas equipos de los puestos en
            print("\n\n\n         Torneos de bola\n")  # configuración de torneo
            print("      Registrar equipos: Agregar equipos\n")

            while True:
                # solicita código de equipo, validación de que no esté registrado y que tenga 3 carácteres,
                # en caso de ingresar "C" se sale
                codigo_equipo = str(input("Código del equipo:    "))
                if codigo_equipo == "C":
                    break

                # validación de que el código de equipo sea en mayúscula y que sean 3 caracteres, la función
                # .isupper() retorna True en caso de que la variable consultada contenga todo su valor en mayúscula
                if not (len(codigo_equipo) == 3 and codigo_equipo.isupper()):
                    print("\"Favor ingresar 3 caracteres en mayúscula.\"\n")
                else:
                    # revisa en cada tupla de la lista de equipos si está el código del equipo
                    for equipo in lista_equipos:
                        if codigo_equipo in equipo[0]:
                            print("\"Este equipo ya está registrado, no se puede agregar.\"\n")
                            break
                    else:
                        break

            if codigo_equipo == "C":
                break

            while True:
                nombre_equipo = str(input("Nombre del equipo:    "))

                if 3 <= len(nombre_equipo) <= 40:
                    break
                else:
                    print("\"Nombre de equipo debe tener entre 3 y 40 caracteres\"")

                    if len(nombre_equipo) > 40:
                        print("\"Nombre de equipo se ha excedido por", len(nombre_equipo) - 40, "caracteres\"\n")
                    else:
                        print("\"Nombre de equipo le ha hecho falta", 3 - len(nombre_equipo), "caracteres\"\n")

            while True:
                opcion = input("\nOPCIÓN:       <C> Cancelar    <A> Aceptar ")

                # en caso de presionar "A" guarda los datos, si presiona "C" se cancela y vuelve al menú anterior
                if opcion == "A":
                    tupla_equipo = codigo_equipo, nombre_equipo
                    lista_equipos.append(tupla_equipo)
                    break
                elif opcion == "C":
                    break
                else:
                    print("ERROR: Valor ingresado debe ser \"C\" o \"A\".\n")
        else:
            print("\n\"Límite cantidad de equipos alcanzado, no se puede agregar más equipos.\"\n")

            break

    return lista_equipos


# función para el menú de consultar equipo en registro de equipos
def consultar_equipo(lista):
    while True:
        print("\n\n\n         Torneos de bola\n")
        print("      Registrar equipos: Consultar equipos\n")

        while True:
            # solicita código de equipo, validación de que esté registrado y que tenga 3 carácteres, en caso de
            # ingresar "C" se sale
            codigo_equipo = input("Código del equipo:    ")
            if codigo_equipo == "C":
                break

            # validación de que el código de equipo sea en mayúscula y que sean 3 caracteres, la función .isupper()
            # retorna True en caso de que la variable consultada contenga todo su valor en mayúscula, en caso de no
            # cumplirse, imprime mensaje y vuelve al inicio del ciclo
            if not (len(codigo_equipo) == 3 and codigo_equipo.isupper()):
                print("\"Favor ingresar 3 caracteres en mayúscula.\"\n")
                continue
            else:
                # revisa en cada tupla de la lista de equipos si está el código del equipo
                for equipo in lista:
                    if codigo_equipo in equipo[0]:
                        print("Nombre del equipo:   ", equipo[1], "\n")
                        break
                else:  # en caso de no encontrar código de equipo, imprime mensaje y vuelve al inicio de ciclo
                    print("\"Este equipo no está registrado, no se puede consultar\"\n")
                    continue
            break

        if codigo_equipo == "C":
            break

        while True:
            opcion_modificar_equipos = input("OPCIÓN:    <A> Aceptar ")

            if opcion_modificar_equipos == "A":
                break
            else:
                print("ERROR: Valor ingresado debe ser \"A\".\n")


# función para el menú de modificar equipo en registro de equipos
def modificar_equipo(lista):
    posicion_equipo_lista = None  # esto es solo para inicializar una variable local
    lista_equipos = lista

    while True:
        print("\n\n\n         Torneos de bola\n")
        print("    Registrar equipos: Modificar equipos\n")

        while True:
            # solicita código de equipo, validación de que esté registrado y que tenga 3 carácteres, en caso de
            # ingresar "C" se sale
            codigo_equipo = input("Código del equipo:    ")
            if codigo_equipo == "C":
                break

            # validación de que el código de equipo sea en mayúscula y que sean 3 caracteres, la función .isupper()
            # retorna True en caso de que la variable consultada contenga todo su valor en mayúscula, en caso de no
            # cumplirse, imprime mensaje y vuelve al inicio del ciclo
            if not (len(codigo_equipo) == 3 and codigo_equipo.isupper()):
                print("\"Favor ingresar 3 caracteres en mayúscula.\"\n")
                continue
            else:
                # revisa en cada tupla de la lista de equipos si está el código del equipo
                for equipo in lista:
                    if codigo_equipo in equipo[0]:
                        posicion_equipo_lista = lista.index(equipo)
                        print("Nombre del equipo:   ", equipo[1])
                        break
                else:  # en caso de no encontrar código de equipo, imprime mensaje y vuelve al inicio de ciclo
                    print("\"Este equipo no está registrado, no se puede modificar\"\n")
                    continue
            break

        if codigo_equipo == "C":
            break

        while True:
            nuevo_nombre = str(input("Nombre modificado del equipo: "))

            if 3 <= len(nuevo_nombre) <= 40:
                break
            else:
                print("\"Nombre de equipo debe tener entre 3 y 40 caracteres\"")

                if len(nuevo_nombre) > 40:
                    print("\"Nombre de equipo se ha excedido por", len(nuevo_nombre) - 40, "caracteres\"\n")
                else:
                    print("\"Nombre de equipo le ha hecho falta", 3 - len(nuevo_nombre), "caracteres\"\n")

        while True:
            opcion_modificar_equipos = input("\nOPCIÓN:       <C> Cancelar    <A> Aceptar ")

            if opcion_modificar_equipos == "A":
                equipo_modificado = codigo_equipo, nuevo_nombre

                del lista_equipos[posicion_equipo_lista]
                lista_equipos.insert(posicion_equipo_lista, equipo_modificado)
                break
            elif opcion_modificar_equipos == "C":
                break
            else:
                print("ERROR: Valor ingresado debe ser \"C\" o \"A\".\n")

    return lista_equipos


# función para el menú eliminar equipo en registro de equipos
def eliminar_equipos(lista):
    posicion_equipo_lista = None
    lista_equipos = lista

    while True:
        print("\n\n\n         Torneos de bola\n")
        print("    Registrar equipos: Eliminar equipos\n")

        while True:
            # solicita código de equipo, validación de que esté registrado y que tenga 3 carácteres, en caso de
            # ingresar "C" se sale
            codigo_equipo = input("Código del equipo:    ")
            if codigo_equipo == "C":
                break

            # validación de que el código de equipo sea en mayúscula y que sean 3 caracteres, la función .isupper()
            # retorna True en caso de que la variable consultada contenga todo su valor en mayúscula, en caso de no
            # cumplirse, imprime mensaje y vuelve al inicio del ciclo
            if not (len(codigo_equipo) == 3 and codigo_equipo.isupper()):
                print("\"Favor ingresar 3 caracteres en mayúscula.\"\n")
                continue
            else:
                # revisa en cada tupla de la lista de equipos si está el código del equipo
                for equipo in lista:
                    if codigo_equipo in equipo[0]:
                        posicion_equipo_lista = lista.index(equipo)
                        print("Nombre del equipo:   ", equipo[1])
                        break
                else:  # en caso de no encontrar código de equipo, imprime mensaje y vuelve al inicio de ciclo
                    print("\"Este equipo no está registrado, no se puede eliminar.\"\n")
                    continue
            break

        if codigo_equipo == "C":
            break

        while True:
            opcion_modificar_equipos = input("\nOPCIÓN:       <C> Cancelar    <A> Aceptar ")

            # en caso de ingresar "A" elimina el equipo con el código respectivo
            if opcion_modificar_equipos == "A":
                del lista_equipos[posicion_equipo_lista]
                break
            elif opcion_modificar_equipos == "C":
                break
            else:
                print("ERROR: Valor ingresado debe ser \"C\" o \"A\".\n")

    return lista_equipos


# funcion para crear combinacion de calendario de equipos
def crear_calendario(lista_equipos):
    parejas = []
    lista_codigo_equipos = []
    cantidad_fechas = len(lista_equipos) - 1
    cantidad_partidos_fecha = len(lista_equipos) // 2
    intermediario_partidos_vuelta = []

    for equipo in lista_equipos:
        lista_codigo_equipos.append(equipo[0])

    for fecha in range(cantidad_fechas):
        parejas_fecha_ida = []
        parejas_fecha_vuelta = []
        primera_mitad_equipos = lista_codigo_equipos[:cantidad_partidos_fecha]
        segunda_mitad_equipos = list(reversed(lista_codigo_equipos[cantidad_partidos_fecha:]))

        for indice in range(len(primera_mitad_equipos)):
            parejas_fecha_ida.append((primera_mitad_equipos[indice], segunda_mitad_equipos[indice]))
            parejas_fecha_vuelta.append((segunda_mitad_equipos[indice], primera_mitad_equipos[indice]))

        parejas.append(tuple(parejas_fecha_ida))
        intermediario_partidos_vuelta.append(tuple(parejas_fecha_vuelta))
        lista_codigo_equipos = lista_codigo_equipos[0:1] + lista_codigo_equipos[2:] + lista_codigo_equipos[1:2]

    for pareja_vuelta in intermediario_partidos_vuelta:
        parejas.append(tuple(pareja_vuelta))

    return parejas


def agregar_resultados(juegos, resultados_marcador, resultados_goles):
    resultados = resultados_marcador
    goleadores = resultados_goles

    while True:
        reposicion = 0
        anotadores_goles_casa, anotadores_goles_visita = [], []
        print("\n\n\n                       Torneos de bola\n")
        print("              Registrar resultados: Agregar\n")
        partido_existe = False
        # solicita código de equipo, validación de que no esté registrado y que tenga 3 carácteres,
        # en caso de ingresar "C" se sale
        codigo_equipo_casa = input("Código del equipo casa:   ")
        if codigo_equipo_casa == "C":
            break

        codigo_equipo_visita = input("Código del equipo visita:   ")
        partido_a_agregar = codigo_equipo_casa, codigo_equipo_visita
        # validación de que el código de equipo sea en mayúscula y que sean 3 caracteres, la función
        # .isupper() retorna True en caso de que la variable consultada contenga su valor en mayúscula
        if not (len(codigo_equipo_casa) == 3 and len(codigo_equipo_visita) == 3 and codigo_equipo_visita.isupper()
                and codigo_equipo_casa.isupper()):
            print("\"Favor ingresar 3 caracteres en mayúscula para equipo casa y equipo visita.\"\n")
            continue
        else:
            # revisa en cada tupla de la lista de equipos si está el código del partido
            for i, fecha in enumerate(juegos):
                for indice, partido in enumerate(fecha):
                    if partido_a_agregar == partido:
                        partido_existe = True
                        indice_fecha = i
                        indice_partido = indice
                        break

            if not partido_existe:
                print("Este juego no está en el calendario, no se puede agregar.\n")
                continue

        # crea una lista de tuplas vacías de la misma cantidad de partidos, que se usará para registrar los goleador
        if goleadores == []:
            for fecha in juegos:
                goleadores_fecha = []
                for partido in fecha:
                    goleadores_fecha.append(())

                goleadores.append(tuple(goleadores_fecha))

        # crea una lista de tuplas vacías de la misma cantidad de partidos, que se usará para registrar los results
        if resultados == []:
            for fecha in juegos:
                resultado_fecha = []
                for partido in fecha:
                    resultado_fecha.append(())

                resultados.append(tuple(resultado_fecha))

        # si los resultados del partido solicitado ya tienen marcador, entonces me devuelve al principio e imprime
        # que ya está registrado el marcador
        if resultados[indice_fecha][indice_partido] != ():
            print("\"Este juego ya está registrado, no se puede agregar\".")
            continue

        while True:
            try:
                cantidad_goles_casa = int(input("\nGoles del equipo casa:    "))
                if not (cantidad_goles_casa >= 0):
                    print("Cantidad de goles debe ser un numero mayor o igual que 0.")
                else:
                    break
            except ValueError:
                print("Cantidad de goles debe ser un numero mayor o igual que 0.")

        # solicita el anotador y el minuto las veces que sea igual a la cantidad de goles casa
        for gol in range(cantidad_goles_casa):
            while True:
                try:
                    anotador = input("\n      - Anotador: ")
                    if len(anotador) > 40 or len(anotador) < 2:
                        print("\"Nombre de anotador debe tener entre 2 y 40 caracteres\"")
                        if len(anotador) > 40:
                            print("\"Nombre de anotador se ha excedido por", len(anotador) - 40, "caracteres\"\n")
                        else:
                            print("\"Nombre de anotador le ha hecho falta", 2 - len(anotador), "caracteres\"\n")

                    minuto = int(input("      - Minuto: "))
                    if 40 >= len(anotador) >= 2 and 0 < abs(minuto) <= 120:
                        if minuto in [45, 90, 120]:
                            reposicion = int(input("      - Reposición: "))
                            if reposicion <= 0:
                                print("Minuto de reposición debe ser mayor que 0")
                                continue

                        anotadores_goles_casa += (anotador, minuto, reposicion),
                        break

                    if abs(minuto) > 120:
                        print("Minuto debe ser un numero entero entre 0 y +-120.")

                except ValueError:
                    print("Minuto debe ser un numero entero entre 0 y +-120.")

        while True:
            try:
                cantidad_goles_visita = int(input("\nGoles del equipo visita:    "))
                if not (cantidad_goles_visita >= 0):
                    print("Cantidad de goles debe ser un numero mayor o igual que 0.")
                else:
                    break
            except ValueError:
                print("Cantidad de goles debe ser un numero mayor o igual que 0.")

        # solicita el anotador y el minuto las veces que sea igual a la cantidad de goles visita
        for gol in range(cantidad_goles_visita):
            while True:
                try:
                    anotador = input("\n      - Anotador: ")
                    if len(anotador) > 40 or len(anotador) < 2:
                        print("\"Nombre de anotador debe tener entre 2 y 40 caracteres\"")
                        if len(anotador) > 40:
                            print("\"Nombre de equipo se ha excedido por", len(anotador) - 40, "caracteres\"\n")
                        else:
                            print("\"Nombre de equipo le ha hecho falta", 2 - len(anotador), "caracteres\"\n")

                    minuto = int(input("      - Minuto: "))
                    if 40 >= len(anotador) >= 2 and 0 <= minuto <= 120:
                        # si el minuto es 45, 90 o 120, entonces me solicita que ingrese el minuto de reposicion
                        if minuto in [45, 90, 120]:
                            reposicion = int(input("      - Reposición: "))
                            while True:
                                if reposicion > 0:
                                    break

                                print("Minuto de reposición debe ser mayor que 0.\n")

                        anotadores_goles_visita += (anotador, minuto, reposicion),
                        break
                    if minuto > 120 or minuto < 0:
                        print("Minuto debe ser un numero entero entre 0 y 120.")
                except ValueError:
                    print("Minuto debe ser un numero entero entre 0 y 120.")

        while True:
            opcion = input("\nOPCIÓN:       <C> Cancelar    <A> Aceptar ")

            if opcion == "A":
                copia_fecha_resultado = list(resultados[indice_fecha])
                del copia_fecha_resultado[indice_partido]
                del resultados[indice_fecha]
                copia_fecha_resultado.insert(indice_partido, (cantidad_goles_casa, cantidad_goles_visita))
                resultados.insert(indice_fecha, tuple(copia_fecha_resultado))

                copia_fecha_goleador = list(goleadores[indice_fecha])
                del copia_fecha_goleador[indice_partido]
                del goleadores[indice_fecha]
                goleadores_partido = tuple(anotadores_goles_casa), tuple(anotadores_goles_visita)
                copia_fecha_goleador.insert(indice_partido, goleadores_partido)
                goleadores.insert(indice_fecha, tuple(copia_fecha_goleador))
                break

            elif opcion == "C":
                break

            else:
                print("ERROR: Valor ingresado debe ser \"C\" o \"A\".\n")

    return resultados, goleadores


###########################################
##                                       ##
##          programa principal           ##
##                                       ##
###########################################

datos_config_torneo = []
equipos = []
calendario_juegos = []
resultados_marcadores, resultados_goleadores = [], []

while True:  # ciclo siempre True para el menú
    print("\n\n   Torneos de bola\n")
    print("1. Configuración del torneo")
    print("2. Registrar equipos")
    print("3. Crear y consultar el calendario de juegos")
    print("4. Registrar los resultados de cada fecha")
    print("5. Tabla de posiciones")
    print("6. Tabla de goleadores")
    print("7. Ayuda")
    print("8. Acerca de")
    print("0. Salir\n")

    while True:
        try:  # try y except en caso de que se ingrese un dato no numérico que envíe el mensaje correspondiente
            opcion_men_principal = int(input("OPCIÓN: "))

            if opcion_men_principal in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                break
            else:
                print("\"ERROR: Valor ingresado debe ser un numero del 0 al 8.\"\n")

        except ValueError:
            print("\"ERROR: Valor ingresado debe ser un numero del 0 al 8.\"\n")

    # Menú configuración torneo
    if opcion_men_principal == 1:
        if not equipos:  # validación que si no se han registrado equipos se puede modificar configuración de torneo
            datos_config_torneo = config_torneo(datos_config_torneo)
        else:
            print("\n\"Ya se ha hecho registro de equipos, por lo que no se puede cambiar la configuración de torneo\"")

    # Menú registro de equipos
    if opcion_men_principal == 2:
        if datos_config_torneo == []:  # Validación de que si no ha configurado el torneo no se puede registrar equipos
            ################## Validar que calendario de juegos no se haya creado ##################
            print("\"Favor ingresar primero configuración de torneo.\"\n")
        else:
            while True:
                print("\n\n\n      Torneos de bola\n")
                print("     Registrar equipos\n")
                print("1.   Agregar equipos")
                print("2.   Consultar equipos")
                print("3.   Modificar equipos")
                print("4.   Eliminar equipos")
                print("0.   Salir")

                while True:
                    try:  # try y except caso de que se ingrese un dato no numérico que envíe el mensaje correspondiente
                        opcion_men_registro_equipos = int(input("\nOPCIÓN: "))

                        if opcion_men_registro_equipos in [0, 1, 2, 3, 4]:
                            break
                        else:
                            print("\"ERROR: Valor ingresado debe ser un número entre 0 y 4.\"\n")

                    except ValueError:
                        print("\"ERROR: Valor ingresado debe ser un número entre 0 y 4.\"\n")

                if opcion_men_registro_equipos == 1:
                    equipos = agregar_equipo(equipos, datos_config_torneo[1])

                if opcion_men_registro_equipos == 2:
                    consultar_equipo(equipos)

                if opcion_men_registro_equipos == 3:
                    equipos = modificar_equipo(equipos)

                if opcion_men_registro_equipos == 4:
                    equipos = eliminar_equipos(equipos)

                if opcion_men_registro_equipos == 0:
                    break

    if opcion_men_principal == 3:
        # si no se han ingresado los datos del equipo o cantidad de equipos es menor a cantidad de equipos a registrar
        # entonces no permite crear calendario
        if datos_config_torneo == [] or len(equipos) < datos_config_torneo[1]:
            print("¡Ups! Para continuar debe registrar la configuración del torneo y agregar la cantidad de equipos "
                  "ingresada en configuración.")
        else:
            if calendario_juegos == []:
                fecha = 0
                calendario_juegos = crear_calendario(equipos)
                print("     ", datos_config_torneo[0])

                for lista_partidos_fecha in calendario_juegos:
                    fecha += 1
                    print("\nFecha:", fecha)
                    for partido in lista_partidos_fecha:
                        for equipo_local in equipos:
                            if partido[0] in equipo_local[0]:
                                equipo_casa = equipo_local[1]
                                break
                        for equipo_visitante in equipos:
                            if partido[1] in equipo_visitante[0]:
                                equipo_visita = equipo_visitante[1]
                                break

                        print(equipo_casa, "-", equipo_visita)
            else:
                fecha = 0
                print("     ", datos_config_torneo[0], "\n")

                for lista_partidos_fecha in calendario_juegos:
                    fecha += 1
                    print("Fecha:", fecha)
                    for partido in lista_partidos_fecha:
                        for equipo_local in equipos:
                            if partido[0] in equipo_local[0]:
                                equipo_casa = equipo_local[1]
                                break
                        for equipo_visitante in equipos:
                            if partido[1] in equipo_visitante[0]:
                                equipo_visita = equipo_visitante[1]
                                break

                        print(equipo_casa, "-", equipo_visita)
                    pausa = input("Presione <ENTER> para ver siguiente fecha\n")

    if opcion_men_principal == 4:
        while True:
            print("\n\n\n      Torneos de bola\n")
            print("     Registrar los resultados\n")
            print("1.   Agregar resultados")
            print("2.   Consultar resultados")
            print("3.   Modificar resultados")
            print("4.   Eliminar resultados")
            print("0.   Salir")

            while True:
                try:  # try y except caso de que se ingrese un dato no numérico que envíe el mensaje correspondiente
                    opcion_men_registro_resultados = int(input("\nOPCIÓN: "))

                    if opcion_men_registro_resultados in [0, 1, 2, 3, 4]:
                        break
                    else:
                        print("\"ERROR: Valor ingresado debe ser un número entre 0 y 4.\"\n")

                except ValueError:
                    print("\"ERROR: Valor ingresado debe ser un número entre 0 y 4.\"\n")

            if opcion_men_registro_resultados == 1:
                if calendario_juegos != []:
                    resultados_marcadores, resultados_goleadores = agregar_resultados(calendario_juegos, resultados_marcadores, resultados_goleadores)
                else:
                    print("¡Oh oh! Para registrar resultados primero debe crear calendario de juegos.")

            elif opcion_men_registro_resultados == 0:
                break

    if opcion_men_principal == 0:
        break
