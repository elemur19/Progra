from empleados.empleados import Empleado


class Administrador(Empleado):
    def __init__(self, nombre, edad, salario, area):
        super().__init__(nombre, edad, salario)
        self.__area = area

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, nueva_area):
        self.__area = nueva_area

    def __str__(self):
        return f"ADMINISTRADOR\n{super().__str__()}\nÁrea: {self.__area}"