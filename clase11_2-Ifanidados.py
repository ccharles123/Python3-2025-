isMember = False
age = 14
access = 15

if isMember:
    if age >= access:
        print("Eres miembro y cumples con la mayoria de edad de", access, "Puedes Ingresar!")
    else:
        print("Eres miembro pero no cumples con la mayoria de edad de", access, "No Puedes Ingresar!")
else:
    print("No Eres miembro, No Puedes Ingresar!")

#Juego PIEDRA, PAPEL, TIJERAS:

jugador1 = int(input("Jugador 1: PIEDRA:1, PAPEL:2, TIJERAS:3, Selecciona tu juego aqui:"))
jugador2 = int(input("Jugador 2: PIEDRA:1, PAPEL:2, TIJERAS:3, Selecciona tu juego aqui:"))

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == 1):
    if jugador2 == 3:
        print("Gana Jugador 1, PIEDRA gana a TIJERAS")
    else:
        print("Gana Jugador 2, PIEDRA pierde con PAPEL")
elif (jugador1 == 2):
    if jugador2 == 1:
        print("Gana Jugador 1, PAPEL gana a PIEDRA")
    else:
        print("Gana Jugador 2, PAPEL pierde con TIJERAS")
elif (jugador1 == 3):
    if jugador2 == 2:
        print("Gana Jugador 1, TIJERAS gana a PAPEL")
    else:
        print("Gana Jugador 2, TIJERAS pierde con PIEDRA")
        

