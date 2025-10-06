#Realizamos el contructor, y le vamos a decir que salude.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hola, mi nombre es {self.name} y tengo {self.age} años")
    
person1 = Person("Carlos", 40)
person2 = Person("Mariana", 25)

person1.greet()
person2.greet()

#EJEMPLO CUENTA BANCARIA:
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount} en la cuenta {self.account_holder}, el nuevo saldo es {self.balance}")
        else:
            print(f"No se puede depositar porque la cuenta {self.account_holder} se encuentra Inactiva")

    def withdraw (self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount} en la cuenta de {self.account_holder}, el nuevo saldo es {self.balance}")
            else:
                print(f"No se puede hacer el retiro debido a que no cuenta con saldo suficiente")                
        else:
            print(f"No se puede retirar porque la cuenta de {self.account_holder} se encuentra Inactiva")
    
    def desactive_account(self):
        self.is_active = False
        print("Se ha desactivado la cuenta satisfactoriamente")

    def active_account(self):
        self.is_active = True
        print("Se ha activado la cuenta satisfactoriamente")

#Aqui llamamos a los metodos:
account1 = BankAccount("Betty", 500)
account2 = BankAccount("Mariana", 1000)

#llamada a los metodos
account1.deposit(200)
account2.deposit(100)

account1.desactive_account()
account1.withdraw(100)

account1.active_account()
account1.withdraw(50)