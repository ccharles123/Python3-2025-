separador = "***************************************"
#vamos hallar los numeros cuadrados del 1 al 10:
print(separador)
print("***********Numeros Cuadrados***********")
print(separador)

squares = [x**2 for x in range(1,11)]
print("Los resultados son:", squares)

#vamos a pasar celsius a Fahrenheit
print(separador)
print("**********Celsius a Fahrenheit*********")
print(separador)

celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [(temp*9/5)*32 for temp in celsius]
print("Esta es la temperatura en Fahrenheit:", fahrenheit)

#vamos hallar numero pares:
print(separador)
print("*************Numero Pares**************")
print(separador)

events = [x for x in range(1,21) if x%2 == 0]
print(events)

#vamos hallar numero Impares:
print(separador)
print("************Numero Impares*************")
print(separador)

events = [x for x in range(1,21) if x%2 == 1]
print(events)

#vamos hallar la transpuesta de una matrix:
print(separador)
print("**********Transpuesta Matrix***********")
print(separador)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transport = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transport)

#ejercicios
print(separador)
print("**********Ejercicios***********")
print(separador)

numeros = [1, 2, 3, 4, 5]
elDoble = [2*x for x in numeros if x%2 == 0]
print(elDoble)