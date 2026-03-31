from modelos.figura import Figura

class Paralelepipedo(Figura):
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def volumen(self):
        return self.largo * self.ancho * self.alto