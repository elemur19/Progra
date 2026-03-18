from animales.animales import Animal


class Mamifero(Animal):

    def __init__(self, nombre, edad, peso, tipo_pelaje):
        super().__init__(nombre, edad, peso)
        self.__tipo_pelaje = tipo_pelaje

    @property
    def tipo_pelaje(self):
        return self.__tipo_pelaje

    @tipo_pelaje.setter
    def tipo_pelaje(self, valor):
        self.__tipo_pelaje = valor

    def __str__(self):
        return f"MAMIFERO\n{super().__str__()}\nPelaje: {self.__tipo_pelaje}"


# Clase específica para León, que hereda de Mamifero
class Leon(Mamifero):

    def __init__(self, nombre, edad, peso, tipo_pelaje, manada):
        super().__init__(nombre, edad, peso, tipo_pelaje)
        self.__manada = manada

    @property
    def manada(self):
        return self.__manada

    @manada.setter
    def manada(self, valor):
        self.__manada = valor

    def __str__(self):
        return f"LEON\n{super().__str__()}\nManada: {self.__manada}"