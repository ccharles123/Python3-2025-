def divide(a:int, b:int) -> float:
    #Validar que ambos parametros sean enteros.
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos parametros deben ser enteros o flotantes')
    if b == 0:
        raise ValueError ('El divisor no puede ser cero')
    
    return print(f'La operacion de la resta es {a/b}')

#res1 = divide(10, "10")
#res2 = divide(10, 0)
#res3 = divide(10, 10)

#Ejemplo de uso:
try:
    res = divide(10,'2') #Error de tipo
    print(res)
except TypeError as e:
    print(f'ERROR: {e}')

try:
    res = divide(10,0) #Error de division por cero
    print(res)
except ValueError as e:
    print(f'ERROR: {e}')

try:
    res = divide(10,2) #Division correcta
    print(res)
except (ValueError, TypeError) as e:
    print(f'ERROR: {e}')