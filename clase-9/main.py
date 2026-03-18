from modelos.figura import Figura
from modelos.cubo import Cubo
from modelos.paralelepipedo import Paralelepipedo
from modelos.cilindro import Cilindro
from modelos.esfera import Esfera
from modelos.cono import Cono

# Liskov Substitution 
def imprimir_volumen(figura: Figura):
    print("====> Volumen =", round(figura.volumen(), 4))
    input("\n[ENTER] para volver al menú...")
    # Agrege un enter para volver al menu, esto no lo tenia el codigo original, pero me gusta como se ve asi

# menu de la calculadora 
def mostrar_menu():
    print("\n******* Calculadora de Volúmenes *******")
    print("\nOpciones a calcular:")
    print("\n1) Cubo")
    print("2) Paralelepípedo")
    print("3) Cilindro")
    print("4) Esfera")
    print("5) Cono")
    print("6) Salir")

# Funcion principal de la calculadora. 
def main():
    cubo = Cubo(4)
    paralelepipedo = Paralelepipedo(5, 3, 2)
    cilindro = Cilindro(3, 6)
    esfera = Esfera(4)
    cono = Cono(3, 5)

    while True:
        mostrar_menu()
        opcion = input("\nElija una opción: ")

        if opcion == "6":
            print("Hasta luego!")
            break

        elif opcion == "1":
            print("\nFigura seleccionada: Cubo")
            imprimir_volumen(cubo)

        elif opcion == "2":
            print("\nFigura seleccionada: Paralelepípedo")
            imprimir_volumen(paralelepipedo)

        elif opcion == "3":
            print("\nFigura seleccionada: Cilindro")
            imprimir_volumen(cilindro)

        elif opcion == "4":
            print("\nFigura seleccionada: Esfera")
            imprimir_volumen(esfera)

        elif opcion == "5":
            print("\nFigura seleccionada: Cono")
            imprimir_volumen(cono)

        else:
            print("!! Opción inválida. Intente otra vez !!")



if __name__ == "__main__":
    main()