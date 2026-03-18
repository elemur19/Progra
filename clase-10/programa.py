# Leer archivos CSV y JSON, calculos de promedios
from modulos.datos_csv import leer_personas_csv
from modulos.datos_json import leer_personas_json
from modulos.calculos import calcular_promedios

# Funcion para mostar el menu de opciones y resultados 
def mostrar_menu():
    print("====" * 6)
    print("\nDATA READER CSV / JSON")
    print("\n======== MENÚ ========")
    print("1. Leer archivo CSV")
    print("2. Leer archivo JSON")
    print("3. Salir")


def mostrar_resultados(promedios):
    print("\n===== RESULTADOS =====")
    print(f"Promedio de edad: {promedios['edad']:.2f}")
    print(f"Promedio de salario: {promedios['salario']:.2f}")
    print(f"Promedio de peso: {promedios['peso']:.2f}")
    print()

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            ruta = "data/personas.csv"
            personas = leer_personas_csv(ruta)
            promedios = calcular_promedios(personas)
            mostrar_resultados(promedios)

        elif opcion == "2":
            ruta = "data/personas.json"
            personas = leer_personas_json(ruta)
            promedios = calcular_promedios(personas)
            mostrar_resultados(promedios)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.\n")


main()