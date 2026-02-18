class Persona:
    def __init__(self, genero,nombre, edad, pais, ocupacion, hobby, tatuajes, estado_civil):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.ocupacion = ocupacion
        self.hobby = hobby
        self.tatuajes = tatuajes
        self.estado_civil = estado_civil
        self.genero = genero

    def __str__(self):
        return (
             f"\n{self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Género: {self.genero}\n"
            f"País: {self.pais}\n"
            f"Ocupación: {self.ocupacion}\n"
            f"Hobby: {self.hobby}\n"
            f"Tatuajes: {self.tatuajes}\n"
            f"Estado civil: {self.estado_civil}\n"
            f"----------------------------"
        )