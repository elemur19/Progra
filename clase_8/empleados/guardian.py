from empleados.empleados import Empleado


class Guardian(Empleado):
    def __init__(self, nombre, edad, salario, zona):
        super().__init__(nombre, edad, salario)
        self.__zona = zona

    @property
    def zona(self):
        return self.__zona

    @zona.setter
    def zona(self, nueva_zona):
        self.__zona = nueva_zona

    def __str__(self):
        return f"GUARDIÁN\n{super().__str__()}\nZona: {self.__zona}"