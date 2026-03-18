from empleados.empleados import Empleado


class Conserje(Empleado):
    def __init__(self, nombre, edad, salario, turno):
        super().__init__(nombre, edad, salario)
        self.__turno = turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, nuevo_turno):
        self.__turno = nuevo_turno

    def __str__(self):
        return f"CONSERJE\n{super().__str__()}\nTurno: {self.__turno}"