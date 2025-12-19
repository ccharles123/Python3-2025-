x = 5 #Variable Global
def modify_global():
    global x
    x+=3
    print(f'Vaor modigficado {x}')

modify_global()
print(x)