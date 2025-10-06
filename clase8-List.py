to_do = ["Ir al hotel",
         "Almorzar",
         "visitar un museo",
         "Regresar al Hotel"]

print(to_do)
print(type(to_do))#el tipo de esta variable lista siempre es list.

#Aunque ingrese en la list diferentes tipos de datos, esta siempre se va ha mantener como list.
mix = ["uno", "dos", 3, 3.14, True, [1,2,3,4]]
print(mix)
print(type(mix))
print(len(mix))#cuantos datos tenemos en la lista.
print("Primer elemento de la lista:", mix[0]) #muestra el primer elemento de la lista.
print("Segundo elemento de la lista:", mix[1]) #muestra el segundo elemento de la lista.
print("Ultimo elemento de la lista:", mix[-1]) #muestra el Ultimo elemento de la lista.
print("segmento de elementos de la lista:", mix[0:3]) #muestra un segmento de elementos sin mostar el ultimo asignado de la lista.
print("segmento de elementos de la lista:", mix[:3]) #muestra un segmento de elementos desde inicio hasta posicion asingnada de la lista.
print("segmento de elementos de la lista:", mix[3:]) #muestra un segmento de elementos desde posicion asignada hasta el final de la lista.

#Metodos

#Agregar un elemento a la lista en el final
separacion = "************"
print(separacion)
mix.append(False)
print(mix)
print(separacion)
mix.append(["a", "b", "c"])
print(mix)

#Agregar un elemento a la lista en la posicion deseada
print(separacion)
mix.insert(1, ["a", "b", "c"])
print(mix)

#Conocer la posicion de un elemento a la lista
print(separacion)
print(mix.index(3.14))

#Imprimir el elemento mayor de una lista
numbers = [1, 2, 3, 4, 5, 90.23, 25]
print(separacion)
print("Mayor:", max(numbers))
print("Menor:", min(numbers))

#Elimiar un elemnto según posicion
print(separacion)
print(numbers)
del numbers[-1]
print(numbers)

#Eliminar un segmento de datos
print(separacion)
print(numbers)
del numbers[:1]
print(numbers)