class Servivo:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} esta respirando...")

class Person(Servivo):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        print(f"Hola, soy {self.name} y tengo {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old, my student id: {self.student_id}")

student1 = Student("Carlos", 40, "SP001")

student1.introduce()
student1.speak()
student1.breathe()