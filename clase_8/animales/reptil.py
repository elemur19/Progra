from animales.animales import Animal


class Reptil(Animal):

    def __init__(self, nombre, edad, peso, venenoso):
        super().__init__(nombre, edad, peso)
        self.__venenoso = venenoso

    @property
    def venenoso(self):
        return self.__venenoso

    @venenoso.setter
    def venenoso(self, valor):
        self.__venenoso = valor

    def __str__(self):
        return f"REPTIL\n{super().__str__()}\nVenenoso: {self.__venenoso}"

# Clase específica para Iguana, que hereda de Reptil
class Iguana(Reptil):

    def __init__(self, nombre, edad, peso, venenoso, longitud):
        super().__init__(nombre, edad, peso, venenoso)
        self.__longitud = longitud

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, valor):
        self.__longitud = valor

    def __str__(self):
        return f"IGUANA\n{super().__str__()}\nLongitud: {self.__longitud}"