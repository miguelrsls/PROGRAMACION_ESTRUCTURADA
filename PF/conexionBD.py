# CONEXIONBD.PY - Modulo para la conexión a la base de datos del programa de reservaciones de salas de ensayo YOURSELF STUDIO.

import mysql.connector

conexion = None
cursor = None

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_reservaciones"
    )
    cursor = conexion.cursor(buffered=True) # buffered=True Permite que se pueda usar el cursosr varias veces sin tener que volver a ejecutar la consulta.
except mysql.connector.Error as err:
    print(f"❌ Error de conexión: {err}") # Mensaje de error que nos muestra si hay un problema al conectar a la base de datos.
