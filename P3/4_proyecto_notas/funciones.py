def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\tOprima cualquier tecla para continuar... ")

def menu_usurios():
   print("\n \t.:: Sistema de Gestión de Notas ::.. \n\n1.- Registro  \n2.- Login \n3.- Salir ")
   opcion=input("\t\t Elige una opción: ").upper().strip() 
   return opcion

def menu_notas():
   print("\n \t .::  Menu Notas ::. \n\n1.- Crear \n2.- Mostrar \n3.- Cambiar \n4.- Eliminar \n5.- Buscar \n6.- Salir""")
   opcion = input("\t\t Elige una opción: ").upper().strip()
   return opcion   