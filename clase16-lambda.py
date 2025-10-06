add = lambda a, b: a + b
print(add(10, 6))

sustrat = lambda a, b: a - b
print(sustrat(10, 4))

multiply = lambda a, b: a * b
print(multiply(10, 4))

#Obtener el cuadrado de cada numero de un rango del 0 al 10

numbers = range(11)
cuadrado = list(map(lambda x: x**2, numbers))
print("el cuadrado es:", cuadrado)

#Obtener el cuadrado de cada numero de un rango del 0 al 10, utilizando comprehension list:

numbers = range(11)
cuadrado = [x**2 for x in numbers]
print("el cuadrado es:", cuadrado)

#Obtener el cuadrado de cada numero de un rango del 0 al 10, utilizando Usando un bucle for clásico:

numbers = range(11)
cuadrado = []
for x in numbers:
    cuadrado.append(x**2)

print("el cuadrado es:", cuadrado)

# Obtener los numeros pares:
pares = list(filter(lambda x: x%2 == 0, numbers))
print("los numero pares son:", pares)