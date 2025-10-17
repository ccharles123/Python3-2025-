class Vehicle:
    def __init__(self, brand, model, price):
        #ENCAPSULACION
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
        self.sold_to = None #Creo esta nueva variable y no le asigno nada, lo dejo vacio. 

    def sell(self, buyer_name: str):
        if self.is_available:
            self.is_available = False
            self.sold_to = buyer_name #aqui recibo el nombre del cliente y lo asigno a la variable vacia sold_to.
            print(f"El vehiculo {self.brand} - {self.model} - Se vendio satisfactoriamente por valor de {self.price} a el cliente {self.sold_to}.")
        else:
            print(f"El vehiculo {self.brand} - {self.model} - No se encuentra en inventario")

    #ABSTRACCION    
    def check_available(self):
        return self.is_available
    
    #ABSTRACCION
    def get_price(self):
        return self.price
 

    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

#HERENCIA
class Car(Vehicle):
    #POLIMORFISMO
    def start_engine(self):
        if self.is_available:
            return f"El motor del carro {self.brand} esta en marcha"
        else: 
            return f"El carro {self.brand} no esta disponible"

    #POLIMORFISMO
    def stop_engine(self):
        if self.is_available:
            return f"El motor del carro {self.brand} esta detenido"
        else: 
            return f"El carro {self.brand} no esta disponible"
    
class Bike(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} esta en uso"
        else: 
            return f"La bicicleta {self.brand} no esta disponible"

    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} esta detenida"
        else: 
            return f"La bicicleta {self.brand} no esta disponible"

class Truck(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"El motor del camion {self.brand} esta en marcha"
        else: 
            return f"El camion {self.brand} no esta disponible"

    def stop_engine(self):
        if self.is_available:
            return f"El motor del camion {self.brand} esta detenido"
        else: 
            return f"El camion {self.brand} no esta disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell(self.name) #Le envio el nombre del comprador
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, el vehiculo {vehicle.brand}, No esta disponible")

    def inquire_vehicle(self, vehicle : Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else: 
            availablity = "No Disponible"
        print(f"El vehiculo {vehicle.brand} se encuentra {availablity} y cuesta {vehicle.get_price()}")

class Dealership:

    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle:Vehicle):
        self.inventory.append(vehicle)
        print(f"El vehiculo {vehicle.brand} fue agregado al inventario")

    def register_customers(self, customer : Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} fue agregado al listado de clientes")
    
    def show_available_vehicle(self):
        print(f"Los vehiculos disponibles son:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} {vehicle.model} por {vehicle.get_price()}")


# Creamos los vehiculos:
car1 = Car("Mazda", "3", 80)
bike1 = Bike("Treck", "MTB", 1.5)
truck1 = Truck("Volvo","FH16", 105)

# Creamos los clientes:
customer1 = Customer("Carlos")
customer2 = Customer("Mariana")

#Creamos el concesionario, agregamos los vehiculos:
dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

dealership.register_customers(customer1)
dealership.register_customers(customer2)

#Mostrar Vehiculos Disponibles:
dealership.show_available_vehicle()

#Cliente va ha consultar vehiculo:
customer1.inquire_vehicle(car1)

#Como esta disponible va ha comprar:
customer1.buy_vehicle(car1)

#COn el cliente 2 veo la disponibilidad del car1.
customer2.inquire_vehicle(car1)

#Mostrar Vehiculos Disponibles:
dealership.show_available_vehicle()