# EXPORTAR.PY - Este modulo contiene funciones para exportar datos de reservaciones a diferentes formatos.

import pandas as pd # Biblioteca para manejo de datos y exportación.
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle # Biblioteca para crear PDFs.
from reportlab.lib import colors # Biblioteca para colores en PDFs.
from conexionBD import conexion # Importamos la conexión a la base de datos.

def exportar_reservaciones_csv(nombre_archivo): # Funcion para exportar reservaciones a CSV.
    try:
        df = pd.read_sql("SELECT * FROM reservaciones", conexion) # Primero paso, leemos los datos de la tabla reservaciones.
        df.to_csv(nombre_archivo, index=False) # Segundo paso, exportamos los datos a un archivo CSV sin incluir el índice.
        return True
    except:
        return False

def exportar_salas_csv(nombre_archivo): # Funcion para exportar salas a CSV.
    try:
        df = pd.read_sql("SELECT * FROM reservaciones", conexion)
        df.to_csv(nombre_archivo, index=False)
        return True
    except:
        return False

def exportar_reservaciones_excel(nombre_archivo): # Funcion para exportar reservaciones a Excel.
    try:
        df = pd.read_sql("SELECT * FROM reservaciones", conexion)
        df.to_excel(nombre_archivo, index=False)
        return True
    except:
        return False

def exportar_salas_excel(nombre_archivo): # Funcion para exportar salas a Excel.
    try:
        df = pd.read_sql("SELECT * FROM reservaciones", conexion)
        df.to_excel(nombre_archivo, index=False)
        return True
    except:
        return False

def exportar_reservaciones_pdf(nombre_archivo): # Funcion para exportar reservaciones a PDF.
    try:
        df = pd.read_sql("SELECT * FROM reservaciones", conexion)

        data = [df.columns.tolist()] + df.values.tolist()
        pdf = SimpleDocTemplate(nombre_archivo)
        tabla = Table(data)

        estilo = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
        ])

        tabla.setStyle(estilo)
        pdf.build([tabla])
        return True
    except:
        return False

def exportar_salas_pdf(nombre_archivo): # Funcion para exportar salas a PDF.
    try:
        df = pd.read_sql("SELECT * FROM salas", conexion)

        data = [df.columns.tolist()] + df.values.tolist()
        pdf = SimpleDocTemplate(nombre_archivo)
        tabla = Table(data)

        estilo = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
        ])

        tabla.setStyle(estilo)
        pdf.build([tabla])
        return True
    except:
        return False
