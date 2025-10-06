#Sirve para iterar cada uno de los elementos pero sin utilizar indices. Ejemplo de Iterador:
separador = "*****************************"
print(separador)
print("Iterador de Listas")
print(separador)


#Crear una lista
list = [1,2,3,4]

#Obtener el Iterador: 
iterList = iter(list)

#Usar el iterador (utilizando la palabra next() vamos ingresando a cada uno de los valores de la list):
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(separador)

#Iterador de Cadenas
print("Iterador de Cadenas")
print(separador)
text = "Hola mundo"
iter_text = iter(text)

for char in iter_text:
    print(char)

print(separador)

#Iterador para numeros impares.
print("numeros impares")
print(separador)
#creamos un limite:
limit = 10

#Crear Iterador: utilizamos range(inicio, final, frecuencia)
imparIter = iter(range(1, limit+1, 2))

#Usar el iterador:
for num in imparIter:
    print(num)

print(separador)
#Iterador para numeros pares.
print("numeros pares")
print(separador)
#creamos un limite:
limitPar = 10

#Crear Iterador: utilizamos range(inicio, final, frecuencia)
parIter = iter(range(0, limitPar+1, 2))

#Usar el iterador:
for num in parIter:
    print(num)

print(separador)
#GENERADOR: funcion que genera una secuencia de numeros que podemos iterar.
print("Generador")
print(separador)
#creamos la funcion generador:
def my_generador():
    yield 1
    yield 2
    yield 3

for value in my_generador():
    print(value)