#al igualar 2 variables, la principal se modifica la dependiente tambien. apuntan en el mismo espacio en memoria.
separador = "****************************"
a = [1,2,3,4,5]
b = a
print(a)
print(b)

del a[0]
print(id(a))
print(id(b))
print(a)
print(b)

#slicing: vamos hacer una nueva variable igualando con a pero con otro id
c = a[:]
print(c)
print(id(c))

# vamos anadir un elemento a la lista a
print(separador)
a.append(6)
print(a)
print(b)
print(c)