import agenda

def main():

    datos = {}

    opcion=True

    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menuPrincipal()

        match opcion:
            case "1":
                agenda.agregarContactos(datos)
                agenda.espereTecla()
            case "2":
                agenda.mostrarContactos(datos)
                agenda.espereTecla()
            case "3":
                agenda.buscarContactos(datos)
                agenda.espereTecla()
            case "4":
                agenda.eliminarContactos(datos)
                agenda.espereTecla()
            case "5":
                agenda.modificarContactos(datos)
                agenda.espereTecla()
            case "6":
                opcion=False
                agenda.borrarPantalla()
                print(f"\n\t💾 Terminaste la ejecucion del sistema... Gracias... \n")
            case _:
                agenda.borrarPantalla()
                print("\n\t❌ Opcion invalida, vuelva a intentarlo. ")
                agenda.espereTecla()
                opcion=True

if __name__=="__main__": # Para accesibilidad.
    main()