X = 10
Y = 10
Z = 20

#El If se usa para comparar una condicional, elif para agregar mas condicionales, else se coloca en el final sino se cumplen las demas.
if X > Y:
    print(X, "es mayor que", Y)
elif X == Y:
    print(X, "es igual que", Y)
else:
    print(X, "es menor que", Y)

# AND: se ultiliza para mezclar dos variables y si se cumplen las dos ingresa.
if X > Z and Y > Z:
    print(X, "y", Y, "son mayores que", Z)
elif X < Z and Y < Z:
    print(X, "y", Y, "son menores que", Z)
elif X == Z and Y == Z:
    print(X, "y", Y, "son iguales que", Z)
else:
    print("O", X, "ó", Y, "no cumplen con las condiones")

# OR: se ultiliza para mezclar dos variables y si UNA se cumple ingresa al condicional.
if X > Z or Y > Z:
    print(X, "o", Y, "es mayor que", Z)
elif X < Z or Y < Z:
    print(X, "o", Y, "son menores que", Z)
elif X == Z or Y == Z:
    print(X, "o", Y, "son iguales que", Z)
else:
    print("Ni", X, "Ni", Y, "cumplen con las condiones")


#NOT: sirve para negar una condicion:
if not X > Y and not X == Y:
    print(X, "no es mayor que", Y)
elif not X < Y and not X == Y:
    print(X, "no es menor que", Y)
else:
    print(X, "es igual que", Y)