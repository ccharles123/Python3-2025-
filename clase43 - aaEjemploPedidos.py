from collections import deque, Counter, defaultdict
from enum import Enum

# 1️⃣ Estados del pedido (agregamos PREPARACION)
class Estado(Enum):
    PENDIENTE = 1
    PREPARACION = 2
    LISTO = 3
    ENTREGADO = 4

# 2️⃣ Estructuras
cola = deque()
ventas = defaultdict(int)

# 3️⃣ Crear pedido
def crear_pedido(cliente, productos):
    pedido = {
        "cliente": cliente,
        "productos": productos,
        "estado": Estado.PENDIENTE
    }
    cola.append(pedido)
    print(f"Pedido creado para {cliente}")

# 4️⃣ Pasar a PREPARACION
def iniciar_preparacion():
    if cola:
        pedido = cola[0]
        pedido["estado"] = Estado.PREPARACION
        print(f"Pedido de {pedido['cliente']} está en PREPARACION")
    else:
        print("No hay pedidos")

# 5️⃣ Marcar LISTO
def marcar_listo():
    if cola:
        pedido = cola[0]
        pedido["estado"] = Estado.LISTO
        print(f"Pedido de {pedido['cliente']} está LISTO")
    else:
        print("No hay pedidos")

# 6️⃣ Entregar pedido
def entregar_pedido():
    if cola:
        pedido = cola.popleft()
        pedido["estado"] = Estado.ENTREGADO
        
        conteo = Counter(pedido["productos"])
        for producto, cantidad in conteo.items():
            ventas[producto] += cantidad
        
        print(f"Pedido entregado a {pedido['cliente']}")
    else:
        print("No hay pedidos")

# 7️⃣ Ver ventas
def ver_ventas():
    print("Ventas totales:")
    for producto, cantidad in ventas.items():
        print(producto, ":", cantidad)


# 🔥 PRUEBA
crear_pedido("Carlos", ["hamburguesa", "papitas", "papitas"])
crear_pedido("Mariana", ["Pizza", "papitas", "hamburguesa"])
iniciar_preparacion()
marcar_listo()
entregar_pedido()
ver_ventas()

iniciar_preparacion()
marcar_listo()
entregar_pedido()   
ver_ventas()
