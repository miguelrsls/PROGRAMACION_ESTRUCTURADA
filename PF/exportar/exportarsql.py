# EXPORTACIONBD.PY - Módulo para exportar la base de datos completa a un archivo SQL.

from conexionBD import conexion, cursor

def exportarsql(nombre_archivo, database="bd_reservaciones"): # Funcion para exportar la base de datos en formato SQL.
    try:
        if conexion is None or not conexion.is_connected():
            raise RuntimeError("❌ No hay conexión activa con la base de datos.")

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"-- Backup de la base de datos `{database}`\n")
            archivo.write(f"-- Generado desde Python\n\n")
            archivo.write(f"CREATE DATABASE IF NOT EXISTS `{database}`;\nUSE `{database}`;\n\n")

            # 1. Obtener todas las tablas
            cursor.execute("SHOW TABLES;")
            tablas = [t[0] for t in cursor.fetchall()]

            for tabla in tablas:
                archivo.write(f"-- ----------------------------\n")
                archivo.write(f"-- Estructura de la tabla `{tabla}`\n")
                archivo.write(f"-- ----------------------------\n\n")

                # 2. Estructura de la tabla
                cursor.execute(f"SHOW CREATE TABLE `{tabla}`;")
                create_stmt = cursor.fetchone()[1]
                archivo.write(f"{create_stmt};\n\n")

                # 3. Datos de la tabla
                cursor.execute(f"SELECT * FROM `{tabla}`;")
                filas = cursor.fetchall()
                if filas:
                    columnas = [desc[0] for desc in cursor.description]
                    archivo.write(f"-- Datos de la tabla `{tabla}`\n")
                    for fila in filas:
                        valores = []
                        for valor in fila:
                            if valor is None:
                                valores.append("NULL")
                            elif isinstance(valor, str):
                                valores.append("'" + valor.replace("'", "''") + "'")
                            else:
                                valores.append(str(valor))
                        archivo.write(f"INSERT INTO `{tabla}` ({', '.join(columnas)}) VALUES ({', '.join(valores)});\n")
                    archivo.write("\n")

        return True

    except Exception as e:
        print(f"❌ Error al exportar: {e}")
        return False
