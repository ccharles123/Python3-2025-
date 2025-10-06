#Los diccionarios se cierran en llaves, almacenan datos con clave y valor, para ver valores solo es llamar a la clave.
numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])

information = {"Nombre": "Carlos",
               "Apellido":"Hernandez",
               "Altura": 1.6,
               "Edad": 40}
print(information)
del information["Edad"]
print(information)
print(information["Nombre"])

#metodo key: podemos ver las llaves del diccionario.
claves = information.keys()
print(claves)
print(type(claves))

#metodo values: podemos ver los valores del diccionario.
values = information.values()
print(values)
print(type(values))

#metodo items: me muestra las claves y sus valores en Tuplas.
items = information.items()
print(items)

#Ejemplo: vamos hacer un diccionario de diccionarios en forma de contactos.
contacts = {"Carlos": {"Apellido":"Hernandez",
               "Altura": 1.7,
               "Edad": 40},
            "Camila":{
                "Apellido":"Fernandez",
                "Altura": 1.65,
                "Edad": 27},
            "Andres":{
                "Apellido":"Lopez",
                "Altura": 1.67,
                "Edad": 30}}
#acceder a todos los datos del diccionario:
print(contacts)

#acceder a solo la informacion de Camila:
print(contacts["Camila"])