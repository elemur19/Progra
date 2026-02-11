from volumenes_info import (
    volumen_cilindro,
    volumen_cono,
    volumen_paralelepipedo,
    volumen_cubo,
    volumen_esfera
)

#menu de calculadora 
def mostrar_menu():
    print("\n ******* Calculadora de Volúmenes *******")
    print("\n Opciones a calcular:")
    print("\n1) Cubo")
    print("2) Paralelepípedo")
    print("3) Cilindro")
    print("4) Esfera")
    print("5) Cono")
    print("0) Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("\nElija una opción: ")

        if opcion == "0":
            print("Hasta Luego!")
            break

        elif opcion == "1":
            lado = float(input("Lado: "))
            v = volumen_cubo(lado)
            print("====> Volumen del cubo =", round(v, 4))

        elif opcion == "2":
            largo = float(input("Largo: "))
            ancho = float(input("Ancho: "))
            alto =float(input("Alto: "))
            v = volumen_paralelepipedo(largo, ancho, alto)
            print("====> Volumen del paralelepípedo =", round(v, 4))

        elif opcion == "3":
            radio = float(input("Radio: "))
            altura = float(input("Altura: "))
            v = volumen_cilindro(radio, altura)
            print("====> Volumen del cilindro =", round(v, 4))

        elif opcion == "4":
            radio = float(input("Radio: "))
            v = volumen_esfera(radio)
            print("====> Volumen de la esfera =", round(v, 4))

        elif opcion == "5":
            radio = float(input("Radio: "))
            altura = float(input("Altura: "))
            v = volumen_cono(radio, altura)
            print("====> Volumen del cono =", round(v, 4))

        else:
            print("!! Opción inválida. Intente otra vez !!")

if __name__ == "__main__":
    main()