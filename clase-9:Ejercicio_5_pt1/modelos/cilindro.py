from modelos.figura import Figura

class Cilindro(Figura):
    PI = 3.14

    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return self.PI * self.radio * self.radio * self.altura