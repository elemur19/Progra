from DB_Censo import personas


def pedir_int(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            return int(valor)
        except ValueError:
            print("Entrada inválida.")


def pedir_float(mensaje):
    while True:
        valor = input(mensaje).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Entrada inválida.")


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("No puede ir vacío.")
        else:
            return valor


def agregar_nueva_persona():
    print("\n--- Agregar nueva persona ---")
    identificacion = pedir_texto("Identificación: ")
    nombre = pedir_texto("Nombre: ")
    apellido = pedir_texto("Apellido: ")
    edad = pedir_int("Edad: ")
    salario = pedir_float("Salario: ")
    ocupacion = pedir_texto("Ocupación: ")
    altura = pedir_float("Altura (en metros, ej 1.75): ")
    peso = pedir_float("Peso (en kg, ej 72.5): ")


    nueva_persona = {
        "identificacion": identificacion,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "salario": salario,
        "ocupacion": ocupacion,
        "altura": altura,
        "peso": peso
    }

    personas.append(nueva_persona)
    print("Persona agregada correctamente.\n")


def imprimir_todas_las_personas():
    print("\n--- Listado completo de personas ---")
   

    for i, p in enumerate(personas, start=1):
        print(f"\nPersona #{i}")
        print(f"  Identificación: {p.get('identificacion')}")
        print(f"  Nombre: {p.get('nombre')}")
        print(f"  Apellido: {p.get('apellido')}")
        print(f"  Edad: {p.get('edad')}")
        print(f"  Salario: {p.get('salario')}")
        print(f"  Ocupación: {p.get('ocupacion')}")
        print(f"  Altura: {p.get('altura')}")
        print(f"  Peso: {p.get('peso')}")
    print("")


def calcular_imc(p):
    # IMC = peso / (altura^2)
    altura = float(p.get("altura", 0))
    peso = float(p.get("peso", 0))
    if altura <= 0:
        return None
    return peso / (altura * altura)


def persona_mayor_imc():
    print("\n--- Persona con mayor IMC ---")
    if len(personas) == 0:
        print("No hay personas registradas.\n")
        return

    max_imc = None
    persona_max = None

    for p in personas:
        imc = calcular_imc(p)
        if imc is None:
            continue
        if (max_imc is None) or (imc > max_imc):
            max_imc = imc
            persona_max = p

    if persona_max is None:
        print("No se pudo calcular IMC (revisar alturas/pesos).\n")
        return

    print(f"Nombre: {persona_max.get('nombre')} {persona_max.get('apellido')}")
    print(f"Identificación: {persona_max.get('identificacion')}")
    print(f"Altura: {persona_max.get('altura')} m")
    print(f"Peso: {persona_max.get('peso')} kg")
    print(f"IMC: {max_imc:.2f}\n")


def media_salario():
    print("\n--- Media del salario ---")
    if len(personas) == 0:
        print("No hay personas registradas.\n")
        return

    total = 0.0
    for p in personas:
        total += float(p.get("salario", 0))

    media = total / len(personas)
    print(f"Media salarial: {media:.2f}\n")


def varianza_salario():
    print("\n--- Varianza del salario ---")
    n = len(personas)
    if n == 0:
        print("No hay personas registradas.\n")
        return
    if n == 1:
        print("Varianza no definida con 1 persona (se necesita al menos 2).\n")
        return

    # media del salario
    total = 0.0
    for p in personas:
        total += float(p.get("salario", 0))
    media = total / n

    suma_cuadrados = 0.0
    for p in personas:
        x = float(p.get("salario", 0))
        diff = x - media
        suma_cuadrados += diff * diff

    # varianza 
    varianza = suma_cuadrados / (n - 1)
    print(f"Media salarial: {media:.2f}")
    print(f"Varianza salarial (muestral): {varianza:.2f}\n")


def media_altura():
    print("\n--- Media de la altura ---")
    if len(personas) == 0:
        print("No hay personas registradas.\n")
        return

    total = 0.0
    for p in personas:
        total += float(p.get("altura", 0))

    media = total / len(personas)
    print(f"Media de altura: {media:.2f} m\n")


def persona_mas_alta():
    print("\n--- Persona más alta ---")
    if len(personas) == 0:
        print("No hay personas registradas.\n")
        return

    max_altura = None
    persona_max = None

    for p in personas:
        altura = float(p.get("altura", 0))
        if (max_altura is None) or (altura > max_altura):
            max_altura = altura
            persona_max = p

    print(f"Nombre: {persona_max.get('nombre')} {persona_max.get('apellido')}")
    print(f"Identificación: {persona_max.get('identificacion')}")
    print(f"Altura: {max_altura:.2f} m\n")


def persona_mas_pesada():
    print("\n--- Persona más pesada ---")
    if len(personas) == 0:
        print("No hay personas registradas.\n")
        return

    max_peso = None
    persona_max = None

    for p in personas:
        peso = float(p.get("peso", 0))
        if (max_peso is None) or (peso > max_peso):
            max_peso = peso
            persona_max = p

    print(f"Nombre: {persona_max.get('nombre')} {persona_max.get('apellido')}")
    print(f"Identificación: {persona_max.get('identificacion')}")
    print(f"Peso: {max_peso:.2f} kg\n")


def mostrar_menu():
    print("=== Analizador de Censo – Isla Karakuri ===")
    print("1. Agregar nueva persona")
    print("2. Imprimir todas las personas")
    print("3. Indicar la persona con mayor IMC")
    print("4. Cálculo de la media del salario")
    print("5. Cálculo de la varianza del salario")
    print("6. Cálculo de la media de la altura")
    print("7. Encontrar la persona más alta")
    print("8. Encontrar la persona más pesada")
    print("9. Salir del sistema")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "1":
            agregar_nueva_persona()
        elif opcion == "2":
            imprimir_todas_las_personas()
        elif opcion == "3":
            persona_mayor_imc()
        elif opcion == "4":
            media_salario()
        elif opcion == "5":
            varianza_salario()
        elif opcion == "6":
            media_altura()
        elif opcion == "7":
            persona_mas_alta()
        elif opcion == "8":
            persona_mas_pesada()
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()
