from conexionBD import *
import datetime

def registrar(nombre,apellidos,email,contra):
    try:
        fecha=datetime.datetime.now()
        cursor.execute("insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)",(nombre,apellidos,email,contra,fecha))
        conexion.commit()
        return True
    except:
        return False
    
def inicio_sesion(email,contra):
    print("-")
    try:
        cursor.execute(("select*from usuarios where email=%s and password=%s"),(email,contra))
        return cursor.fetchone()
    except:
        return []
    