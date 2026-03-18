from animales.animales import Animal


class Anfibio(Animal):

    def __init__(self, nombre, edad, peso, habitat):
        super().__init__(nombre, edad, peso)
        self.__habitat = habitat

    @property
    def habitat(self):
        return self.__habitat

    @habitat.setter
    def habitat(self, valor):
        self.__habitat = valor

    def __str__(self):
        return f"ANFIBIO\n{super().__str__()}\nHabitat: {self.__habitat}"

# Clase específica para Rana, que hereda de Anfibio
class Rana(Anfibio):

    def __init__(self, nombre, edad, peso, habitat, color):
        super().__init__(nombre, edad, peso, habitat)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, valor):
        self.__color = valor

    def __str__(self):
        return f"RANA\n{super().__str__()}\nColor: {self.__color}"