from modelos.figura import Figura

class Esfera(Figura):
    PI = 3.14

    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        return (4.0 / 3.0) * self.PI * self.radio * self.radio * self.radio