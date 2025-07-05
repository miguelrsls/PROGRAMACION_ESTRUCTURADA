"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

import os
os.system("cls")

paises=["México", "Brasil", "España", "Canada", "Canada"] # Lista
print(paises)

paises={"México", "Brasil", "España", "Canada", "Canada"} # Set
print(paises)

varios={True, "UTD", 33, 3.14}
print(varios)

# Funciones u Operaciones

paises.add("Mexico")
print(paises)

paises.pop() # Elimina cualquiera.
print(paises)

#paises.remove("Mexico") # Elimina algo especifico.
#print(paises)

'''
Ejemplo: Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla
los emails sin duplicados.
'''

'''
# Solucion 1
correosset={""}
flag="SI"

while flag=="SI":
  correos=(input(f"¿Cual es tu correo electronico? "))
  correosset.add(correos)
  flag=(input(f"¿Deseas agregar otro correo? ")).upper()

print(correosset)
'''

# Solucion 2
os.system("cls")

correosset=[]
flag="SI"

while flag=="SI":
  correosset.append(input(f"¿Cual es tu correo electronico? "))
  flag=(input(f"¿Deseas agregar otro correo? ")).upper()

print(correosset)

emails_set=set(correosset) # Quitar duplicados de una lista.
print(emails_set)

correosset=list(emails_set) # Con el set limpio de duplicados, ahora pasa a ser una lista.
print(correosset)