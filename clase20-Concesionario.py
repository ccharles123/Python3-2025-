class Vehiculo:

    def __init__(self, idVehiculo, marca, modelo, precio):
        self.idVehiculo = idVehiculo
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(
                f"Vehículo id {self.idVehiculo} | {self.marca} {self.modelo} "
                f"fue vendido por ${self.precio:,.0f}")
        else:
            print(
                f"El vehículo {self.marca} {self.modelo} ya fue vendido (no disponible)")
    
    def devolucion(self):
        if not self.disponible:
            self.disponible = True
            print(f"Vehiculo de marca {self.marca} modelo {self.modelo} fue devuelto al concesionario")
        else:
            print(f"Vehiculo de Marca: {self.marca} Modelo: {self.modelo} se encuentra en inventario")

class Cliente:
    def __init__(self, idCliente, nombre):
        self.idCliente = idCliente
        self.nombre = nombre
        self.vehiculosCliente = []

    def compra(self, vehiculo : Vehiculo):
        if vehiculo.disponible:
            vehiculo.vender()
            self.vehiculosCliente.append(vehiculo)
            print(f"{self.nombre} ahora posee el {vehiculo.marca} {vehiculo.modelo}")
        else:
            print(
                f"El vehículo {vehiculo.marca} {vehiculo.modelo} no está disponible para la venta"
            )

    def devolver(self, vehiculo : Vehiculo):
            if vehiculo in self.vehiculosCliente:
                vehiculo.devolucion()
                self.vehiculosCliente.remove(vehiculo)
                print(f"{self.nombre} devolvió el {vehiculo.marca} {vehiculo.modelo}")
            else:
                print(
                    f"{self.nombre} no tiene registrado el vehículo {vehiculo.marca} {vehiculo.modelo}"
                )
    
    def vehiculoCliente(self):
        print(f"los vehiculos comprados por el cliente {self.nombre} son:")
        for vehiculo in self.vehiculosCliente:
                print(f"Vehiculo {vehiculo.marca} - {vehiculo.modelo}")

class Concesionario:
    def __init__(self):
        self.vehiculos = []
        self.clientes = []
    
    def adicionarVehiculo(self, vehiculo : Vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"El vehiculo {vehiculo.marca} {vehiculo.modelo} fue agregado al inventario")

    def adicionarCliente(self, cliente : Cliente):
        self.clientes.append(cliente)
        print(f"El Cliente {cliente.nombre} fue agregado al listado de clientes")

    def vehiculosDisponibles(self):
        print(f"los vehiculos disponibles son:")
        for vehiculo in self.vehiculos:
            if vehiculo.disponible:
                print(f"Vehiculo {vehiculo.marca} - {vehiculo.modelo}")



#Creamos vehiculo y cliente:
v1 = Vehiculo(1, "Toyota", "Corolla", 85000000)
v2 = Vehiculo(2, "Mazda", "3", 95000000)
v3 = Vehiculo(3, "BYD", "2025", 125000000)
c1 = Cliente(1,"Carlos")
c2 = Cliente(2, "Mariana")

concesionario = Concesionario()

concesionario.adicionarVehiculo(v1)
concesionario.adicionarVehiculo(v2)
concesionario.adicionarVehiculo(v3)
concesionario.adicionarCliente(c1)
concesionario.adicionarCliente(c2)

c1.compra(v1)
c1.compra(v1)
c1.vehiculoCliente()

c2.compra(v1)
c2.compra(v2)
c2.vehiculoCliente()

concesionario.vehiculosDisponibles()

c1.devolver(v2)
c1.devolver(v1)

c2.devolver(v1)
c2.devolver(v2)

concesionario.vehiculosDisponibles()

c1.compra(v3)