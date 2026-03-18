class Transporte:
    """
    Clase padre para representar un medio de transporte del zoológico.
    """

    def __init__(self, marca, capacidad, velocidad_maxima):
        self.__marca = marca
        self.__capacidad = capacidad
        self.__velocidad_maxima = velocidad_maxima

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, nueva_marca):
        self.__marca = nueva_marca

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, nueva_capacidad):
        self.__capacidad = nueva_capacidad

    @property
    def velocidad_maxima(self):
        return self.__velocidad_maxima

    @velocidad_maxima.setter
    def velocidad_maxima(self, nueva_velocidad):
        self.__velocidad_maxima = nueva_velocidad

    def __str__(self):
        return (
            f"Marca: {self.__marca}\n"
            f"Capacidad: {self.__capacidad}\n"
            f"Velocidad máxima: {self.__velocidad_maxima}"
        )