# Ejemplo de como funciona una clase que contiene atributos (variables) que usaran luego
# Los objetos (definiciones/funciones) que estan dentro de la clase

class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def encender_motor(self):
        return f"El {self.marca} {self.modelo} esta encendiendo."
    
Carro1 = Carro("BMW", "M3", "Azul") # En esta variable se guarda a instancia que contiene la clase Carro y sus funciones
Carro2 = Carro("Jeep", "Wrangler", "Rojo")

print(Carro1.encender_motor()) # Mencionando la variable que contiene la clase podemos acceder a sus demas definiciones
print(Carro2.encender_motor())