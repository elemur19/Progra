from modelos.figura import Figura

class Cono(Figura):
    PI = 3.14

    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return (1.0 / 3.0) * self.PI * self.radio * self.radio * self.altura