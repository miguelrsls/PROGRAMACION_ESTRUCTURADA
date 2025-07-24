import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\t⏰ Oprima cualquier tecla para continuar. ")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def menuPrincipal():
    print(f"\n\t\t\t👥 .:: Sistemas de Gestion de Agenda de Contactos ::. 👥 \n\n\t1️⃣  Agregar Contacto\n\t2️⃣  Mostrar todos los contactos\n\t3️⃣  Buscar contacto por nombre\n\t4️⃣  Eliminar contactos\n\t5️⃣  Modificar contactos\n\t6️⃣  Salir\n\t")
    opcion=input(f"\t\t🔢 Elige una opcion (1 - 6): ")
    return opcion

def agregarContactos(agenda):
    
    borrarPantalla()
    conexionBD=conectar()

    print(f"\n\t👥 .:: Agregar Contactos ::. 👥\n")

    nombre=str(input(f"🎷 Nombre: ")).upper().strip()

    if nombre in agenda:
        print(f"❌ Este contacto ya existe, intentelo de nuevo. ")
    else:
        tel=int(input(f"\n📱 Telefono: "))
        email=str(input(f"\n📨 E-mail: ")).lower().strip()
        agenda[nombre]=[tel, email]
        print(f"\n✅ Accion realizada con exito. \n")

    cursor=conexionBD.cursor()
    
    sql="insert into agenda (nombre, telefono, email) values (%s, %s, %s)"
    val=(nombre, agenda[nombre][0], agenda[nombre][1]) # 0 = telefono - 1 = email
    
    cursor.execute(sql,val)
    conexionBD.commit() # Solo se usa en INSERT, UPDATE, DELETE.

def mostrarContactos(agenda):

    borrarPantalla()
    conexionBD=conectar()

    cursor=conexionBD.cursor()

    sql="select * from agenda"
    # No existe val, porque no tenemos valor de referencia en un select.

    cursor.execute(sql) # Ejecuta con sql y val (val no es aplicable aqui).
    registros=cursor.fetchall() # Guarda todos los valores en una lista.
    
    print(f"\n\t👁️  .:: Mostrar Contactos ::.  👁️\n")

    print(f"{'Nombre 👤':<10} {'📱 Telefono':<15} {'📨 E-mail':<15}")
    print(f"-"*90)

    if registros:
        for agendas in registros:
            print(f"{agendas[1]:<10} {agendas[2]:<15} {agendas[3]:<15}")
    else:
        print(f"\n\t❓ No hay contactos en el sistema. ")

def buscarContactos(agenda):

    borrarPantalla()

    # Conectar a MySQL
    conexionBD=conectar()

    if conexionBD!=None:

        print(f"\n\t🔎 .:: Buscar Contacto ::. 🔎\n")
        nombre=input(f"Nombre de el contacto a buscar: ").upper().strip() # Variable de nombre para la tupla
        cursor=conexionBD.cursor()

        sql="select * from agenda where nombre=%s" # Comando SQL %s = Valor de tupla.
        val=(nombre,) # Si es solo una variable, debe contener una coma.

        cursor.execute(sql,val) # Ejecuta con sql y val.
        registros=cursor.fetchall() # Guarda todos los valores en una lista.

        print(f"\n{'Nombre 👤':<10} {'📱 Telefono':<15} {'📨 E-mail':<15}")
        print(f"-"*90)

        if registros:
            for agendas in registros:
                print(f"{agendas[1]:<10} {agendas[2]:<15} {agendas[3]:<15}")
        else:
            print(f"\n\t❓ No hay contactos en el sistema. ")

def eliminarContactos(agenda):

    borrarPantalla()

    # Conectar a MySQL
    conexionBD=conectar()

    if conexionBD!=None:

        print(f"\n\t❌  .:: Eliminar Contactos ::.  ❌\n")

        nombre=input(f"Nombre de el contacto a eliminar: ").upper().strip() # Variable de nombre para la tupla

        cursor=conexionBD.cursor()

        sql="select * from agenda where nombre=%s" # Comando SQL %s = Valor de tupla.
        val=(nombre,) # Si es solo una variable, debe contener una coma.
        cursor.execute(sql,val) # Ejecuta con sql y val.

        registros=cursor.fetchall() # Guarda todos los valores en una lista.

        print(f"\n{'Nombre 👤':<10} {'📱 Telefono':<15} {'📨 E-mail':<15}")
        print(f"-"*90)

        if registros:
            for agendas in registros:
                print(f"{agendas[1]:<10} {agendas[2]:<15} {agendas[3]:<15}")

                resp=input(f"\n¿Deseas eliminar el contacto {nombre}? (SI/NO:) ").lower().strip()
                if resp=="si":
                    sql="delete from agenda where nombre=%s" # Comando SQL %s = Valor de tupla.
                    val=(nombre,) # Si es solo una variable, debe contener una coma.
                    cursor.execute(sql,val) # Ejecuta con sql y val.
                    conexionBD.commit()
                    print(f"\n\t\t¡Operacion realizada con exito!")
        else:
            print(f"No hay peliculas registradas en este momento con ese nombre...")

def modificarContactos(agenda):

    borrarPantalla()

    # Conexion a SQL
    conexionBD = conectar()
    if conexionBD!=None:

        cursor = conexionBD.cursor()
        
        sql = "select * from agenda"
        cursor.execute(sql)
        registros = cursor.fetchall()

        print(f"\n\t✍️  .:: Modificar Contactos ::.  ✍️\n")
        resp=input(f"¿Deseas modificar un contacto? (SI/NO) ").upper().strip()

        if resp=="SI":
            if registros:
                print(f"\n{'Nombre 👤':<10} {'📱 Telefono':<15} {'📨 E-mail':<15}")
                print(f"-"*90)

                for agendas in registros:
                    print(f"{agendas[1]:<10} {agendas[2]:<15} {agendas[3]:<15}")

                try:
                    id_modificar = str(input("\nIngrese el nombre de el contacto que desea modificar: ")).upper().strip()
                   
                    id_valor = (id_modificar,)
                    id_sql = ("SELECT * FROM agenda WHERE nombre=%s")

                    cursor.execute(id_sql, id_valor)
                    agenda = cursor.fetchone()

                    if agenda:
                        print("\nEn caso de que no quieras modificar un valor, deja vacio el espacio. (Recomendacion: Usa solo numeros en el telefono) \n")

                        nuevo_nombre = (input(f"Nombre: ")).upper().strip() or agendas[1]
                        nuevo_telefono = (input(f"Telefono: ")) or agendas[2]
                        nuevo_email = (input(f"E-mail: ")).lower().strip() or agendas[3]

                        sql_update = """
                            update agenda 
                            set nombre=%s, telefono=%s, email=%s
                            where nombre=%s
                        """
                        datos = (nuevo_nombre, nuevo_telefono, nuevo_email, id_modificar)
                        cursor.execute(sql_update, datos)
                        conexionBD.commit()
                        
                        print(f"\n✅ Accion realizada con exito. \n")
                    else:
                        print("\n\t❌ No se encontró ningun contacto con ese nombre.\n")
                except Exception as e:
                    print(f"\n\t❌ Ocurrió un error: {e}\n")
            else:
                print(f"❌ Este contacto no existe. ")
    else:
        print(f"\n❌ No se realizo ninguna accion, intente nuevamente. ")