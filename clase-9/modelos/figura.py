from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def volumen(self):
        pass