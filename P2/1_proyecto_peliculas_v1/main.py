"""
Crear un proyecto que permita gestionar (administrar)
peliculas. Colocar un menu de opciones para agregar, borrar
modificar, mostrar, buscar, limpiar una lista de peliculas.

Notas:

1. Utilizar funciones y mandar llamar desde otro archivo (modulo).
2. Utilizar listas para almacenar los nombres de peliculas.
"""

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t .:: Gestion de Peliculas ::.\n\t1. Agregar\n\t2. Borrar\n\t3. Modificar\n\t4. Mostrar\n\t5. Buscar\n\t6. Limpiar\n\t7. Salir")
    opcion=input(f"\n\t\t Elige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.espereTecla()
        case "7":
            opcion=False
            peliculas.borrarPantalla()
            print(f"\n\tTerminaste la ejecucion del sistema... Gracias...")
        case _:
            peliculas.borrarPantalla()
            print("\n\tOpcion invalida, vuelva a intentarlo.")
            peliculas.espereTecla()
            opcion=True
            