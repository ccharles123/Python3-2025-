class Person:
    def __init__(self, name, apellido, cedula, direccion):
        self.name = name
        self.apellido = apellido
        self.cedula = cedula
        self.direccion = direccion

class Student(Person):
    def __init__(self, name, apellido, cedula, direccion):
        super().__init__(name, apellido, cedula, direccion)
        self.matriculado = True

    def retirar(self):
        if self.matriculado:
            self.matriculado = False
            status = "Desvinculado Satisfactoriamente"
        else:
            status = "Desvinculado Anteriormente"
        print(f"El alumno(a) {self.name} - Estatus: {status}")
    
    def ingresar(self):
        if not self.matriculado:
            self.matriculado = True
            print(f"El alumno(a) {self.name} - Fue activada su matricula nuevamente")
        else:
            print(f"El alumno(a) {self.name} - Ya se encuentra Matriculado")

class Teacher(Person):
    def __init__(self, name, apellido, cedula, direccion):
        super().__init__(name, apellido, cedula, direccion)
        self.contratado = True
        self.cursos = []
        self.materias = []
    
class Grados:
    def __init__(self, grado, cupos):
        self.grado = grado
        self.disponible = True
        self.cupos = cupos
        self.students = []
        self.teachers = []

    def asignarAlumnos(self, student : Student):
        if self.disponible:
            if len(self.students) == (self.cupos - 1):
                self.students.append(student)
                self.disponible = False
                print(f"- Alumno {student.name} - Curso Asignado: {self.grado}, PD: Ultimo Cupo asignado al grado")
            elif len(self.students) < self.cupos:
                self.students.append(student)
                print(f"- Alumno {student.name} - Curso Asignado: {self.grado}")
        else:
            print(f"No hay Cupos para el Grado {self.grado}")

    def totalAlumnosGrado (self):
        print(f"Los alumnos matriculados en el grado {self.grado} son:")
        for student in self.students:
            if student.matriculado:
                print(f"- {student.name} {student.apellido} - Id: {student.cedula}")

    def asignarDocente(self, teacher : Teacher):
        if teacher.contratado:
            self.teachers.append(teacher)
            print(f"El profesor {teacher.name} fue asignado al grado {self.grado}")

    def totalDocentes(self):
        print (f"Los docentes que dan clases en el Grado {self.grado} son:")
        for teacher in self.teachers:
            if teacher.contratado:
                print(f"- {teacher.name} {teacher.apellido} - Id: {teacher.cedula}")

    def eliminarGrado(self):
        if self.disponible:
            self.disponible = False
            disponible = "Eliminado Satisfactoriamente"
        else:
            disponible = "No Existe"
        print(f"- Grado {self.grado} - Estatus: {disponible}")

    def activarGrado(self):
        if not self.disponible:
            self.disponible = True
            disponible = "Activado Satisfactoriamente"
        else:
            disponible = "Activo"
        print(f"- Grado: {self.grado} - Estatus: {disponible}")

student1 = Student("Carlos", "Hernandez", 8487634, "Calle 4 17 32")
student2 = Student("Mariana", "Hernandez", 19191919, "Calle 5 32")
student3 = Student("Edimer", "Villarreal", 202029, "Calle 9 12")

teacher1 = Teacher("Betty", "Lopez", 22837884, "Cl 78 24 35")
teacher2 = Teacher("Cherlys", "Dominguez", 39033647, "Cl 30 12 3")

grado6 = Grados("Sexto", 2)
grado7 = Grados("Septimo", 1)

grado6.asignarAlumnos(student1)
grado6.asignarAlumnos(student2)
grado6.asignarAlumnos(student3)

grado7.asignarAlumnos(student3)
grado7.asignarAlumnos(student2)

grado6.asignarDocente(teacher1)
grado7.asignarDocente(teacher2)

grado6.totalAlumnosGrado()
grado6.totalDocentes()

grado7.totalAlumnosGrado()
grado7.totalDocentes()

student1.ingresar()
student1.retirar()
student1.retirar()

grado6.totalAlumnosGrado()

student1.ingresar()
grado6.totalAlumnosGrado()

grado6.eliminarGrado()
grado6.eliminarGrado()

grado6.activarGrado()
grado6.activarGrado()