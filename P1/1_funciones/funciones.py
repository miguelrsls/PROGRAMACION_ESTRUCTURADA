"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

# 1.- Funcion que no recibe parametros y no regresa valor

def solicitarDatos1():
    nombre=input(f"Nombre: ")
    telefono=input(f"Telefono: ")
    print(f"El nombre es: {nombre} y su telefono es: {telefono}")

# 3.- Funcion que recibe parametros y no regresa valor

def solicitarDatos3(nom, tel):
    nombre=nom
    telefono=tel
    print(f"El nombre es: {nom} y su telefono es: {tel}")

# 2.- Funcion que no recibe parametros y regresa valor

def solicitarDatos2():
    nombre=input(f"Nombre: ")
    telefono=input(f"Telefono: ")
    return nombre,telefono

# 4.- Funcion que recibe parametros y regresa valor

def solicitarDatos4(nom, tel):
    nombre=nom
    telefono=tel
    return nombre,telefono

# Invocar las funciones

# Caso 1

solicitarDatos1()

# Caso 2

nombre,telefono=solicitarDatos2()
print(f"\n\t\tCaso 2\n\t\tAgenda telefonica: \n\n\tNombre: {nombre}\n\tTelefono: {telefono}")

# Caso 3

nombre=input(f"\n\t\tCaso 3 \n\t\tTu nombre: ")
telefono=input(f"Tu telefono: ")
solicitarDatos3(nombre,telefono)

# Caso 4

nombre=input(f"\n\t\tCaso2 \n\t\tTu nombre: ")
telefono=input(f"Tu telefono: ")
nombre,telefono=solicitarDatos4(nombre,telefono)
print(f"\n\t\tCaso 4 \n\t\tAgenda telefonica: \n\n\tNombre: {nombre}\n\tTelefono: {telefono}")