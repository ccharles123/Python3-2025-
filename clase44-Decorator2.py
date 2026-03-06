def check_access(func):
    def wrapper(employee):
        #COmprobar si el empledo tiene rol 'admin'.
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('ACCESO DENEGADO. Solo los administradores pueden acceder.')
    return wrapper

@check_access
def delete_employee (employee):
    print(f"El empledo {employee['name']} ha sido eliminado")


admin = {
    'name': 'Carlos', 
    'role': 'admin'
}

employee = {
    'name': 'Ana', 
    'role': 'employee'
}

#delete_employee(admin)
#delete_employee(employee)

#Ejemplo

def check_action(func):
    def wrapper(employee):
        #COmprobar si el empledo tiene rol 'orador'.
        if employee.get('role') == 'orador':
            return func(employee)
        else:
            print('ACCESO DENEGADO. Solo los oradores pueden hablar.')
    return wrapper

@check_action
def log_employee_acction(employee):
    print(f'El empleado {employee["name"]} es orador y puede hablar')

orador = {
    'name': 'Carlos', 
    'role': 'orador'
}

employee = {
    'name': 'Ana', 
    'role': 'employee'
}

log_employee_acction(orador)
#log_employee_acction(employee)