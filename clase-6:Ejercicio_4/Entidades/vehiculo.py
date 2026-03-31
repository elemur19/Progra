class Vehiculo:
    def __init__(self, marca, modelo, año, color, dueño_nombre):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.dueño = dueño_nombre
    def __str__(self):
        return (
            f"Marca: {self.marca}\n" 
            f"Modelo: {self.modelo}\n"
            f"Año: {self.año}\n"
            f"Color: {self.color}\n"
            f"Dueño: {self.dueño}\n"
            f"----------------------------"
        )