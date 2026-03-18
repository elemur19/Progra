from medios_transporte.transportes import Transporte


class Cuadraciclo(Transporte):
    def __init__(self, marca, capacidad, velocidad_maxima, traccion):
        super().__init__(marca, capacidad, velocidad_maxima)
        self.__traccion = traccion

    @property
    def traccion(self):
        return self.__traccion

    @traccion.setter
    def traccion(self, nueva_traccion):
        self.__traccion = nueva_traccion

    def __str__(self):
        return f"CUADRACICLO\n{super().__str__()}\nTracción: {self.__traccion}"