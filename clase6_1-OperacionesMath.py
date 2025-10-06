a = 10
b = 3
print("Suma:", a + b)
print("Resta:",a - b)
print("Multiplicacion:",a * b)
print("Potenciacion:",a ** b)

print("Division:",a / b)
print("Parte Entera de la Division:",a // b)
print("Modulo:",a % b)

#agregamos a la variable y luego imprimimos

a= a + 2
print("Nuevo resultado de a:",a)

a += 2
print("Nuevo segundo resultado de a:",a)

a -= 2
print("Nuevo resultado resta de a:",a)

a *= 2
print("Nuevo resultado Multiplicacion de a:",a)

a /= 6
print("Nuevo resultado Division de a:",a)

#REgla PEMDAS (Parentesis, Exponente, Multiplicacion, Division, Adicion, Sustraccion) Ejemplo:
operation_1 = 2 + 5 * 3
operation_2 = (2 + 5) * 3
operation_3 = (2+3) * (4**2)/8 - 1
print("Resultado automatico con PEMDAS:", operation_1)
print("Resultado Agregando parentisis con PEMDAS:", operation_2)
print("Resultado automatico con PEMDAS:", operation_3)