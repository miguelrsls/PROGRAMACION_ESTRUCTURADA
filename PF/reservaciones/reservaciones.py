# RESERVACIONES.PY - Este modulo contiene funciones para manejar las reservaciones de salas de ensayo en el programa YOURSELF STUDIO.

from conexionBD import conexion, cursor
import datetime
import funciones as funciones

def agregarReservaciones(datos, fecha): # Funcion para agregar una nueva reservación.
    try:
        # Primer paso, verificar si la sala existe y obtener su ID.
        cursor.execute("SELECT sala_id FROM salas WHERE nombre = %s", (datos["Sala"],))
        resultado = cursor.fetchone()
        if resultado is None:
            print("❌ No se encontró la sala especificada en la base de datos.")
            return False
        sala_id = resultado[0]

        # Segundo paso, verificar la capacidad de la sala y la ocupación actual.
        cursor.execute("SELECT capacidad FROM salas WHERE sala_id = %s", (sala_id,))
        row = cursor.fetchone()
        capacidad_maxima = row[0] if row else None

        cursor.execute("""
            SELECT SUM(personas) FROM reservaciones
            WHERE sala = %s AND DATE(fecha) = DATE(%s)
        """, (sala_id, fecha))
        ocupacion_actual = cursor.fetchone()[0] or 0

        # Tercer paso, verificar si hay suficiente capacidad.
        personas_reserva = int(datos.get("Personas", 1))

        if capacidad_maxima is not None and (ocupacion_actual + personas_reserva) > capacidad_maxima:
            print("\n❌ No hay cupo suficiente para esa sala en la fecha indicada.")
            return False
        
        # Cuarto paso, insertar la nueva reservación.
        cursor.execute("""
            INSERT INTO reservaciones (nombre, genero, sala, fecha, duracion, personas, pago)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            datos["Nombre"],
            datos["Genero"],
            sala_id,
            fecha,
            datos["Duracion"],
            personas_reserva,
            datos.get("Pago", 0)
        ))
        conexion.commit()
        return True
    except Exception as e:
        print("\n❌ Error al guardar la reservación:", e)
        return False

def mostrarReservaciones(): # Funcion para mostrar todas las reservaciones.
    try:
        # Primer paso, consultar para obtener todas las reservaciones con sus detalles.
        cursor.execute("""
            SELECT r.id, r.nombre, r.genero, s.nombre as sala, r.fecha, r.duracion, r.personas, r.pago
            FROM reservaciones r
            LEFT JOIN salas s ON r.sala = s.sala_id
            ORDER BY r.fecha
        """)
        return cursor.fetchall()
    except Exception as e:
        print("❌ Error al obtener reservaciones:", e)
        return []

def buscarReservaciones(id, nombre): # Funcion para buscar reservaciones por ID o nombre.
    try:
        # Primer paso, verificar si se busca por ID o nombre.
        if id and id != "0":
            cursor.execute("""
                SELECT r.id, r.nombre, r.genero, s.nombre as sala, r.fecha, r.duracion, r.personas, r.pago
                FROM reservaciones r LEFT JOIN salas s ON r.sala = s.sala_id
                WHERE r.id = %s
            """, (id,))
        # Segundo paso, buscar por nombre si no se proporciona un ID.
        else:
            cursor.execute("""
                SELECT r.id, r.nombre, r.genero, s.nombre as sala, r.fecha, r.duracion, r.personas, r.pago
                FROM reservaciones r LEFT JOIN salas s ON r.sala = s.sala_id
                WHERE r.nombre = %s
            """, (nombre,))
        return cursor.fetchall()
    except Exception as e:
        print("❌ Error al buscar reservaciones:", e)
        return []

def eliminarReservaciones(id): # Funcion para eliminar una reservación.

    try:
        # Primer paso, verificar si existe la reservación.
        cursor.execute("SELECT * FROM reservaciones WHERE id = %s", (id,))
        reservacion_actual = cursor.fetchone()
        if reservacion_actual is None:
            print("❌ No se encontró una reservación con ese ID.")
            return False
        # Segundo paso, eliminar la reservación.
        cursor.execute("DELETE FROM reservaciones WHERE id = %s", (id,))
        conexion.commit()
        return True
    except Exception as e:
        print("❌ Error al eliminar la reservación:", e)
        return False
    
def obtenercapacidadSala(sala): # Funcion para obtener la capacidad de una sala.

    try:
        cursor.execute("SELECT capacidad FROM salas WHERE nombre = %s", (sala,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            print("❌ No se encontró la sala especificada.")
            return None
    except Exception as e:
        print("❌ Error al obtener la capacidad de la sala:", e)
        return None
    
def obtenerReservacionPorID(id_reservacion): # Funcion para obtener una reservación por su ID.
    try:
        # Primer paso, verificar si la reservación existe.
        cursor.execute("SELECT * FROM reservaciones WHERE id = %s", (id_reservacion,))
        return cursor.fetchone()
    except Exception as e:
        print(f"❌ Error al obtener la reservación: {e}")
        return None

def modificarReservacion(id, nuevos_datos, nueva_fecha): # Funcion para modificar una reservación existente.
    try:
        # Primer paso, verificar si la reservación existe.
        cursor.execute("SELECT * FROM reservaciones WHERE id = %s", (id,))
        reservacion_actual = cursor.fetchone()
        if reservacion_actual is None:
            print("❌ No se encontró una reservación con ese ID.")
            return False
        
        # Segundo paso, actualizar los datos de la reservación.
        cursor.execute("""
            UPDATE reservaciones
            SET nombre = %s, genero = %s, sala = (SELECT sala_id FROM salas WHERE nombre = %s), fecha = %s, duracion = %s, personas = %s, pago = %s
            WHERE id = %s
        """, (  
            nuevos_datos["Nombre"],
            nuevos_datos["Genero"],
            nuevos_datos["Sala"],
            nueva_fecha,
            nuevos_datos["Duracion"],
            nuevos_datos["Personas"],
            nuevos_datos["Pago"],
            id
        ))
        conexion.commit()
        return True
    except Exception as e:
        print("❌ Error al modificar la reservación:", e)
        return False

def limpiarTablaReservaciones(): # Funcion para limpiar la tabla de reservaciones.
    try:
        # Primer paso, eliminar todas las reservaciones.
        cursor.execute("DELETE FROM reservaciones")
        conexion.commit()
        return True
    except Exception as e:
        print("❌ Error al limpiar la tabla de reservaciones:", e)
        return False
