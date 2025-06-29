def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\tOprima cualquier tecla para continuar. ⏰ ")

def menuPrincipal():
    print(f"\n\t\t\t📂 .:: Sistemas de Gestion de Calificaciones ::. 📂 \n\t1. Agregar ➕\n\t2. Mostrar 👁️\n\t3. Calcular Promedio 📝\n\t4. Buscar 🔎\n\t5. Salir 🚪")
    opcion=input(f"\n\t\t🔢 Elige una opcion (1 - 5): ")
    return opcion

def agregarCalificaciones(lista):
    borrarPantalla()
    print(f"\n\t🔄 .:: Agregar Calificaciones ::. 🔄\n")
    nombre=input(f"\n\t🧑 Nombre del alumno: ").upper().strip()

    calificaciones=[]

    for i in range (1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"\n\t📒 Calificacion #{i}: "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print(f"\n\t❌ Ingresa una calificacion valida (0 - 10). ")
            except ValueError:
                print(f"\n\tIngresa un valor numerico. ")

    lista.append([nombre]+calificaciones) # Nombre no es una lista, entonces se "trasnforma" con [].
    print(f"\n\t\t💾 Accion realizada con exito. ")
 
def mostrarCalificaciones(lista):
    borrarPantalla()
    print(f"\n\t📝 .:: Mostrar las Calificaciones ::. 📝\n")
    if len(lista)>0:
        print(f"{'Nombre 👤':<13} {'📗 Calif. 1':<8} {'📘 Calif. 2':<8} {'📙 Calif. 3':<8}")
        print("-"*50)
        for fila in lista:
            print(f"{fila[0]:<15} {fila[1]:<10}  {fila[2]:<10}  {fila[3]:<10}")
        print("-"*50)

        cuantos=len(lista)
        print(f"\n👥 Son {cuantos} alumno(s). ")
    else:
        print(f"\n\t❓ No hay calificaciones en el sistema. ")

def calcularPromedios(lista):
    borrarPantalla()
    print(f"\n\t👤 .:: Promedio de los Alumnos ::. 👤\n")
    if len(lista)>0:
        print(f"{'Nombre 👤':<15} {'Promedio 📖':<10}")
        print("-"*40)
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            #promedio=(fila[1]+fila[2]+fila[3])/3
            promedio=sum(fila[1:])/3
            print(f"{nombre:<15} {promedio:<.2f}")
            promedio_grupal+=promedio

        print("-"*40)
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio del grupo es: {promedio_grupal:.2f} 👥")
    else:
        print(f"\n\t❓ No hay calificaciones en el sistema. ")

def buscarCalificaciones(lista):
    borrarPantalla()
    print(f"\n\t🔎 .:: Buscar Calificaciones ::. 🔎\n")
    print(f"\n\tmy dih creamy as shi🥀🥀")