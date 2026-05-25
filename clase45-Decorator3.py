#Ejemplo de decoradores anidados, un empleado quiere eliminar a otro pero solo lo puede hacer si es Admin.


#Decorador que comprueba si un empleado tiene un rol especifico.
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            #Si el rol del empleado coincide con el rol requerido.
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'ACCESO DENEGADO. Solo los {required_role} pueden realizar esta accion.')
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f"Registrando accion para el empleado {employee['name']}")
        return func(employee)
    return wrapper


@check_access('admin')
@log_action
def delete(employee):
    print(f"El empledo {employee['name']} ha sido Eliminado con Exito.")


admin = {
    'name': 'Carlos', 
    'role': 'admin'
}

employee = {
    'name': 'Ana', 
    'role': 'employee'
}

delete(admin)

#Otro Ejemplo de un payaso que hace reir ninos, pero solo se rien si el payaso es gracioso.

def check_gracioso(required_role):
    def decorador2(func2):
        def wrapper(payaso):
            if payaso.get('smile') == required_role:
                return func2(payaso)
            else:
                print(f'EL payaso {payaso['name']} no hizo reir a los ninos. Solo los payasos {required_role} pueden hacer reir')
        return wrapper
    return decorador2



@check_gracioso('payaso')
#@log_action
def smile(person):
    print(f'EL payaso {person['name']} hizo reir a los ninos')

payaso = {
    'name': 'Carlos', 
    'role': 'admin'
}

nino = {
    'name': 'Ana', 
    'role': 'employee'
}