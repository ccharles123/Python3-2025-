#ejemplo de manejo de rrores sen una divicion:
"""
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
        print("Ha ocurrido el siguiente error:", e)"""


while True:
    try:
        entrada = input("Ingresa un número > 0 (o escribe 'salir' para terminar): ")

        # 🧠 Centinela: si el usuario escribe "salir", rompe el ciclo
        if entrada.lower() == "salir":
            print("Programa finalizado por el usuario.")
            break

        divisor = int(entrada)  # convierte la entrada a número

        if divisor <= 0:
            print("Error: el número debe ser mayor que 0.")
            continue  # vuelve a pedir otro número

        result = 100 / divisor
        print("El resultado de la división es:", result)
        break  # sale si todo está correcto

    except ZeroDivisionError as e:
        print("Error: el número ingresado no debe ser 0.")
        print("Ha ocurrido el siguiente error:", e)

    except ValueError as e:
        print("Error: Debes introducir un número válido.")
        print("Ha ocurrido el siguiente error:", e)
