x = 5 #Variable Global
def modify_global():
    global x #toma el valor global externo
    x+=3
    print(f'Vaor modigficado {x}')

modify_global()
print(x)