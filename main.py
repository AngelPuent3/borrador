def main():
    print("Bienvenidos")
    print("1.Contestar encuesta\n2.-Diagrama tallo/hoja\n3.Ver encuesta\n4.Salir")
    try:
        opcion = int(input("Ingrese una opcion: "))
        while opcion != 4:
            if opcion==1:
                print("Contestar encuesta")
            elif opcion==2:
                print("Diagrama tallo/hoja")
            elif opcion==3:
                print("Ver encuesta")
            else:
                print("Opcion incorrecta debe ser un numero entero entre 1-3")
                return main()
    except: Exception 
    print("Opcion incorrecta debe ser un numero entero entre 1-3")
    f=input("Enter para continuar >>>")
    return main()
    

main()

            