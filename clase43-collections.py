####Defaultdict#### es una extensión del método predeterminado dict, que permite asignar valores por defecto para claves inexistentes. 


from collections import defaultdict

def contar_productos(ordenes):
    product_count = defaultdict(int)
    for orden in ordenes:
        product_count[orden] += 1
    return product_count

ordenes = ['laptop', 'smartphone', 'laptop', 'tablet', 'tablet', 'tablet']
resultado = contar_productos(ordenes)
print(resultado)  # Output: defaultdict(<class 'int'>, {'laptop': 2, 'smartphone': 1, 'tablet': 3})



####Counter#### es una herramienta poderosa para contar ocurrencias de elementos en listas. Permite hacer sumatorias directas y es particularmente útil para estadísticas y análisis de datos.

from collections import Counter

def contar_ventas(productos):
    return Counter(productos)

productos = ['laptop', 'smartphone', 'smartphone', 'laptop', 'tablet', 'laptop','laptop']
resultado = contar_ventas(productos)
print(resultado)  # Output: Counter({'laptop': 2, 'smartphone': 2, 'tablet': 1})



####Las colas (deques)#### ofrecen una estructura ideal para manejar flujos de datos donde el orden de entrada importa. En Python, deque ofrece operaciones eficientes de O(1) tanto para agregar como para quitar elementos de ambos extremos de la cola.
from collections import deque


def manejar_ordenes():
    ordenes = deque(['orden1', 'orden2', 'orden3'])
    ordenes.append('orden4')  # Añadir al final
    ordenes.appendleft('orden0')  # Añadir al inicio
    print(ordenes)  # Output: deque(['orden0', 'orden1', 'orden2', 'orden3', 'orden4'])
    ordenes.pop()  # Eliminar del final
    ordenes.popleft()  # Eliminar del inicio
    print(ordenes)  # Output: deque(['orden1', 'orden2', 'orden3'])

manejar_ordenes()



####Las enumeraciones#### permiten definir constantes de manera clara y organizada, mejorando la legibilidad del código y reduciendo errores.

from enum import Enum

class EstadoOrden(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3

def verificar_estado_orden(status):
    if status == EstadoOrden.PENDIENTE:
        return "La orden está pendiente."
    elif status == EstadoOrden.ENVIADO:
        return "La orden ha sido enviada."
    elif status == EstadoOrden.ENTREGADO:
        return "La orden ha sido entregada."

estado_actual = EstadoOrden.ENTREGADO 
print(verificar_estado_orden(estado_actual))  # Output: La orden ha sido enviada.