print ("BIENVENIDO")
print ("Este es un generador de contraseña, debe proporcionar el tamaño y el caracter de su preferencia")
print ("_____________________________________________________________________________________________________________________________")
longitud = int(input("Digite la logitus de la contraseña: "))

while True:
        print ("--------------------------------------------------------")
        print ("escoge el tipo de caracter que quiere incluir")
        print ("    0. Incluir Mayúscula")
        print ("    1. Incluir Minúsculas ")
        print ("    2. Incluir Caracteres Alfanúmericos")
        print ("    3. Inluir Símbolos")
        print ("    4. Salir")


        try:
            opc = int(input("Elige una de las opciones disponibles: "))

            if opc == 0:
                print("")
            elif opc == 1:
                print("hola 1")
            elif opc == 2:
                 print("hola 2")
            elif opc == 3:
                 print("hola 3")
            elif opc == 4:
                print("¡hasta pronto!")
                break

        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")