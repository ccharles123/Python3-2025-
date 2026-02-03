# Código lento y poco eficiente
numeros = [1, 2, 3, 4, 5]
cuadrados = []
for numero in numeros:
    cuadrados.append(numero ** 2)
print(cuadrados)


# Código Pytónico usando list comprehension
cuadrados = [numero ** 2 for numero in numeros]
print(cuadrados)

