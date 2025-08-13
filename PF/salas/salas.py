# SALAS.PY - Este modulo contiene funciones relacionadas con las salas de ensayo.

from conexionBD import conexion, cursor
import datetime
import funciones as funciones

def modificarCapacidad(nombre, capacidad): # Función para modificar la capacidad de una sala.
    try:
        # Primer paso, actualiza la capacidad de la sala en la base de datos.
        cursor.execute("UPDATE salas SET capacidad = %s WHERE nombre = %s", (capacidad, nombre))
        conexion.commit()

        # Segundo paso, verifica si se actualizó al menos una fila. (Cursor.rowcount devuelve el número de filas afectadas por la última operación).
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except:
        return False

def mostrarCapacidad(): # Funcion para mostrar la capacidad de todas las salas.
    try:
        # Primer paso, ejecuta la consulta para obtener los nombres y capacidades de las salas.
        cursor.execute("SELECT nombre, capacidad FROM salas")

        # Segundo paso, obtiene todos los resultados de la consulta y los almacena en una variable.
        salas = cursor.fetchall()
        return salas
    except:
        return []
    
def limpiarReservacionesExcedidas(nombre_sala, nueva_capacidad): # Función para eliminar reservaciones que excedan la nueva capacidad de la sala.
    try:
        # Primer paso, eliminar las reservaciones que excedan la nueva capacidad.
        cursor.execute("""
            DELETE FROM reservaciones
            WHERE sala = %s AND personas > %s
        """, (nombre_sala, nueva_capacidad))
        conexion.commit()
        return True 
    except Exception as e:
        print("❌ Error al limpiar reservaciones excedidas:", e)
        return False
