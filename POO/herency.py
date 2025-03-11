# La herencia permite que una clase (subclase) herede atributos(variables) y metodos(funciones)
# de otra clase (Superclase/ClasePadre), facilitando la reutilizacion de codigo

class Animal:
    # Atributos de la clase Animal
    def __init__(self, name):
        self.name = name
        
    def suenan(self):
        return "Some sound"

# Herencia de clase Animal    
class Dog(Animal):
    def suenan(self):
        return "Woof!"
    
class Cat(Animal):
    def suenan(self):
        return "Meow!"

# Objetos de la sublclase
Perro = Dog("Frida")
Gato = Cat("Kira")

print(Perro.name, "says", Perro.suenan())
print(Gato.name, "says", Gato.suenan())