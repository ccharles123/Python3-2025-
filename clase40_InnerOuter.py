x = 'Global' #Variable Global

#Funcion externa:
def outer_function():
    x = 'Enclosing'

    #Funcion Interna
    def inner_function():
        x = 'Local' #Variable Local
        print(x)
    inner_function()
    print(x)
outer_function()
print(x)
