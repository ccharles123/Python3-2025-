def calcular_promedio(numbers):
    """
    Calcula el promedio de una lista de números.

    Parameters:
    numbers (list): Lista de enteros o flotantes.

    Returns:
    float: El promedio de los números en la lista.
    """
    return sum(numbers) / len(numbers)

print(calcular_promedio([1,2,3,4,5]))

#Calcular el area:

def calculate_area(base, height):
    """
    Calcula el Area de un Triangulo
    """
    #Multiplicamos la base por la altura y se divide entre 2
    return (base * height) / 2


print(calculate_area(4,4))