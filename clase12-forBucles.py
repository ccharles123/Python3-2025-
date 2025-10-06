#con el for puedes ingresar a cada uno de los valores dentro de una lista, Ejemplo:
numbers = [1,2,3,7,5,6]
for i in numbers:
    print("Aqui i es igual a:", i)

#range(n:m): podemos iterar en un rango de datos entre n y m, llega hasta el penultimo numero. ejemplo:
for i in range(10):
    print(i)

#condicional if, para encontrar un elemento dentro de la lista
fruits = ["Manzana", "Pera", "Uva", "Mora"]
for fruit in fruits:
    if fruit != 'Pera':
        print(fruit)
    elif fruit == "Pera":
        print("Pera Encontrada")

#while: mientras se cumpla una condicion entramos en el cuerpo de while. OJO: hay que colocar un limite (break) de lo contrario entra en un bucle infinito. Ejemplo:

x=0
while x <= 5:
    if x == 3:
        break
    print(x)
    x += 1

numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 4:
        break
    print("Aqui i termina cuando es igual a 4:", i)

#continue: se usa para que cuando cumpla una condicion no se ejecute y continue con la siguiente. ejemplo:
numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        continue
    print("Aqui i es no igual a 3:", i)