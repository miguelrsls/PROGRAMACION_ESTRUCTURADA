import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\tOprima cualquier tecla para continuar. ⏰ ")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def menuPrincipal():
    print(f"\n\t\t\t📂 .:: Sistemas de Gestion de Calificaciones ::. 📂 \n\t1. Agregar ➕\n\t2. Mostrar 👁️\n\t3. Calcular Promedio 📝\n\t4. Buscar 🔎\n\t5. Salir 🚪")
    opcion=input(f"\n\t\t🔢 Elige una opcion (1 - 5): ")
    return opcion

def agregarCalificaciones(lista):

    borrarPantalla()
    conexionBD=conectar()

    print(f"\n\t🔄 .:: Agregar Calificaciones ::. 🔄\n")
    nombre=str(input(f"\n\t🧑 Nombre del alumno: ")).upper().strip()

    calificaciones=[]

    for i in range (1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"\n\t📒 Calificacion #{i}: "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print(f"\n\t❌ Ingresa una calificacion valida (0 - 10). ")
            except ValueError:
                print(f"\n\tIngresa un valor numerico. ")

    lista.append([nombre]+calificaciones) # Nombre no es una lista, entonces se "trasnforma" con [].
    
    promedio=(calificaciones[0]+calificaciones[1]+calificaciones[2])/3

    cursor=conexionBD.cursor()

    sql="insert into calificaciones (alumno, calificacion1, calificacion2, calificacion3, promedio) values (%s, %s, %s, %s, %s)"
    val=(nombre, calificaciones[0], calificaciones[1], calificaciones[2], promedio)

    cursor.execute(sql,val)

    conexionBD.commit() # Solo se usa en INSERT, UPDATE, DELETE.

    print(f"\n\t\t💾 Accion realizada con exito. ")
 
def mostrarCalificaciones(lista):
    borrarPantalla()

    conexionBD=conectar()

    if conexionBD!=None:

        cursor=conexionBD.cursor()

        sql="select * from calificaciones"
        # No existe val, porque no tenemos valor de referencia en un select.

        cursor.execute(sql) # Ejecuta con sql y val (val no es aplicable aqui).
        registros=cursor.fetchall() # Guarda todos los valores en una lista.

        print(f"\n\t📝 .:: Mostrar las Calificaciones ::. 📝\n")
        print(f"{'Nombre 👤':<10} {'📗 Calif. 1':<15} {'📘 Calif. 2':<15} {'📙 Calif. 3':<15}")
        print(f"-"*90)

        if registros:
            for calis in registros:
                print(f"{calis[1]:<10} {calis[2]:<15} {calis[3]:<15} {calis[4]:<15}")
        else:
            print(f"\n\t❓ No hay calificaciones en el sistema. ")

def calcularPromedios(lista):
    borrarPantalla()

    conexionBD=conectar()

    if conexionBD!=None:

        cursor=conexionBD.cursor()

        sql="select * from calificaciones"
        # No existe val, porque no tenemos valor de referencia en un select.

        cursor.execute(sql) # Ejecuta con sql y val (val no es aplicable aqui).
        registros=cursor.fetchall() # Guarda todos los valores en una lista.

        suma_promedios = 0
        cantidad_alumnos = 0

        if registros:
            print(f"\n{'Alumno 👤':<10} {'📗 Promedios':<15}\n")
            print(f"-"*90)
            for calis in registros:
                promedio_individual = calis[5]  # Asumimos que el índice 5 es el promedio
                print(f"{calis[1]:<10} {promedio_individual:<15}")
                suma_promedios += promedio_individual
                cantidad_alumnos += 1

            promedio_grupal = suma_promedios / cantidad_alumnos
            print(f"\n📊 Promedio Grupal: {promedio_grupal:.2f}")
        else:
            print(f"\n\t❓ No hay calificaciones en el sistema. ")

        print(f"-"*90)
        
def buscarCalificaciones(lista):
    borrarPantalla()

    # Conectar a MySQL
    conexionBD=conectar()

    if conexionBD!=None:

        print(f"\n\t🔎 .:: Buscar Calificaciones ::. 🔎\n")
        nombre=input(f"Nombre de el alumno a buscar: ").upper().strip() # Variable de nombre para la tupla
        cursor=conexionBD.cursor()

        sql="select * from calificaciones where alumno=%s" # Comando SQL %s = Valor de tupla.
        val=(nombre,) # Si es solo una variable, debe contener una coma.

        cursor.execute(sql,val) # Ejecuta con sql y val.
        registros=cursor.fetchall() # Guarda todos los valores en una lista.

        print(f"\n{'Nombre 👤':<10} {'📗 Calif. 1':<15} {'📘 Calif. 2':<15} {'📙 Calif. 3':<15} {'📚 Promedio':<15}")
        print(f"-"*90)

        if registros:
            for calis in registros:
                print(f"{calis[1]:<10} {calis[2]:<15} {calis[3]:<15} {calis[4]:<15} {calis[5]:<15}")
        else:
            print(f"No hay peliculas registradas en este momento con ese nombre...")