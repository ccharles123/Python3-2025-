import random

#Vamos a genera un numero entenro aleatorio entre 1 al 10 incluyendo los limites:

random_number = random.randint(1,10)
print(random_number)

#Elegir colores alearotios:

colors = ['Rojo', 'Azul', 'Verde']
random_colors = random.choice(colors)
print(random_colors)

#varajar una lista de cartas:
cards = ['as', 'Rey', 'Reina', 'Jack', '10']
random.shuffle(cards)
print(cards)