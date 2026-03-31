class Mascota:
    def __init__(self, nombre, raza, edad, color, juguete_favorito, dueño_nombre):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color 
        self.juguete_favorito = juguete_favorito
        self.dueño_nombre = dueño_nombre
    def __str__(self):
        return (
            f"\n{self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Raza: {self.raza}\n"
            f"Color: {self.color}\n"
            f"Juguete favorito: {self.juguete_favorito}\n"
            f"Dueño: {self.dueño_nombre}\n"
            f"----------------------------"
        )