from validacion import pedir_texto, pedir_entero, pedir_float
from menu import menu_principal, submenu_empleados, submenu_transportes, submenu_animales

from empleados.administrador import Administrador
from empleados.guardian import Guardian
from empleados.conserje import Conserje
from empleados.veterinario import Veterinario

from medios_transporte.bicicleta import Bicicleta
from medios_transporte.cuadraciclo import Cuadraciclo
from medios_transporte.patineta import Patineta

from animales.mamifero import Leon
from animales.pez import Tiburon
from animales.ave import Aguila
from animales.reptil import Iguana
from animales.anfibio import Rana


empleados = []
transportes = []
animales = []


def listar(lista, titulo):

    print("\n==========================")
    print(titulo)
    print("==========================")

    if len(lista) == 0:
        print("No hay registros.")
    else:
        for i, elemento in enumerate(lista, start=1):
            print(f"\nRegistro #{i}")
            print(elemento)

    input("\n[ENTER] para volver al menú...")

def agregar_empleado():

    submenu_empleados()
    opcion = pedir_entero("Seleccione una opción: ")

    nombre = pedir_texto("Nombre: ")
    edad = pedir_entero("Edad: ")
    salario = pedir_float("Salario: ")

    if opcion == 1:

        area = pedir_texto("Área: ")
        empleado = Administrador(nombre, edad, salario, area)
        empleados.append(empleado)

        print("Administrador agregado.")

    elif opcion == 2:

        zona = pedir_texto("Zona: ")
        empleado = Guardian(nombre, edad, salario, zona)
        empleados.append(empleado)

        print("Guardián agregado.")

    elif opcion == 3:

        turno = pedir_texto("Turno: ")
        empleado = Conserje(nombre, edad, salario, turno)
        empleados.append(empleado)

        print("Conserje agregado.")

    elif opcion == 4:

        especialidad = pedir_texto("Especialidad: ")
        empleado = Veterinario(nombre, edad, salario, especialidad)
        empleados.append(empleado)

        print("Veterinario agregado.")

    else:
        print("Opción inválida.")


def agregar_transporte():

    submenu_transportes()
    opcion = pedir_entero("Seleccione una opción: ")

    marca = pedir_texto("Marca: ")
    capacidad = pedir_entero("Capacidad: ")
    velocidad = pedir_float("Velocidad máxima: ")

    if opcion == 1:

        tipo = pedir_texto("Tipo de bicicleta: ")
        transporte = Bicicleta(marca, capacidad, velocidad, tipo)
        transportes.append(transporte)

        print("Bicicleta agregada.")

    elif opcion == 2:

        traccion = pedir_texto("Tipo de tracción: ")
        transporte = Cuadraciclo(marca, capacidad, velocidad, traccion)
        transportes.append(transporte)

        print("Cuadraciclo agregado.")

    elif opcion == 3:

        electrica = pedir_texto("¿Es eléctrica? (si/no): ")
        transporte = Patineta(marca, capacidad, velocidad, electrica)
        transportes.append(transporte)

        print("Patineta agregada.")

    else:
        print("Opción inválida.")


def agregar_animal():

    submenu_animales()
    opcion = pedir_entero("Seleccione una opción: ")

    nombre = pedir_texto("Nombre: ")
    edad = pedir_entero("Edad: ")
    peso = pedir_float("Peso: ")

    if opcion == 1:

        venenoso = pedir_texto("¿Es venenoso? (si/no): ")
        longitud = pedir_float("Longitud: ")

        animal = Iguana(nombre, edad, peso, venenoso, longitud)
        animales.append(animal)

        print("Iguana agregada.")

    elif opcion == 2:

        pelaje = pedir_texto("Tipo de pelaje: ")
        manada = pedir_texto("Nombre de la manada: ")

        animal = Leon(nombre, edad, peso, pelaje, manada)
        animales.append(animal)

        print("León agregado.")

    elif opcion == 3:

        vuela = pedir_texto("¿Puede volar? (si/no): ")
        envergadura = pedir_float("Envergadura: ")

        animal = Aguila(nombre, edad, peso, vuela, envergadura)
        animales.append(animal)

        print("Águila agregada.")

    elif opcion == 4:

        agua = pedir_texto("Tipo de agua: ")
        especie = pedir_texto("Especie: ")

        animal = Tiburon(nombre, edad, peso, agua, especie)
        animales.append(animal)

        print("Tiburón agregado.")

    elif opcion == 5:

        habitat = pedir_texto("Hábitat: ")
        color = pedir_texto("Color: ")

        animal = Rana(nombre, edad, peso, habitat, color)
        animales.append(animal)

        print("Rana agregada.")

    else:
        print("Opción inválida.")


def main():

    while True:

        menu_principal()
        opcion = pedir_entero("Seleccione una opción: ")

        if opcion == 1:
            agregar_empleado()

        elif opcion == 2:
            listar(empleados, "LISTA DE EMPLEADOS")

        elif opcion == 3:
            agregar_transporte()

        elif opcion == 4:
            listar(transportes, "LISTA DE TRANSPORTES")

        elif opcion == 5:
            agregar_animal()

        elif opcion == 6:
            listar(animales, "LISTA DE ANIMALES")

        elif opcion == 7:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


main()