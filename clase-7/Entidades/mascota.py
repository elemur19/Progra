class Mascota:
    def __init__(self, nombre, raza, edad, color, juguete_favorito, dueño):
        # Atributos privados
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__color = color
        self.__juguete_favorito = juguete_favorito
       # Quite del original el 'dueno_nombre' y lo cambié por 'dueño' para que si sea una asociación con Persona
        # Asociación: dueño es Persona
        self.__dueño = dueño


    # Getters

    def get_nombre(self):
        return self.__nombre

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    def get_color(self):
        return self.__color

    def get_juguete_favorito(self):
        return self.__juguete_favorito

    def get_dueño(self):
        return self.__dueño

  
    # Setters

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_raza(self, raza):
        self.__raza = raza

    def set_edad(self, edad):
        self.__edad = edad

    def set_color(self, color):
        self.__color = color

    def set_juguete_favorito(self, juguete_favorito):
        self.__juguete_favorito = juguete_favorito

    def set_dueno_nombre(self, dueno_nombre):
        self.__dueno_nombre = dueno_nombre

  
    # str y len

    def __str__(self):
        if self.__dueño:
            nombre_dueño = self.__dueño.get_nombre()
        else:
            nombre_dueño = "Sin dueño"

        return (
            f"\n{self.__nombre}\n"
            f"Edad: {self.__edad}\n"
            f"Raza: {self.__raza}\n"
            f"Color: {self.__color}\n"
            f"Juguete favorito: {self.__juguete_favorito}\n"
            f"Dueño: {nombre_dueño}\n"
            f"----------------------------"
        )

    def __len__(self):
        return len(self.__nombre)