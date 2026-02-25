class Vehiculo:
    def __init__(self, marca, modelo, año, color, dueño):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__color = color
# Quite del original el 'dueno_nombre' y lo cambié por 'dueño' para que si sea una asociación con Persona
        # Asociación: dueño es Persona
        self.__dueño = dueño

    # Getters
    def get_marca(self): 
        return self.__marca
    def get_modelo(self): 
        return self.__modelo
    def get_año(self): 
        return self.__año
    def get_color(self): 
        return self.__color
    def get_dueño(self): 
        return self.__dueño

    # Setters
    def set_marca(self, marca): 
        self.__marca = marca
    def set_modelo(self, modelo): 
        self.__modelo = modelo
    def set_año(self, año): 
        self.__año = año
    def set_color(self, color): 
        self.__color = color
    def set_dueño(self, dueño): 
        self.__dueño = dueño


# str y len
    def __str__(self):
        if self.__dueño is not None:
            nombre_dueño = self.__dueño.get_nombre()
        else:
            nombre_dueño = "Sin dueño"

        return (
            f"Marca: {self.__marca}\n"
            f"Modelo: {self.__modelo}\n"
            f"Año: {self.__año}\n"
            f"Color: {self.__color}\n"
            f"Dueño: {nombre_dueño}\n"
            f"----------------------------"
        )

    def __len__(self):
        return len(self.__marca)