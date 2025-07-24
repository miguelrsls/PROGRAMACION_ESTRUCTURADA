"""
Crear un proyecto que permita gestionar (administrar)
peliculas. Colocar un menu de opciones para agregar, borrar
modificar, mostrar, buscar, limpiar una lista de peliculas.

Notas:

1. Utilizar funciones y mandar llamar desde otro archivo (modulo).
2. Utilizar DICT para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma) de una pelicula.
3. Implementar y utilizar una base de datos relacional en MySQL.
"""

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t .:: Gestion de Peliculas ::.\n\t1. Crear\n\t2. Borrar\n\t3. Mostrar\n\t4. Buscar\n\t5. Modificar\n\t6. Salir")
    opcion=input(f"\n\t\t Elige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case "6":
            opcion=False
            peliculas.borrarPantalla()
            print(f"\n\tTerminaste la ejecucion del sistema... Gracias...")
        case _:
            peliculas.borrarPantalla()
            print("\n\tOpcion invalida, vuelva a intentarlo.")
            peliculas.espereTecla()
            opcion=True
            