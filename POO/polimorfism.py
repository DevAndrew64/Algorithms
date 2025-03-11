
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

# Significa que diferentes clases pueden tener el mismo método con comportamientos distintos
animals = [Dog("Max"), Cat("Fiona"), Animal("Unknown")]

for animal in animals:
    print(f"{animal.name} says {animal.suenan()}")