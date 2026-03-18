from medios_transporte.transportes import Transporte


class Bicicleta(Transporte):
    def __init__(self, marca, capacidad, velocidad_maxima, tipo):
        super().__init__(marca, capacidad, velocidad_maxima)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    def __str__(self):
        return f"BICICLETA\n{super().__str__()}\nTipo: {self.__tipo}"