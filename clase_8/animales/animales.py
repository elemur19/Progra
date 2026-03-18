class Animal:
    """
    Clase padre para representar un animal del zoológico.
    """

    def __init__(self, nombre, edad, peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, nuevo_peso):
        self.__peso = nuevo_peso

    def __str__(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nPeso: {self.__peso}"