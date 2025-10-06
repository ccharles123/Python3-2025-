#Definimos una funcion y la llamamos para que se ejecute:

def greet(name, lastName = "No tiene Apellido"):
    print("Hola mundo", name, lastName)

greet("Carlos", "Hernandez")
greet("Camila")
greet(lastName="Hernandez", name= "Carlos")

#Realizamos la funcion Calculadora:

def add(a, b):
    return a+b

def sustract (a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide (a,b):
    return a/b

def calculator ():
    while True:
        print("Selecciones una operacion:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        option = int(input("Ingresa su opcion (1, 2, 3, 4, 5):"))

        if option == 5:
            print("Saliendo de la calculadora")
            break
        
        if option in [1, 2, 3, 4]:
            num1 = float(input("Ingrese el primer numero:"))
            num2 = float(input("Ingrese el segundo numero:"))

            if option == 1:
                print("La suma de los dos numero ingresados es:", add(num1, num2))
            
            elif option == 2:
                print("La resta de los dos numero ingresados es:", sustract(num1, num2))
            
            elif option == 3:
                print("La multiplicacion de los dos numero ingresados es:", multiply (num1,num2))

            elif option == 4:
                print("La division de los dos numero ingresados es:", divide (num1,num2))

calculator()

        


