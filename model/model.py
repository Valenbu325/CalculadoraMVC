from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, a: float, b:float)-> float: 
        pass

class Suma(Operacion):
    def ejecutar(self, a, b):
        return a + b
    
class Resta(Operacion):
    def ejecutar(self, a, b):
        return a - b 

class Multiplicacion(Operacion):
    def ejecutar(self, a, b):
        return a * b
    
class Division(Operacion):
    def ejecutar(self, a, b):
        if b == 0:
            raise ValueError ("Division por cero no es permitida")

        return a / b







