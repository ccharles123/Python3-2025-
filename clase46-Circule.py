class Circle:

    def __init__(self, radius:float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.1416 * (self._radius **2)
    
    @property
    def radius(self) -> float:
        return self._radius 
    
    @radius.setter
    def radius(self, value:float):
        if value < 0:
            raise ValueError('El radio no puede ser negativo')
        self._radius = value


class Cuadrado:

    def __init__(self, lado:float):
        self._lado = lado

    @property
    def area(self) -> float:
        return self._lado **2
    
    @property
    def lado(self) -> float:
        return self._lado
    
    @lado.setter
    def lado(self, value: float):
        if value < 0:
            raise ValueError('El lado no puede ser negativo')
        self._lado = value

#circle = Circle(5)
#print(circle.area)
#print(circle.radius)
#circle.radius = -10
#print(circle.area)
#print(circle.radius)


cuadrado = Cuadrado(3)
print(cuadrado.area)
print(cuadrado.lado)
cuadrado.lado = 10
print(cuadrado.area)
print(cuadrado.lado)