#ejemplo de manejo de rrores sen una divicion:

while True:
    try:
        divisor = int(input("ingresar un numero > 0: "))
        result = 100 / divisor
        print("el resultado de la divicion es: ", result)
        break
    except ZeroDivisionError as e:
        print("Error: El numero ingresado no debe ser 0")
        print("Ha ocurrido el siguiente error:", e)
    except ValueError as e:
        print("Error: Debes introducir un numero valido")
        print("Ha ocurrido el siguiente error:", e)