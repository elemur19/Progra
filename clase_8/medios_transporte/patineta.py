from medios_transporte.transportes import Transporte


class Patineta(Transporte):
    def __init__(self, marca, capacidad, velocidad_maxima, electrica):
        super().__init__(marca, capacidad, velocidad_maxima)
        self.__electrica = electrica

    @property
    def electrica(self):
        return self.__electrica

    @electrica.setter
    def electrica(self, nueva_electrica):
        self.__electrica = nueva_electrica

    def __str__(self):
        return f"PATINETA\n{super().__str__()}\nEléctrica: {self.__electrica}"