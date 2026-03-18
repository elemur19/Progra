class Empleado:
    """
    Clase padre para representar a un empleado del zoológico.
    """

    def __init__(self, nombre, edad, salario):
        self.__nombre = nombre
        self.__edad = edad
        self.__salario = salario

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario):
        self.__salario = nuevo_salario

    def __str__(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nSalario: {self.__salario}"