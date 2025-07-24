import mysql.connector
from mysql.connector import Error

# DICT u objeto que permita almacenar los siguientes atributos. (nombre, categoria, clasificacion, genero, idioma)

"""
pelicula={
    "Nombre":"",
    "Categoria":"",
    "Clasificacion":"",
    "Genero":"",
    "Idioma":""
}
"""

pelicula={}

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\tOprima cualquier tecla para continuar. ")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def crearPeliculas():
    
    borrarPantalla()

    # Conectar a MySQL
    conexionBD=conectar()

    if conexionBD!=None:

        print("\n\t.:: Agregar peliculas ::.\n")

        pelicula.update({"Nombre":input("Ingresa el nombre: ").upper().strip()})

        # pelicula["Nombre"]=input(f"Ingresa el nombre: ").upper().strip() // Misma manera de agregar.

        pelicula.update({"Categoria":input("Ingresa la categoria: ").upper().strip()})
        pelicula.update({"Clasificacion":input("Ingresa la clasificación: ").upper().strip()})
        pelicula.update({"Genero":input("Ingresa el genero: ").upper().strip()})
        pelicula.update({"Idioma":input("Ingresa el idioma: ").upper().strip()})

        # ---------------------------------------- MySQL a BD ---------------------------------------- #

        # Cursor
        cursor=conexionBD.cursor()

        # Comando SQL
        sql="insert into peliculas (nombre, categoria, clasificacion, genero, idioma) values (%s, %s, %s, %s, %s)" # %s = Posicion o valor a insertar con una Tupla.
        
        # Tupla
        val=(pelicula["Nombre"], pelicula["Categoria"], pelicula["Clasificacion"], pelicula["Genero"], pelicula["Idioma"])

        cursor.execute(sql,val)
        conexionBD.commit() # Solo se usa en INSERT, UPDATE, DELETE.

        print(f"\n\t\tLa operacion se realizo con exito")

def mostrarPeliculas():


    borrarPantalla()

    # Conectar a MySQL
    conexionBD=conectar()

    if conexionBD!=None:

        cursor=conexionBD.cursor()

        sql="select * from peliculas"
        # No existe val, porque no tenemos valor de referencia en un select.

        cursor.execute(sql) # Ejecuta con sql y val (val no es aplicable aqui).
        registros=cursor.fetchall() # Guarda todos los valores en una lista.

        print(f"\n\t.:: Mostrar peliculas ::.\n")
        print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
        print(f"-"*90)

        if registros:
            for pelis in registros:
                print(f"{pelis[0]:<10} {pelis[1]:<15} {pelis[2]:<15} {pelis[3]:<15} {pelis[4]:<15} {pelis[5]:<15}")
        else:
            print(f"No hay peliculas registradas en este momento...")

def buscarPeliculas():

    borrarPantalla()

    # Conectar a MySQL
    conexionBD=conectar()

    if conexionBD!=None:

        nombre=input(f"Nombre de la pelicula a buscar: ").upper().strip() # Variable de nombre para la tupla
        cursor=conexionBD.cursor()

        sql="select * from peliculas where nombre=%s" # Comando SQL %s = Valor de tupla.
        val=(nombre,) # Si es solo una variable, debe contener una coma.

        cursor.execute(sql,val) # Ejecuta con sql y val.
        registros=cursor.fetchall() # Guarda todos los valores en una lista.

        print(f"\n\t.:: Mostrar peliculas ::.\n")
        print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
        print(f"-"*90)

        if registros:
            for pelis in registros:
                print(f"{pelis[0]:<10} {pelis[1]:<15} {pelis[2]:<15} {pelis[3]:<15} {pelis[4]:<15} {pelis[5]:<15}")
        else:
            print(f"No hay peliculas registradas en este momento con ese nombre...")

def borrarPeliculas():

    borrarPantalla()

    # Conectar a MySQL
    conexionBD=conectar()

    if conexionBD!=None:

        nombre=input(f"\nNombre de la pelicula a eliminar: ").upper().strip() # Variable de nombre para la tupla

        cursor=conexionBD.cursor()

        sql="select * from peliculas where nombre=%s" # Comando SQL %s = Valor de tupla.
        val=(nombre,) # Si es solo una variable, debe contener una coma.
        cursor.execute(sql,val) # Ejecuta con sql y val.

        registros=cursor.fetchall() # Guarda todos los valores en una lista.

        print(f"\n\t.:: Mostrar peliculas ::.\n")
        print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
        print(f"-"*90)

        if registros:
            for pelis in registros:
                print(f"{pelis[0]:<10} {pelis[1]:<15} {pelis[2]:<15} {pelis[3]:<15} {pelis[4]:<15} {pelis[5]:<15}")

                resp=input(f"\n¿Deseas eliminar la pelicula {nombre}? (SI/NO:) ").lower().strip()
                if resp=="si":
                    sql="delete from peliculas where nombre=%s" # Comando SQL %s = Valor de tupla.
                    val=(nombre,) # Si es solo una variable, debe contener una coma.
                    cursor.execute(sql,val) # Ejecuta con sql y val.
                    conexionBD.commit()
                    print(f"\n\t\t¡Operacion realizada con exito!")
        else:
            print(f"No hay peliculas registradas en este momento con ese nombre...")

def modificarPeliculas():

    borrarPantalla()

    # Conexion a SQL
    conexionBD = conectar()
    if conexionBD is not None:

        # Cursor
        cursor = conexionBD.cursor()
        
        # Datos
        sql = "SELECT * FROM peliculas"
        cursor.execute(sql)
        registros = cursor.fetchall()

        print("\n\t .:: Modificar Películas ::.\n")
        resp=input(f"¿Deseas modificar una pelicula? (SI/NO) ").upper().strip()

        if resp=="SI":
            if registros:
                print(f"\n{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
                print("-" * 90)

                for fila in registros:
                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")

                try:
                    id_modificar = int(input("\nIngrese el ID de la película que desea modificar: "))
                    cursor.execute("SELECT * FROM peliculas WHERE id = %s", (id_modificar,))
                    pelicula = cursor.fetchone()

                    if pelicula:
                        print("\nEn caso de que no quieras modificar un valor, deja vacio el espacio.\n")
                        nuevo_nombre = input(f"Nombre ({pelicula[1]}): ") or pelicula[1]
                        nueva_categoria = input(f"Categoría ({pelicula[2]}): ") or pelicula[2]
                        nueva_clasificacion = input(f"Clasificación ({pelicula[3]}): ") or pelicula[3]
                        nuevo_genero = input(f"Género ({pelicula[4]}): ") or pelicula[4]
                        nuevo_idioma = input(f"Idioma ({pelicula[5]}): ") or pelicula[5]

                        sql_update = """
                            UPDATE peliculas 
                            SET nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s 
                            WHERE id=%s
                        """
                        datos = (nuevo_nombre, nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, id_modificar)
                        cursor.execute(sql_update, datos)
                        conexionBD.commit()
                        
                        print("\n\tPelícula modificada correctamente.\n")
                    else:
                        print("\n\tNo se encontró una película con ese ID.\n")
                except Exception as e:
                    print(f"\n\tOcurrió un error: {e}\n")
            else:
                print("\n\t .:: No hay películas en el Sistema ::.\n")
    else:
        print("No se ha modificado nada. ")
