name = "Carli"
serparador = "***************"
lastName = "   Hernandez Lopez"

print(type(name))

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print(serparador)
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])

print(serparador)
print(name + " " + lastName)
print((name + " ") * 5)

print(serparador)
print(len(name))
print(len(lastName))
print(len(name))

print(serparador)
name2= "CARLOS"
print(name2.lower())
print(name.upper())
print(lastName)
print(lastName.strip())#quita los espacio de adelante.

print(serparador)
print("Nunca", "pares", "de", "aprender") #La coma dentro de la función print se usa para separar varios argumentos. Al hacerlo, Python añade automáticamente un espacio entre los argumentos.

print(serparador)
print("Nunca", "pares", "de", "aprender", sep="* ") #El parámetro sep permite especificar cómo separar los elementos al imprimir. 

#4. Uso de end
#El parámetro end cambia lo que se imprime al final de la llamada a print. En lugar de imprimir cada mensaje en una nueva línea, end="" asegura que “Nunca” y “pares” se impriman en la misma línea, resultando en “Nunca pares”. Por defecto, end es un salto de línea ("\n"), lo que hace que cada llamada a print comience en una nueva línea.

print(serparador)
print("Nunca", end=" ")
print("pares de aprender")

#5. Impresión de variables
#Puedes usar print para mostrar el valor de las variables. En este ejemplo, imprimirá “Frase: Nunca pares de aprender” y “Autor: Platzi”. Esto es útil para depurar y ver los valores de las variables en diferentes puntos de tu programa.

print(serparador)
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

#6. Uso de formato con f-strings
#Las f-strings permiten insertar expresiones dentro de cadenas de texto. Al anteponer una f a la cadena de texto, puedes incluir variables directamente dentro de las llaves {}. En este ejemplo, frase y author se insertarán en la cadena, resultando en “Frase: Nunca pares de aprender, Autor: Platzi”. Esto hace que el código sea más legible y fácil de escribir.
print(serparador)
print(f"Frase: {frase}, Autor: {author}")

#7. Uso de formato con format
#El método format es otra forma de insertar valores en cadenas de texto. Usando {} como marcadores de posición, puedes pasar los valores que quieres insertar como argumentos de format. En este ejemplo, se imprimirá “Frase: Nunca pares de aprender, Autor: Platzi”. Es una forma flexible y poderosa de formatear cadenas, aunque las f-strings son más concisas.
print(serparador)
print("Frase:{}, Autor:{}".format(frase, author))

#8. Impresión con formato específico
#Puedes controlar el formato de los números al imprimir. En este ejemplo, :.2f indica que el número debe mostrarse con dos decimales. Así, imprimirá “Valor: 3.14”, redondeando el número a dos decimales. Esto es especialmente útil cuando trabajas con datos numéricos y necesitas un formato específico.
valor = 3.1416
print(serparador)
print("Valor: {:.2f}".format(valor))

#9. Saltos de línea y caracteres especiales
#Los saltos de línea en Python se indican con la secuencia de escape \n. Por ejemplo, para imprimir “Hola\nmundo”, que aparecerá en dos líneas:
print(serparador)
print("Hola\nmundo")

#Para imprimir una cadena que contenga comillas simples o dobles dentro de ellas, debes usar secuencias de escape para evitar confusiones con la sintaxis de Python. Por ejemplo, para imprimir la frase “Hola soy ‘Carli’”:
print(serparador)
print('Hola soy \'Carli\'')

#Si necesitas imprimir una ruta de archivo en Windows, que incluya barras invertidas, también necesitarás usar secuencias de escape para evitar que Python interprete las barras invertidas como parte de secuencias de escape. Por ejemplo:
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
print(serparador)


