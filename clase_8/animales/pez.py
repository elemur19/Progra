from animales.animales import Animal


class Pez(Animal):
    def __init__(self, nombre, edad, peso, tipo_agua):
        super().__init__(nombre, edad, peso)
        self.__tipo_agua = tipo_agua

    @property
    def tipo_agua(self):
        return self.__tipo_agua

    @tipo_agua.setter
    def tipo_agua(self, nuevo_tipo):
        self.__tipo_agua = nuevo_tipo

    def __str__(self):
        return f"PEZ\n{super().__str__()}\nTipo de agua: {self.__tipo_agua}"
    



# Clase específica para Tiburón, que hereda de Pez
class Tiburon(Pez):

    def __init__(self, nombre, edad, peso, tipo_agua, especie):
        super().__init__(nombre, edad, peso, tipo_agua)
        self.__especie = especie

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, valor):
        self.__especie = valor

    def __str__(self):
        return f"TIBURON\n{super().__str__()}\nEspecie: {self.__especie}"