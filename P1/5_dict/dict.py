"""
 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. 
  Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""

import os
os.system("clear")

paises=["México", "Brasil", "Canada", "España"]

pais1={
        "Nombre":"México",
        "Capital":"CDMX",
        "Poblacion":12000000,
        "Idioma":"Español",
        "Status":True
        }


pais2={
        "Nombre":"Brasil",
        "Capital":"Brasilia",
        "Poblacion":14000000,
        "Idioma":"Portugues",
        "Status":True
        }

pais3={
        "Nombre":"Canada",
        "Capital":"Otawua",
        "Poblacion":10000000,
        "Idioma":["Ingles", "Frances"],
        "Status":True
        }

os.system("cls")

print(pais1)

for i in pais1: # Valores = Categoria - pais1[valores] = Caracteristicas.
    print(f"{i} = {pais1[i]}")

# Agregar un atributo a un objeto.

pais1["Altitud"]=3000
for i in pais1:
    print(f"{i} = {pais1[i]}")

# Modificar un valor de un item o atributo que ya existe.

pais1.update({"Altitud":2500})
for i in pais1:
    print(f"{i} = {pais1[i]}")

# Quitar atributo de un objeto, en este caso el ultimo atributo.

pais1.popitem()
for i in pais1:
    print(f"{i} = {pais1[i]}")

# Quitar atributo de un objeto, en este caso el seleccionado.

pais1.pop("Status")
for i in pais1:
    print(f"{i} = {pais1[i]}")
