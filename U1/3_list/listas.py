import os

os.system("cls")

# Ejemplo 1: Crear una lista de numeros e imprimir el contenido.

ejemplo1=[1,2,3,4,5]
print(f"La lista numerica se conforma de los siguientes valores: {ejemplo1}")

# Ejemplo 2: Crear una lista de palabaras y posteriormente buscar la coincidencia de una palabra.

ejemplo2=["Hola","Adios","Nos vemos","Como estas","Hola","Hola","Adios"]
ejemplocontadorhola=(ejemplo2.count("Hola"))
print(f"La cantidad de veces que aparece la palabra Hola en la lista es la siguiente: {ejemplocontadorhola}")

# Ejmplo 3: Añadir elementos a la lista.

ejemplo3=[1,2,3,4,5]
print(f"La lista basica es: {ejemplo3}")

ejemplo3.append(6)
print(f"La lista con valores agregados es: {ejemplo3}")

# Ejemplo 4: Crear una multidimensional que permita almacenar el nombre y telefono de una agenda.

ejemplo4=True
nombrelista=[]
telefonolista=[]
nombre=""
telefono=0
repetidor=""
decision=""

while ejemplo4:
    nombre=input(f"Ingrese su nombre: ")
    nombrelista.append(nombre)
    telefono=input(f"Ingrese su numero telefonico: ")
    telefonolista.append(telefono)
    repetidor=input(f"Deseas repetir el proceso? ").upper()
    if repetidor=="SI":
        os.system("cls")
        ejemplo4=True
    if repetidor=="NO":
        ejemplo4=False

decision=input(f"Deseas ver la agenda? ").upper()

if decision=="SI": 
    print(f"La agenda de nombres es: {nombrelista}")
    print(f"La agenda de numeros es: {telefonolista}")
if decision=="NO":
    print(f"Eso ha sido todo...")