#Generador Fibonacci
#0 1 1 2 3 5 8 13 21...
separador = "********************"
print(separador)
print("Fibonacci")
print(separador)

#creamos la funcion para un limite:
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

#utilizamos for para ejecutar la funcion fibonacci(limit):
for num in fibonacci(14):
    print(num)