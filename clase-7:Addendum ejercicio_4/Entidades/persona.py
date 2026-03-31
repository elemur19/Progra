class Persona:
    def __init__(self, nombre, edad, pais, ocupacion, hobby, tatuajes, estado_civil, genero):
        # atributos ahora privados
        self.__nombre = nombre
        self.__edad = edad
        self.__pais = pais
        self.__ocupacion = ocupacion
        self.__hobby = hobby
        self.__tatuajes = tatuajes
        self.__estado_civil = estado_civil
        self.__genero = genero

        # composición: ahora tiene mascotas y vehículos
        self.__mascotas = []
        self.__vehiculos = []

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_pais(self):
        return self.__pais

    def get_ocupacion(self):
        return self.__ocupacion

    def get_hobby(self):
        return self.__hobby

    def get_tatuajes(self):
        return self.__tatuajes

    def get_estado_civil(self):
        return self.__estado_civil

    def get_genero(self):
        return self.__genero

    def get_mascotas(self):
        return self.__mascotas

    def get_vehiculos(self):
        return self.__vehiculos

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_pais(self, pais):
        self.__pais = pais

    def set_ocupacion(self, ocupacion):
        self.__ocupacion = ocupacion

    def set_hobby(self, hobby):
        self.__hobby = hobby

    def set_tatuajes(self, tatuajes):
        self.__tatuajes = tatuajes

    def set_estado_civil(self, estado_civil):
        self.__estado_civil = estado_civil

    def set_genero(self, genero):
        self.__genero = genero

    # __str__ y __len__
    def __str__(self):
        texto = (
            f"\n{self.__nombre}\n"
            f"Edad: {self.__edad}\n"
            f"Género: {self.__genero}\n"
            f"País: {self.__pais}\n"
            f"Ocupación: {self.__ocupacion}\n"
            f"Hobby: {self.__hobby}\n"
            f"Tatuajes: {self.__tatuajes}\n"
            f"Estado civil: {self.__estado_civil}\n"
        )

        if len(self.__mascotas) > 0:
            texto += "Mascotas:\n"
            for m in self.__mascotas:
                texto += f"  - {m.get_nombre()} ({m.get_raza()})\n"
        else:
            texto += "Mascotas: Ninguna\n"

        if len(self.__vehiculos) > 0:
            texto += "Vehículos:\n"
            for v in self.__vehiculos:
                texto += f"  - {v.get_marca()} {v.get_modelo()} ({v.get_año()})\n"
        else:
            texto += "Vehículos: Ninguno\n"

        texto += "----------------------------"
        return texto
    
    def __len__(self):
        return len(self.__nombre)
    
    def agregar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)

#al correr sims_main.py me di cuenta que el len estaba mal y ademas queria que al imprimir personas mostrara los vehiculos y mascotas de persona para que se vea la composición