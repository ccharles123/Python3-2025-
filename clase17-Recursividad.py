#hallamos el factorial de un numero, ejemplo 5! = 5*4*3*2*1, por medio de la siguiente funcion:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_5 = print(factorial(5))

#aplicamos la recursividad en la serie de fibonacci:

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

numbers = 11
print("el resultado del fibonacci es:", fibonacci(numbers))

#aplicamos la recursividad en la serie de sumatoria consecutiva de numero enteros:

def sumatoria(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sumatoria(n-1)
    
numero = 4
print("el resultado de la sumatoria es:", sumatoria(numero))