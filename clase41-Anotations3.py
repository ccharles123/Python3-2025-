class Employee:
    name: str
    age : str
    salary: float

    def __init__(self, name: str, age : str, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f'Hola, me llamo {self.name}, tengo {self.age} años y gano {self.salary}'

employee1 = Employee('Carlos', '40', 3500.0)
print(employee1.introduce())