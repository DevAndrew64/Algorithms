# La abstraccion se trata de:
# Esconder detalles internos y mostrar solo lo esencial. Se implementa con clases abstractas.


# Clase abstracta (Abstract Base Class)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    
Carro = Car()
Moto = Motorcycle()
print(Carro.start_engine())
print(Moto.start_engine())