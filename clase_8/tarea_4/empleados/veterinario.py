from empleados.empleados import Empleado


class Veterinario(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.__especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        self.__especialidad = nueva_especialidad

    def __str__(self):
        return f"VETERINARIO\n{super().__str__()}\nEspecialidad: {self.__especialidad}"