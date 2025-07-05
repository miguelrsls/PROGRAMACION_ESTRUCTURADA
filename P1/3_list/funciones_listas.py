"""

List (Array)
Son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace un indice numerico.

Nota: Sus valores si son modificables.

La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

import os
os.system("cls")

# Funciones mas comunes en las listas.

paises=["Mexico","España","Brasil","Canada"] # Cadenas
numeros=[23,45,8,24] # Enteros
varios=["Hola", 3.1416, 33, True] # Combinado

# Imprimir el contenido de una lista.

print(f"Paises: {paises}")
print(f"Numeros: {numeros}")
print(f"Varios: {varios}")

# Recorrer la lista.

# Primera forma.
for i in paises:
    print(f"- {i}")

# Segunda forma.
for i in range(0,len(paises)):
    print(f"- {paises[i]}")

# Ordenar elementos de una lista.

paises.sort()
print (paises)

numeros.sort()
print (numeros)

# Varios no se puede ordenar debido a que son tipos de datos distintos.

# Darle la vuelta a una lista.

paises.reverse()
print(paises)

numeros.reverse()
print(numeros)

varios.reverse()
print(varios)

# Agregar, insertar, añadir un elemento a una lista.

# Primera forma.
paises.append("Honduras")
print(paises)

# Segunda forma.
paises.insert(1,"Honduras") # Permite elegir el lugar en donde se ingresara la cadena.
print(paises)

paises.sort()
print(paises)

# Eliminar, borrar, suprimir, un elemento de una lista.

# Primer forma.
paises.pop(4) # Elimina una posicion especifca.
print(paises)

# Segunda forma.
paises.remove("Honduras") # Elimina el primer valor que encuentre con el mismo contenido.
print(paises)

# Buscar un elemento dentro de la lista.

print(paises)

print("Brasil" in paises) # Regresa TRUE o FALSE dependiendo si el valor esta en la lista.

# Contar el numero de veces que aparece un elemento dentro de una lista.

print(numeros)
print(numeros.count(23))

numeros.append(23)
print(numeros.count(23))

# Conocer la posicion o indice en el que se encuentra un elemento de la lista.

paises.reverse()
paises.append("Canada")
print(paises)

print(f"El valor de canada lo encontro en: {paises.index("Canada")}")

# Unir contenido de una lista dentro de otra.

print(numeros)
numeros2=[100,200]

print(numeros2)

# Crear a partir de las listas de numeros 1 y 2 una resultante y mostrar el contenido ordenado descendentemente.

os.system("cls")

numeros.extend(numeros2) # Extend funciona para unir listas.
numeros.sort()
numeros.reverse()
print(numeros)