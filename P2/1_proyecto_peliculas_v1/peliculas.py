peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\tOprima cualquier tecla para continuar.")


# Caso 1

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar peliculas ::.\n")

    peliculas.append(input(f"Ingresa el nombre: ").upper().strip())
    print(f"\n\t\tLa operacion se realizo con exito")

# Caso 2

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar peliculas ::.\n")

    pelicula_borrar=input(f"Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
    encontro=0
    if not(pelicula_borrar in peliculas):
        print(f"\n\t\tNo se encuentra la pelicula a buscar!")
    else:
        for i in range (0, len(peliculas)):
            if pelicula_borrar==peliculas[i]:
                resp=input(f"¿Deseas borrar la pelicula (Si/No) ").lower().strip()
                if resp=="si":
                    print(f"La pelicula {pelicula_borrar} fue eliminada y se encuentra en la casilla {i+1}")
                    peliculas.remove(pelicula_borrar)
                    encontro+=1
                    print(f"\n\t\tLa operacion se realizo con exito")
                elif resp=="no":
                    print(f"La pelicula no fue eliminada")
                else:
                    print("Operacion no valida, inserte SI o NO")
                    resp=input(f"¿Deseas borrar la pelicula (Si/No) ").lower().strip()
        print(f"\n\tTenemos {encontro} pelicula(s) con este titulo")

# Caso 3

def modificarPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar peliculas ::.\n")

    pelicula_buscar=input(f"Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print(f"\n\t\tNo se encuentra la pelicula a buscar!")
    else:
        for i in range (0, len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                resp=input(f"¿Deseas actualizar la pelicula (Si/No) ").lower().strip()
                if resp=="si":
                    peliculas[i]=input(f"\nIntroduce el nuevo nombre de la pelicula: ").upper().strip()
                    encontro+=1
                    print(f"\n\t\tLa operacion se realizo con exito")

# Caso 4

def mostrarPeliculas():
    borrarPantalla()
    print(f"\n\t.:: Mostrar peliculas ::.\n")

    if len(peliculas)>0:
        for i in range(0, len(peliculas)): # Len = Longitud de una lista.
            print(f"{i+1}. {peliculas[i]}")
    else:
        print(f"No hay peliculas registradas en este momento...")

# Caso 5

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.:: Buscar pelicula ::.\n")

    pelicula_buscar=input(f"Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print(f"\n\tLa pelicula ingresada no existe en el sistema.")
    else:
        encontro=0
        for i in range(0, len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"\n\t La pelicula {pelicula_buscar} se encontro en el casillero: {i+1}")
                encontro+=1
        print(f"\n\tTenemos {encontro} pelicula(s) con este titulo")
        print(f"\n\t\tLa operacion se realizo con exito")

# Caso 6

def limpiarPeliculas():
    borrarPantalla()
    print("\n\t.:: Limpiar o borrar la lista de peliculas ::.\n")

    resp=input(f"¿Deseas borrar todas las peliculas del sistema? Si/No ").lower().strip()
    if resp=="si":
        peliculas.clear()
        print(f"\n\t\tLa operacion se realizo con exito")
    elif resp=="no":
        print("La lista no ha sido modificada")
        espereTecla()
    else:
        print(f"Operacion no valida, responda con SI o NO.")
        resp=input(f"¿Deseas borrar todas las peliculas del sistema? Si/No ").lower().strip()


