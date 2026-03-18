from animales.animales import Animal


class Ave(Animal):

    def __init__(self, nombre, edad, peso, puede_volar):
        super().__init__(nombre, edad, peso)
        self.__puede_volar = puede_volar

    @property
    def puede_volar(self):
        return self.__puede_volar

    @puede_volar.setter
    def puede_volar(self, valor):
        self.__puede_volar = valor

    def __str__(self):
        return f"AVE\n{super().__str__()}\nPuede volar: {self.__puede_volar}"

# Clase específica para Aguila, que hereda de Ave
class Aguila(Ave):

    def __init__(self, nombre, edad, peso, puede_volar, envergadura):
        super().__init__(nombre, edad, peso, puede_volar)
        self.__envergadura = envergadura

    @property
    def envergadura(self):
        return self.__envergadura

    @envergadura.setter
    def envergadura(self, valor):
        self.__envergadura = valor

    def __str__(self):
        return f"AGUILA\n{super().__str__()}\nEnvergadura: {self.__envergadura}"