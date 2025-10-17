class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello. I'm person {self.name}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Mi Student Id es {self.student_id}")


student1 = Student("Carlos", 40, "001")
student2 = Student("Mariana", 12, "002")

person1 = Person("Edimer", 35)

# Probar método
student1.greet()
student2.greet()

person1.greet()