
# Ejemplo de atributos privados con _

class BankAccount: # El encapsulamiento es restringir el acceso a atributos(variables) y metodos(funciones) internos de un objeto
    def __init__(self, owner, balance): # Esto con el fin de proteger los datos de modificaciones accidentales
        self.owner = owner
        self.__balance = balance # Atributo/variable privada
        
        
    def deposit(self, amount):
        self.__balance += amount
        return f"New balance ${self.__balance}"
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return f"New balance ${self.__balance}"
    
    def get_balance(self):
        return self.__balance

# Creamos cuenta bancaria
account = BankAccount("Jhon", 35000)

print(account.deposit(1500))
print(account.withdraw(2000))
print(account.get_balance())