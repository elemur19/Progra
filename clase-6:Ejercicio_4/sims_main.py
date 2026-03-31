from Entidades.persona import Persona
from Entidades.mascota import Mascota
from Entidades.vehiculo import Vehiculo


personas = []
mascotas = []
vehiculos = []

def mostrar_menu():
    print("========== SIMS ==========")
    print((r"""
         /\_/\  
        ( o.o )  
         > ^ <    
    """))
    print("Crea tu propio mundo de Sims")
    print("----------------------------")
    print("1. Crear Sim")
    print("2. Crear mascota")
    print("3. Crear vehículo")
    print("4. Imprimir personas")
    print("5. Imprimir mascotas")
    print("6. Imprimir vehículos")
    print("7. Imprimir todas las entidades")
    print("8. Salir")

def crear_persona():
    genero = input("Género: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ocupacion = input("Ocupación: ")
    pais = input("País: ")
    hobby = input("Hobby: ")
    tatuajes = int(input("Tatuajes: "))
    estado_civil = input("Estado civil: ")

    nueva_persona = Persona(genero,nombre, edad, pais, ocupacion, hobby, tatuajes, estado_civil)
    personas.append(nueva_persona)
    print("Persona creada correctamente.")

def crear_mascota():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    raza = input("Raza: ")
    color = input("Color: ")
    juguete_favorito = input("Juguete favorito: ")
    dueño_nombre = input("Nombre del dueño: ")

    nueva_mascota = Mascota(nombre, raza, edad, color, juguete_favorito, dueño_nombre)
    mascotas.append(nueva_mascota)
    print("Mascota creada.")

def crear_vehiculo():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = input("Año: ")
    color = input("Color: ")
    dueño_nombre = input("Nombre del dueño: ")

    nuevo_vehiculo = Vehiculo(marca, modelo, año, color, dueño_nombre)
    vehiculos.append(nuevo_vehiculo)
    print("Nuevo vehículo creado.")

def imprimir_lista(lista, titulo):
    print(f"\n--- {titulo} ---")
    if len(lista) == 0:
        print("No hay registros.")
    else:
        for elemento in lista:
            print(elemento)


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_persona()
    elif opcion == "2":
        crear_mascota()
    elif opcion == "3":
        crear_vehiculo()
    elif opcion == "4":
        imprimir_lista(personas, "PERSONAS")
    elif opcion == "5":
        imprimir_lista(mascotas, "MASCOTAS")
    elif opcion == "6":
        imprimir_lista(vehiculos, "VEHÍCULOS")
    elif opcion == "7":
        imprimir_lista(personas, "PERSONAS")
        imprimir_lista(mascotas, "MASCOTAS")
        imprimir_lista(vehiculos, "VEHÍCULOS")
    elif opcion == "8":
        print("Saliendo del programa...Chao!")
        break
    else:
        print("Opción inválida.")
