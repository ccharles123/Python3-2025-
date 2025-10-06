#definimos una matrix:
print("*****matriz*****")
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
print("la posicion zero:", matrix[0])
#vamos a imprimir el numero 8 ([fila], [columna]):
print(matrix[2][1])

#tuplas: son inmutables, no se pueden modificar a diferencia de la matriz.
print("*****tuplas*****")
numbers = 1,2,3,4,5
print(type(numbers))
print(numbers)
#numbers[0]= 0
#print(numbers)