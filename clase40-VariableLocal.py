def local_function():
    x = 10 #Variable de tipo Local
    print(f'el valor de la variable local es {x}')

local_function()
#print(x) #Genera error, solo se ejecuta dentro de la funcion.

x = 100

def show_global():
    print(f'El valor de la variable global es {x}')
show_global()