from Entidades.persona import Persona
from Entidades.mascota import Mascota
from Entidades.vehiculo import Vehiculo


personas = []
mascotas = []
vehiculos = []

#Menu
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

# Persona
def crear_persona():
    genero = input("Género: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ocupacion = input("Ocupación: ")
    pais = input("País: ")
    hobby = input("Hobby: ")
    tatuajes = int(input("Tatuajes: "))
    estado_civil = input("Estado civil: ")

    nueva_persona = Persona(nombre, edad, pais, ocupacion, hobby, tatuajes, estado_civil, genero)
    personas.append(nueva_persona)
    print("Persona creada correctamente.")


#Mascota
def crear_mascota():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    raza = input("Raza: ")
    color = input("Color: ")
    juguete_favorito = input("Juguete favorito: ")
    dueno_nombre = input("Dueño (nombre): ")
    dueno_obj = buscar_persona_por_nombre(personas, dueno_nombre)
    if dueno_obj is None:
        print("No existe una persona con ese nombre. Cree la persona primero.")
    else:
        mascota = Mascota(nombre, raza, edad, color, juguete_favorito, dueno_obj)
        mascotas.append(mascota)
        dueno_obj.agregar_mascota(mascota)  # composición
        print("Mascota creada.")

# cambie el 'dueno_nombre' por 'dueno_obj' para que sea una asociación con Persona, y agregue la mascota a la lista de mascotas del dueño.

#Vehiculo
def crear_vehiculo():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = input("Año: ")
    color = input("Color: ")
    dueno = input("Dueño: ")
    dueño_objeto = buscar_persona_por_nombre(personas, dueno)
    if dueño_objeto is None:
        print("No existe una persona con ese nombre. Cree la persona primero.")
    else:
        vehiculo = Vehiculo(marca, modelo, año, color, dueño_objeto)
        vehiculos.append(vehiculo)
        dueño_objeto.agregar_vehiculo(vehiculo)
        print("Nuevo vehículo creado.")
#cambie el 'dueno' por 'dueño_objeto' para que sea una asociación con Persona, y agregue el vehículo a la lista de vehículos del dueño.


# Imprimir listas
def imprimir_lista(lista, titulo):
    print(f"\n--- {titulo} ---")
    if len(lista) == 0:
        print("No hay registros.")
    else:
        for elemento in lista:
            print(elemento)


#agregue una función para buscar personas por nombre, para luego asociar mascotas y vehículos a ellas
def buscar_persona_por_nombre(personas, nombre):
    for p in personas:
        if p.get_nombre().lower() == nombre.lower():
            return p
    return None

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
