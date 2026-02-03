#Variable que no es local ni global (nonlocal)

def outer_function():
    x = 'enclosing'
    def inner_Function():
        nonlocal x
        x = 'modified'
        print(f'el valor del inner es {x}')
    inner_Function()
    print(f'El valor outer {x}')
outer_function()