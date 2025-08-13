# Sistema de gestion de reservaciones de salas de ensayo YOURSELF STUDIO.

# MAIN.PY - Este es el modulo principal del programa de reservaciones de salas de ensayo YOURSELF STUDIO.

# Importamos modulos y bibliotecas necesarias.

import funciones # Importamos el modulo de funciones.
from reservaciones import reservaciones # Importamos el modulo reservaciones desde el paquete reservaciones.
from salas import salas # Importamos el modulo salas desde el paquete salas.
import conexionBD # Importamos el modulo de conexion a la base de datos.
from datetime import datetime # Importamos el modulo datetime para manejar fechas y horas.
from exportar import exportar # Importamos el modulo exportar desde el paquete exportar.
from exportar import exportarsql # Importamos el modulo exportarsql desde el paquete exportar.
import sys # Importamos el modulo sistema.

pago=35 # Definimos el precio por hora para las reservaciones.

def mainReservaciones(): # Procedimiento principal para manejar las reservaciones.
    opcion = True

    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menuPrincipalReservaciones()

        match opcion: # Match que se encarga de las opciones del menú.

            case "1": # Agendar reservaciones.

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Reservación ::. 🎷\n")
                
                agregar = {} # Diccionario para multiples reservaciones.
                nombregenero_true = True
                while nombregenero_true:
                    try:
                        agregar["Nombre"] = input("\n🎤 Ingresa el nombre de la banda o artista: ").upper().strip()
                        agregar["Genero"] = input("\n🎵 Ingresa el genero: ").upper().strip()
                        if agregar["Nombre"] and agregar["Genero"]:
                            nombregenero_true = False
                        else:
                            print("\n❌ El nombre y el género no pueden estar vacíos.")
                    except Exception as e:
                        print(f"\n❌ Error al ingresar los datos: {e}")

                sala_true=True

                while sala_true:
                    lista_salas = salas.mostrarCapacidad()

                    if len(lista_salas) > 0:
                        print(f"\n🎷 ¿Cuál sala quieres reservar?\n\n\t1. 🟦 Azul (Capacidad: {lista_salas[0][1]})\n\t2. 🟥 Rojo (Capacidad: {lista_salas[1][1]})\n\t3. 🟧 Naranja (Capacidad: {lista_salas[2][1]})\n\t4. ⬜ Blanco (Capacidad: {lista_salas[3][1]})\n\t")
                        salaopcion = input("\t\t 🔢 Elige una opción (1 - 4): ")
                        match salaopcion:
                            case "1": agregar["Sala"] = "AZUL"; sala_true=False
                            case "2": agregar["Sala"] = "ROJO"; sala_true=False
                            case "3": agregar["Sala"] = "NARANJA"; sala_true=False
                            case "4": agregar["Sala"] = "BLANCO"; sala_true=False
                            case _: 
                                print("\n\t❌ Opción inválida, vuelva a intentarlo.")
                                funciones.espereTecla()
                    else:
                        print(f"\n\t❌ No se encontraron salas en este momento, intentelo mas tarde. ")
                        funciones.espereTecla()

                fecha_true=True

                while fecha_true:
                    entrada = input("\n📅 Ingresa la fecha y hora (Formato: YYYY-MM-DD HH:MM) \n(EJEMPLO: 2025-04-23 16:30): ").strip()
                    try:
                        fecha_hora = datetime.strptime(entrada, "%Y-%m-%d %H:%M")
                        agregar["Fecha"] = fecha_hora
                        fecha_true=False
                    except ValueError:
                        print("❌ Formato inválido. Recuerda usar el formato YYYY-MM-DD HH:MM y asegurarte de que la fecha y hora sean válidas.")

                    duracion_valida = True
                    while duracion_valida:
                        try:
                            duracion = int(input("\n⏳ ¿Cuántas horas durará la reservación?: ").strip())
                            if duracion > 0 and duracion <= 12:
                                duracion_valida = False
                            elif duracion <= 0:
                                print("❌ La duración debe ser mayor a cero.")
                            else:
                                print("❌ La duración no puede exceder las 12 horas.")
                        except ValueError:
                            print("❌ Ingresa un número válido.")


                    agregar["Duracion"] = duracion

                personas_true=True

                capacidad_sala = reservaciones.obtenercapacidadSala(agregar["Sala"])
                if capacidad_sala:
                    capacidad = capacidad_sala
                else:
                    print("❌ No se encontró la sala especificada.")
                    funciones.espereTecla()

                total = funciones.calcularPrecio(agregar["Duracion"], pago)
                agregar["Pago"] = total

                while personas_true:
                    try:
                        personas = int(input("\n👥 ¿Cuántas personas asistirán?: ").strip())
                        if personas > 0 and personas <= capacidad:
                            personas_true = False

                            agregar["Personas"] = personas

                            resultado=reservaciones.agregarReservaciones(agregar, fecha_hora)
                            
                            if resultado:
                                print(f"\n✅ Se reservo a {agregar['Nombre']} para la fecha: {fecha_hora}. ")
                                print(f"💵 El costo total a pagar por PERSONA de la reservación es: ${total} MXN.")
                            else:
                                print(f"\n❌ No fue posible agendar en este momento, intentelo mas tarde. ")

                        elif personas <= 0:
                            print("❌ El número de personas debe ser mayor a cero.")
                        else:
                            print("❌ El número de personas no puede exceder la capacidad de las salas.")
                    except ValueError:
                        print("❌ Ingresa un número válido.")

                funciones.espereTecla()

            case "2": # Mostrar reservaciones.

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Mostrar Reservaciones ::. 🎷\n")

                lista_reservaciones=reservaciones.mostrarReservaciones()
                if len(lista_reservaciones)>0:

                    print(f"-"*140)
                    print(f"{'ID':<10} {'Nombre':<15} {'Genero':<15} {'Sala':<15} {'Fecha':<30} {'Duración (hrs)':<15} {'Personas':<15} {'Total a pagar':<15}")
                    print(f"-"*140)
                    for fila in lista_reservaciones:
                        fecha_formateada = fila[4].strftime("%d %b %Y %I:%M %p")
                        print(f"{fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fecha_formateada:<30} {fila[5]:<15} {fila[6]:<15} {fila[7]:<15}")
                else:
                    print(f"\n❌ No hay reservaciones en este momento. ")

                funciones.espereTecla()
            
            case "3": # Buscar reservaciones.

                funciones.borrarPantalla()

                lista_reservaciones=reservaciones.mostrarReservaciones()
                if len(lista_reservaciones)>0:

                    print("\n\t\t\t🎸 .:: Buscar Reservaciones ::. 🎷\n")
                    decision=input("🔎 ¿Deseas buscar por ID o por nombre de artista? (ID/NOMBRE): ").upper().strip()

                    if decision=="ID":
                        id=input("🆔 Ingresa el ID de la reservación: ").strip()
                        respuesta=reservaciones.buscarReservaciones(id,"")

                        funciones.formatoBusqueda(respuesta) # Procedimiento para mostrar el formato de búsqueda.

                    elif decision=="NOMBRE":
                        nombre=input("👦 Ingresa el nombre del artista de la reservación: ").upper().strip()
                        respuesta=reservaciones.buscarReservaciones(0, nombre)

                        funciones.formatoBusqueda(respuesta) # Procedimiento para mostrar el formato de búsqueda.
                
                else:
                    print(f"\n❌ No hay reservaciones en este momento. ")

                funciones.espereTecla()
            
            case "4":  # Modificar reservaciones

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Modificar Reservaciones ::. 🎷\n")

                lista_reservaciones=reservaciones.mostrarReservaciones()
                if len(lista_reservaciones)>0:

                    print(f"-"*140)
                    print(f"{'ID':<10} {'Nombre':<15} {'Genero':<15} {'Sala':<15} {'Fecha':<30} {'Duración (hrs)':<15} {'Personas':<15} {'Total a pagar':<15}")
                    print(f"-"*140)
                    for fila in lista_reservaciones:
                        fecha_formateada = fila[4].strftime("%d %b %Y %I:%M %p")
                        print(f"{fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fecha_formateada:<30} {fila[5]:<15} {fila[6]:<15} {fila[7]:<15}")
                else:
                    print(f"\n❌ No hay reservaciones en este momento. ")

                if len(lista_reservaciones)>0:
                    id = input("\n🆔 Ingresa el ID de la reservación a modificar: ").strip()
                    respuesta = reservaciones.buscarReservaciones(id, "")

                    if not respuesta:
                        print("❌ No se encontró una reservación con ese ID.")
                    else:
                        print("\nReservación actual:")
                        funciones.formatoBusqueda(respuesta)

                        nuevos_datos = {}
                        nombregen_true=True
                        while nombregen_true:
                            try:
                                nuevos_datos["Nombre"] = input("\n🎤 Nuevo nombre de la banda o artista: ").upper().strip()
                                nuevos_datos["Genero"] = input("🎵 Nuevo género musical: ").upper().strip()
                                if nuevos_datos["Nombre"] and nuevos_datos["Genero"]:
                                    nombregen_true = False
                                else:
                                    print("❌ El nombre y el género no pueden estar vacíos.")
                            except Exception as e:
                                print(f"❌ Error al ingresar los datos: {e}")

                        sala_true = True
                        while sala_true:
                            lista_salas = salas.mostrarCapacidad()
                            print(f"\n🎷 ¿A que sala quieres cambiar para la reservacion?\n\n\t1. 🟦 Azul (Capacidad: {lista_salas[0][1]})\n\t2. 🟥 Rojo (Capacidad: {lista_salas[1][1]})\n\t3. 🟧 Naranja (Capacidad: {lista_salas[2][1]})\n\t4. ⬜ Blanco (Capacidad: {lista_salas[3][1]})\n\t")
                            sala_opcion = input("\n🔢 Elige una opción (1 - 4): ").strip()
                            match sala_opcion:
                                case "1":
                                    nuevos_datos["Sala"] = "AZUL"
                                    sala_true = False
                                case "2":
                                    nuevos_datos["Sala"] = "ROJO"
                                    sala_true = False
                                case "3":
                                    nuevos_datos["Sala"] = "NARANJA"
                                    sala_true = False
                                case "4":
                                    nuevos_datos["Sala"] = "BLANCO"
                                    sala_true = False
                                case _:
                                    print("❌ Opción inválida. Intenta nuevamente.")

                        fecha_true = True
                        while fecha_true:
                            entrada = input("\n📅 Ingresa la fecha y hora (Formato: YYYY-MM-DD HH:MM) \n(EJEMPLO: 2025-04-23 16:30): ").strip()
                            try:
                                nueva_fecha = datetime.strptime(entrada, "%Y-%m-%d %H:%M")
                                fecha_true = False
                            except ValueError:
                                print("❌ Formato inválido. Intenta nuevamente.")

                        duracion_valida = True
                        while duracion_valida:
                            try:
                                duracion = int(input("\n⏳ ¿Cuántas horas durará la nueva reservación?: ").strip())
                                if duracion > 0 and duracion <= 12:
                                    duracion_valida = False
                                elif duracion <= 0:
                                    print("❌ La duración debe ser mayor a cero.")
                                else:
                                    print("❌ La duración no puede exceder las 12 horas.")
                            except ValueError:
                                print("❌ Ingresa un número válido.")

                        nuevos_datos["Duracion"] = duracion

                        personas_validas = True

                        capacidad_sala = reservaciones.obtenercapacidadSala(nuevos_datos["Sala"])
                        if capacidad_sala:
                            capacidad = capacidad_sala
                        else:
                            print("❌ No se encontró la sala especificada.")
                            funciones.espereTecla()

                        while personas_validas:
                            try:
                                personas = int(input("\n👥 ¿Cuántas personas asistirán?: ").strip())
                                if personas > 0 and personas <= capacidad:
                                    nuevos_datos["Personas"] = personas
                                    personas_validas = False
                                elif personas <= 0:
                                    print("❌ El número de personas debe ser mayor a cero.")
                                else:
                                    print("❌ El número de personas no debe superar la capacidad de la sala establecida.")
                            except ValueError:
                                print("❌ Ingresa un número válido.")

                        pago_calculado = funciones.calcularPrecio(nuevos_datos["Duracion"], pago)
                        nuevos_datos["Pago"] = pago_calculado

                        print(f"\n💵 Pago calculado automáticamente: ${pago_calculado}")

                        resp = input(f"\n❔ ¿Estás seguro de modificar esta reservación? (S/N): ").strip().upper()

                        if resp == "S":
                            resultado = reservaciones.modificarReservacion(id, nuevos_datos, nueva_fecha)
                            if resultado:
                                print("\n✅ Reservación modificada exitosamente.")
                            else:
                                print("\n❌ No fue posible modificar la reservación.")
                        else:
                            print("\n❌ Modificación cancelada.")

                    funciones.espereTecla()
                else:
                    funciones.espereTecla()

            case "5": # Eliminar reservaciones.

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Eliminar Reservaciones ::. 🎷\n")

                lista_reservaciones=reservaciones.mostrarReservaciones()
                if len(lista_reservaciones)>0:

                    print(f"-"*140)
                    print(f"{'ID':<10} {'Nombre':<15} {'Genero':<15} {'Sala':<15} {'Fecha':<30} {'Duración (hrs)':<15} {'Personas':<15} {'Total a pagar':<15}")
                    print(f"-"*140)
                    for fila in lista_reservaciones:
                        fecha_formateada = fila[4].strftime("%d %b %Y %I:%M %p")
                        print(f"{fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fecha_formateada:<30} {fila[5]:<15} {fila[6]:<15} {fila[7]:<15}")
                else:
                    print(f"\n❌ No hay reservaciones en este momento. ")

                if len(lista_reservaciones)>0:
                    id = input("\n🆔 Ingresa el ID de la reservación a eliminar: ").strip()
                    respuesta = reservaciones.buscarReservaciones(id, "")

                    if respuesta:
                        print("\nReservación actual:")
                        funciones.formatoBusqueda(respuesta)
                        confirmacion = input("\n❔ ¿Estás seguro de que deseas eliminar esta reservación? (S/N): ").strip().upper()
                        if confirmacion == "S":
                            resultado = reservaciones.eliminarReservaciones(id)
                            if resultado:
                                print("\n✅ Reservación eliminada exitosamente.")
                            else:
                                print("\n❌ No fue posible eliminar la reservación.")
                        elif confirmacion == "N":
                            print("\n❌ Eliminación cancelada.")
                        elif confirmacion == "":
                            print("\n❌ Eliminación cancelada, no se ingresó una opción válida.")
                        else:
                            print("\n❌ Opción inválida, por favor intenta nuevamente.")
                    else:
                        print("\n❌ No se encontraron reservaciones con ese ID.")
                    funciones.espereTecla()
                else:
                    funciones.espereTecla()
            
            case "6": # Limpiar tabla de reservaciones.

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Limpiar Tabla de Reservaciones ::. 🎷\n")
                confirmacion = input("❔ ¿Estás seguro de que deseas eliminar todas las reservaciones? Esta acción no se puede deshacer (S/N): ").strip().upper()
                if confirmacion == "S":
                    resultado = reservaciones.limpiarTablaReservaciones()
                    if resultado:
                        print("\n✅ Todas las reservaciones han sido eliminadas exitosamente.")
                    else:
                        print("\n❌ No fue posible limpiar la tabla de reservaciones.")
                elif confirmacion == "N":
                    print("\n❌ Limpieza cancelada.")
                elif confirmacion == "":
                    print("\n❌ Limpieza cancelada, no se ingresó una opción válida.")
                else:
                    print("\n❌ Opción inválida, por favor intenta nuevamente.")

                funciones.espereTecla()

            case "7": # Salir del menu.
                opcion = False
                funciones.borrarPantalla()
                print(f"\n\tVolviendo al menu principal...")
                funciones.espereTecla()
                main()  # Volver a mostrar el menú principal de reservaciones.

            case _: # Opción inválida.
                funciones.borrarPantalla()
                print("\tOpción inválida, vuelva a intentarlo.")
                funciones.espereTecla()

def mainSalas(): # Procedimiento principal para manejar las salas.
    opcion = True

    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menuPrincipalSalas()

        match opcion: # Match que se encarga de las opciones del menú.

            case "1": # Modificar capacidad de una sala.

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Modificar Capacidad de Sala ::. 🎷\n")
                print("⚠️  Advertencia: Al modificar la capacidad de una sala, se eliminarán automáticamente todas las reservaciones que excedan la nueva capacidad establecida.\n")
                opcion=input("❔ ¿Deseas continuar? (S/N): ").upper().strip()
                if opcion=="N":
                    print("\n❌ Operación cancelada, regresando al menú de salas.")
                elif opcion=="S":
                    lista_salas = salas.mostrarCapacidad()

                    if len(lista_salas) > 0:
                        print(f"\n🟦 Salas disponibles:\n\n\t1. 🟦 Azul (Capacidad: {lista_salas[0][1]})\n\t2. 🟥 Rojo (Capacidad: {lista_salas[1][1]})\n\t3. 🟧 Naranja (Capacidad: {lista_salas[2][1]})\n\t4. ⬜ Blanco (Capacidad: {lista_salas[3][1]})\n")
                        
                        nombre = input("🟦 Ingresa el nombre de la sala a modificar: ").upper().strip()
                        if nombre == "":
                            print("❌ El nombre de la sala no puede estar vacío.")
                        else:
                            capacidad = input("🔢 Ingresa la nueva capacidad de la sala: ").strip()

                            if capacidad.isdigit():
                                capacidad = int(capacidad)
                                if capacidad <= 0:
                                    print("❌ La capacidad debe ser mayor que cero.")
                                else:
                                    resultado = salas.modificarCapacidad(nombre, capacidad)
                                    # Limpiar reservaciones que excedan la nueva capacidad.
                                    salas.limpiarReservacionesExcedidas(nombre, capacidad)
                                    
                                    if resultado:
                                        print(f"\n✅ Capacidad de la sala '{nombre}' modificada a {capacidad}.")
                                    else:
                                        print(f"\n❌ No se encontró una sala con el nombre '{nombre}'.")
                            else:
                                print("\n❌ La capacidad debe ser un número entero positivo.")
                    else:
                        print("\n❌ No hay salas registradas en este momento.")
                elif opcion == "":
                    print("\n❌ Operación cancelada, no se ingresó una opción válida.")
                else:
                    print("\n❌ Opción inválida, por favor intenta nuevamente.")

                funciones.espereTecla()

            case "2": # Mostrar capacidad de las salas.

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Mostrar Capacidad de Salas ::. 🎷\n")
                lista_salas = salas.mostrarCapacidad()
                if len(lista_salas) > 0:
                    print(f"-" * 100)
                    print(f"{'Sala':<20} {'Capacidad':<20}")
                    print(f"-" * 100)
                    for fila in lista_salas:
                        print(f"{fila[0]:<20} {fila[1]:<20}")
                else:
                    print(f"\n❌ No hay salas registradas en este momento. ")
                
                funciones.espereTecla()

            case "3": # Salir del menu.
                
                opcion = False
                funciones.borrarPantalla()
                print(f"\n\tVolviendo al menu principal...")
                funciones.espereTecla()
                main()  # Volver a mostrar el menú principal de reservaciones.
            
            case _: # Opción inválida.
    
                funciones.borrarPantalla()
                print("\tOpción inválida, vuelva a intentarlo.")
                funciones.espereTecla()

def mainExportar(): # Procedimiento principal para manejar la exportación de datos.
    opcion = True

    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menuExportar()

        match opcion: # Match que se encarga de las opciones del menú.

            case "1": # Exportar reservaciones a CSV.

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Exportar Reservaciones a CSV ::. 🎷\n")

                nombre_archivo = input("📁 Ingresa el nombre del archivo (con extensión .csv): ").strip()
                if not nombre_archivo.endswith(".csv"):
                    print("❌ El nombre del archivo debe terminar con '.csv'.") 
                else:
                    resultado = exportar.exportar_reservaciones_csv(nombre_archivo)
                    if resultado:
                        print(f"\n✅ Reservaciones exportadas exitosamente a '{nombre_archivo}'.")
                    else:
                        print("\n❌ No fue posible exportar las reservaciones.")
                
                funciones.espereTecla()

            case "2": # Exportar salas a CSV.

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Exportar Salas a CSV ::. 🎷\n")
                nombre_archivo = input("📁 Ingresa el nombre del archivo (con extensión .csv): ").strip()
                if not nombre_archivo.endswith(".csv"):
                    print("❌ El nombre del archivo debe terminar con '.csv'.") 
                else:
                    resultado = exportar.exportar_salas_csv(nombre_archivo)
                    if resultado:
                        print(f"\n✅ Reservaciones exportadas exitosamente a '{nombre_archivo}'.")
                    else:
                        print("\n❌ No fue posible exportar las reservaciones.")
                
                funciones.espereTecla()

            case "3": # Exportar reservaciones a Excel (XLS).

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Exportar Reservaciones a Excel ::. 🎷\n")
                nombre_archivo = input("📁 Ingresa el nombre del archivo (con extensión .xlsx): ").strip()
                if not nombre_archivo.endswith(".xlsx"):
                    print("❌ El nombre del archivo debe terminar con '.xlsx'.")
                else:
                    resultado = exportar.exportar_reservaciones_excel(nombre_archivo)
                    if resultado:
                        print(f"\n✅ Reservaciones exportadas exitosamente a '{nombre_archivo}'.")
                    else:
                        print("\n❌ No fue posible exportar las reservaciones.")

                funciones.espereTecla()

            case "4": # Exportar salas a Excel (XLS).

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Exportar Salas a Excel ::. 🎷\n")
                nombre_archivo = input("📁 Ingresa el nombre del archivo (con extensión .xlsx): ").strip()
                if not nombre_archivo.endswith(".xlsx"):
                    print("❌ El nombre del archivo debe terminar con '.xlsx'.")
                else:
                    resultado = exportar.exportar_salas_excel(nombre_archivo)
                    if resultado:
                        print(f"\n✅ Salas exportadas exitosamente a '{nombre_archivo}'.")
                    else:
                        print("\n❌ No fue posible exportar las salas.")

                funciones.espereTecla()

            case "5": # Exportar reservaciones a PDF.
                
                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Exportar Reservaciones a PDF ::. 🎷\n")
                nombre_archivo = input("📁 Ingresa el nombre del archivo (con extensión .pdf): ").strip()
                if not nombre_archivo.endswith(".pdf"):
                    print("❌ El nombre del archivo debe terminar con '.pdf'.")
                else:
                    resultado = exportar.exportar_reservaciones_pdf(nombre_archivo)
                    if resultado:
                        print(f"\n✅ Reservaciones exportadas exitosamente a '{nombre_archivo}'.")
                    else:
                        print("\n❌ No fue posible exportar las reservaciones.")

                funciones.espereTecla()

            case "6": # Exportar salas a PDF.
                
                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Exportar Salas a PDF ::. 🎷\n")
                nombre_archivo = input("📁 Ingresa el nombre del archivo (con extensión .pdf): ").strip()
                if not nombre_archivo.endswith(".pdf"):
                    print("❌ El nombre del archivo debe terminar con '.pdf'.")
                else:
                    resultado = exportar.exportar_salas_pdf(nombre_archivo)
                    if resultado:
                        print(f"\n✅ Salas exportadas exitosamente a '{nombre_archivo}'.")
                    else:
                        print("\n❌ No fue posible exportar las salas.")

                funciones.espereTecla()

            case "7": # Exportar SQL de base de datos.

                funciones.borrarPantalla()
                print("\n\t\t\t🎸 .:: Exportar Base de Datos SQL ::. 🎷\n")
                nombre_archivo = input("📁 Ingresa el nombre del archivo (con extensión .sql): ").strip()
                if not nombre_archivo.endswith(".sql"):
                    print("❌ El nombre del archivo debe terminar con '.sql'.")
                else:   
                    try:
                        exportarsql.exportarsql(nombre_archivo)
                        print(f"\n✅ Base de datos exportada exitosamente a '{nombre_archivo}'.")
                    except Exception as e:
                        print(f"\n❌ No fue posible exportar la base de datos: {e}")
                
                funciones.espereTecla()

            case "8": # Salir del menu.

                opcion = False
                funciones.borrarPantalla()
                print(f"\n\tVolviendo al menu principal...")
                funciones.espereTecla()
                main()  # Volver a mostrar el menú pri+-ncipal de reservaciones.

                funciones.espereTecla()
            
            case _: # Opción inválida.

                funciones.borrarPantalla()
                print("\tOpción inválida, vuelva a intentarlo.")
                funciones.espereTecla()

def main(): # Procedimiento principal que inicia el programa.
    opcion = True

    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menuPrincipal()
        
        match opcion: # Match que se encarga de las opciones del menú.

            case "1": # Menu de reservaciones.
            
                mainReservaciones()

            case "2": # Menu de salas.

                mainSalas()

            case "3": # Menu de exportación.

                mainExportar()

            case "4": # Salir del programa.
                print("\n👋 ¡Gracias por usar el sistema! Hasta luego.")
                opcion=False
                funciones.espereTecla()
                sys.exit()
        
            case _: # Opción inválida.
                funciones.borrarPantalla()
                print("\n❌ Opción inválida, por favor intenta nuevamente.")
                funciones.espereTecla()
                main()

main() # Manda a llamar la función principal para iniciar el programa.