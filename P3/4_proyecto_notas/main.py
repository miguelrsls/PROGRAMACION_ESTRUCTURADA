import funciones
import conexionBD
from notas import nota
from usuarios import usuario
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..\n")
            nombre=input("¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("¿Cuales son tus apellidos?: ").upper().strip()
            email=input("Ingresa tu email: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\nSe registro el usuario {nombre} {apellidos} correctamente. ")
            else:
                print(f"\nNo fue posible registrar el usuario en este momento, intentelo mas tarde. ")
            funciones.esperarTecla()

        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. \n")     
            email=input("Ingresa tu E-mail: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuario=usuario.inicio_sesion(email,password)
            if len(lista_usuario)>0:
                menu_notas(lista_usuario[0],lista_usuario[1],lista_usuario[2])
            else:
                print("Verifique su usuario. ")

            #menu_notas(19,"Dago","Fiscal")
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema. ")
            opcion=False
            funciones.esperarTecla()  
        
        else:
            print("Opcion no valida. ")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n .:: Crear Nota ::. \n")
            titulo=input("Titulo: ")
            descripcion=input("Descripción: ")

            #Agregar codigo

            respuesta=nota.crear(usuario_id,titulo,descripcion)
            if respuesta:
                print(f"La nota '{titulo}' se ha creado con exito. ")
            else:
                print(f"No ha sido posible crear la nota, intentelo mas tarde. ")

            funciones.esperarTecla()    
        
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()

            #Agregar codigo 
            
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostar las Notas")
                print(f"-"*80)
                print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<15} {'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10} {fila[2]:<15} {fila[3]:<15} {fila[4]}")
            else:
                print(f"No hay notas para este usuario, intentelo mas tarde. ")
            print(f"-"*80)

            funciones.esperarTecla()
        
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()

            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostar las Notas")
                print(f"-"*80)
                print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<15} {'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10} {fila[2]:<15} {fila[3]:<15} {fila[4]}")
            else:
                print(f"No hay notas para este usuario, intentelo mas tarde. ")
            print(f"-"*80)

            resp=input(f"\n¿Deseas modificar alguna nota? (SI/NO) ").lower().strip()
            if resp=="si":
                print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::.")
                id = input("\nID de la nota a actualizar: ")
                titulo = input("\nNuevo título: ")
                descripcion = input("Nueva descripción: ")
                        #Agregar codigo
                respuesta=nota.cambiar(id,titulo,descripcion)
                if respuesta:
                    print(f"La nota '{titulo}' se ha modificado con exito. ")
                else:
                    print(f"No se ha modificado la nota para este usuario, intentelo mas tarde. ")
            else:
                print(f"No se ha modificado la nota, intentelo mas tarde. ")
            funciones.esperarTecla()      
        
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostar las Notas")
                print(f"-"*80)
                print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<15} {'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10} {fila[2]:<15} {fila[3]:<15} {fila[4]}")
            else:
                print(f"No hay notas para este usuario, intentelo mas tarde. ")
            print(f"-"*80)

            resp=input(f"\n¿Deseas eliminar alguna nota? (SI/NO) ").lower().strip()
            if resp=="si":
                print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
                id = input("ID de la nota a eliminar: ")
                respuesta=nota.borrar(id)
                if respuesta:
                    print(f"Se borro la nota '{id}' con exito. ")
                else:
                    print(f"No ha sido posible borrar la nota, intentelo mas tarde. ")
            else:
                print(f"No se ha eliminado ninguna nota, intentelo mas tarde. ")

            funciones.esperarTecla()    
        
        elif opcion == '5' or opcion=="BUSCAR":
            funciones.borrarPantalla()
            print(f"\n\t.:: Buscar Notas ::.")
            resp=input(f"\n¿Deseas buscar una nota? (SI/NO) ").upper().strip()
            if resp=="SI":
                id=input(f"Ingrese el ID de la nota que desea buscar: ")
                respuesta=nota.buscar(id)
                if respuesta:
                    print(f"\n\tEsta es la nota {id}: ")
                    print(f"-"*80)
                    print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<15} {'Fecha':<15}")
                    print(f"-"*80)
                    print(f"{respuesta[0]:<10} {respuesta[2]:<15} {respuesta[3]:<15} {respuesta[4]}")
                else:
                    print(f"No se ha encontrado una nota con esta ID, intentelo de nuevo. ")
            else:
                print(f"No se ha realizado ninguna busqueda.")
                
            funciones.esperarTecla() 

        elif opcion == '6' or opcion=="SALIR":
            break
        
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


