# FUNCIONES.PY - Este modulo contiene funciones auxiliares para el programa de reservaciones de salas de ensayo YOURSELF STUDIO.

def borrarPantalla(): # Procedimiento para borrar pantalla.
    import os
    os.system('cls')

def espereTecla(): # Procedimiento para esperar tecla.
    input(f"\n🚀 ... Oprima ENTER para continuar ... 🚀 ")

def menuPrincipalReservaciones(): # Funcion para nuestro menu principal de reservaciones.
    print("\n\t\t\t\t.:: YOURSELF MUSIC STUDIO ::.")
    print(f"\n\t\t\t.:: Sistema de Gestión de Reservaciones ::. \n\n\t1. Agendar 📖\
          \n\t2. Mostrar 👀\n\t3. Buscar 🔎\n\t4. Modificar ✍️ \n\t5. Eliminar 🆑\n\t6. Limpiar tabla (Reset) ❌ \n\t7. Salir 📱")
    opcion=input(f"\n\t\t 🔢 Elige una opcion (1 - 7): ")

    return opcion

def formatoBusqueda(respuesta): # Procedimiento para darle formato a la respuesta de las reservaciones.
    if len(respuesta)>0:
        print(f"-"*140)
        print(f"{'ID':<10} {'Nombre':<15} {'Genero':<15} {'Sala':<15} {'Fecha':<30} {'Duración (hrs)':<15} {'Personas':<15} {'Total a pagar':<15}")
        print(f"-"*140)
        for fila in respuesta:
                fecha_formateada = fila[4].strftime("%d %b %Y %I:%M %p")
                print(f"{fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fecha_formateada:<30} {fila[5]:<15} {fila[6]:<15} {fila[7]:<15}")
    else:
        print(f"No se encontraron reservaciones con esos datos. ")

def menuPrincipalSalas(): # Funcion para nuestro menu principal de salas.
    print("\n\t\t\t\t.:: YOURSELF MUSIC STUDIO ::.")
    print(f"\n\t\t\t.:: Sistema de Gestión de Salas ::. \n\n\t1. Modificar Capacidad ✍️\
          \n\t2. Mostrar Capacidad 👀\n\t3. Salir 👋")
    opcion=input(f"\n\t\t 🔢 Elige una opcion (1 - 3): ")

    return opcion

def menuPrincipal(): # Funcion para nuestro menu principal.
    print("\n\t\t\t\t.:: YOURSELF MUSIC STUDIO ::.")
    print(f"\n\t\t\t.:: Sistema de Gestión de Reservaciones ::. \n\n\t1. Reservaciones 📖\
          \n\t2. Salas de Ensayo 🎤\n\t3. Exportar tablas 📄\n\t4. Salir 👋")
    opcion=input(f"\n\t\t 🔢 Elige una opcion (1 - 4): ")

    return opcion

def menuExportar(): # Funcion para el menu de exportar.
    print("\n\t\t\t\t.:: YOURSELF MUSIC STUDIO ::.")
    print(f"\n\t\t\t.:: Sistema de Exportación de Datos ::. \n\n\t1. Exportar Reservaciones CSV 📖\n\n\t2. Exportar Salas CSV 📖\n\n\t3. Exportar Reservaciones Excel 📖\n\n\t4. Exportar Salas Excel 📖\n\n\t5. Exportar Reservaciones PDF 📖\n\n\t6. Exportar Salas PDF 📖\n\n\t7. Exportar Base de Datos SQL 📖\n\n\t8. Salir 👋")
    opcion=input(f"\n\t\t 🔢 Elige una opcion (1 - 8): ")

    return opcion

def calcularPrecio(horas, pago): # Función para calcular el precio de la reservación.
    try:
        horas = int(horas)
    except (ValueError, TypeError):
        raise ValueError("Horas debe ser un número entero.")

    if horas < 1:
        raise ValueError("Horas debe ser al menos 1.")

    return horas * pago
