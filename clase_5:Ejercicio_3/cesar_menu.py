from cesar_modulo import encriptar_cesar, desncriptar_cesar 

def mostrar_menu():
    print("\n******* Cifrado Cesar *******")
    print("\nOpciones: ")
    print("\n1) Encriptar texto")
    print("2) Desencriptar texto")
    print("0) Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElija una opción: ")

        if opcion == "0":
            print("Hasta Luego!")
            break

        elif opcion == "1":
            texto = input("Ingrese el texto a encriptar: ")
            n = int(input("Ingrese el desplazamiento: "))
            resultado = encriptar_cesar(texto, n)
            print("===> Texto encriptado:", resultado)

        elif opcion == "2":
            texto = input("Ingrese el texto encriptado: ")
            n = int(input("Ingrese el desplazamiento: "))
            resultado = desncriptar_cesar(texto, n)
            print("===> Texto original:", resultado)


        else:
            print("!! Opción inválida. Intente otra vez !!")

if __name__ == "__main__":
    main()