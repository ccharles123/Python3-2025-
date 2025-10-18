#Leer un archivo line por linea
"""with open('caperucitaRoja.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las lineas en una lista:
"""with open('caperucitaRoja.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

#Agregar un texto al archivo:
"""with open('caperucitaRoja.txt', 'a') as file:
    file.write("\n\nBy ChatGPT")"""

#Sobre escribir el texto, importante: Elimina todo y escribe solo lo que le estamos pasando:

with open('caperucitaRoja.txt', 'w') as file:
    file.write("\n\nBy ChatGPT")

# RETO conteo de las lineas del cuento de caperucita
"""with open ('caperucitaRoja.txt', 'r') as file:
    lines = file.readlines()
    print(len(lines))"""