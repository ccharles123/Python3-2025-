from __future__ import annotations
from typing import List, Dict, Optional
from dataclasses import dataclass, field


# ---------- Entidades base ----------

@dataclass(eq=True, frozen=True)
class Subject:
    """Materia (Matemáticas, Inglés, etc.)."""
    nombre: str


@dataclass(eq=True, frozen=True)  # ✅ ARREGLO: ahora Teacher es hashable (inmutable)
class Teacher:
    """Docente: puede dictar varias materias."""
    nombre: str
    apellido: str

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"


@dataclass
class Grade:
    """Calificación de 1.0 a 5.0."""
    valor: float
    periodo: Optional[str] = None
    comentario: Optional[str] = None

    def __post_init__(self):
        if not (1.0 <= float(self.valor) <= 5.0):
            raise ValueError(f"Calificación fuera de rango (1.0 a 5.0): {self.valor}")
        self.valor = round(float(self.valor), 2)


@dataclass
class Student:
    """Estudiante con registro por curso."""
    nombre: str
    apellido: str
    salon: Optional["Classroom"] = None
    _records: Dict["Course", "StudentRecord"] = field(default_factory=dict, init=False, repr=False)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def record_for(self, course: "Course") -> "StudentRecord":
        if course not in self._records:
            self._records[course] = StudentRecord(self, course)
        return self._records[course]

    @property
    def boletin(self) -> Dict[str, float]:
        return {rec.curso.materia.nombre: rec.promedio for rec in self._records.values()}


@dataclass
class Classroom:
    """Salón/Grado (1° a 11°) con estudiantes y cursos ofrecidos."""
    grado: int  # 1..11
    etiqueta: str
    estudiantes: List[Student] = field(default_factory=list)
    cursos: List["Course"] = field(default_factory=list)

    def agregar_estudiante(self, estudiante: Student):
        estudiante.salon = self
        self.estudiantes.append(estudiante)

    def ofrecer_curso(self, curso: "Course"):
        self.cursos.append(curso)


@dataclass(eq=True, frozen=True)
class Course:
    """
    'Curso' = Materia dictada por un docente en un salón específico.
    """
    materia: Subject
    docente: Teacher     # ✅ ahora Teacher es hashable, por lo que Course también
    salon_id: int

    def __str__(self) -> str:
        return f"{self.materia.nombre} (Grado {self.salon_id}) - {self.docente}"


@dataclass
class StudentRecord:
    """Relación Estudiante-‘Curso’ con calificaciones."""
    estudiante: Student
    curso: Course
    calificaciones: List[Grade] = field(default_factory=list)

    def registrar_nota(self, valor: float, periodo: Optional[str] = None, comentario: Optional[str] = None):
        self.calificaciones.append(Grade(valor, periodo, comentario))

    @property
    def promedio(self) -> float:
        if not self.calificaciones:
            return 0.0
        return round(sum(g.valor for g in self.calificaciones) / len(self.calificaciones), 2)


# ---------- Agregador: Escuela ----------

class School:
    """Agregador principal: administra docentes, materias, salones, cursos y matrículas."""
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.docentes: List[Teacher] = []
        self.materias: Dict[str, Subject] = {}
        self.salones: Dict[int, Classroom] = {}
        self._inicializar_salones()

    def _inicializar_salones(self):
        for grado in range(1, 12):  # 1..11
            etiqueta = (
                f"{grado}° Primaria" if grado <= 5
                else (f"{grado}° Secundaria" if 6 <= grado <= 9 else f"{grado}° Bachillerato")
            )
            self.salones[grado] = Classroom(grado, etiqueta)

    def agregar_docente(self, nombre: str, apellido: str) -> Teacher:
        t = Teacher(nombre, apellido)
        self.docentes.append(t)
        return t

    def agregar_materia(self, nombre: str) -> Subject:
        nombre_norm = nombre.strip().title()
        if nombre_norm not in self.materias:
            self.materias[nombre_norm] = Subject(nombre_norm)
        return self.materias[nombre_norm]

    def ofrecer_curso(self, grado: int, nombre_materia: str, docente: Teacher) -> Course:
        salon = self.salones[grado]
        materia = self.agregar_materia(nombre_materia)
        curso = Course(materia, docente, salon_id=grado)
        salon.ofrecer_curso(curso)
        return curso

    def matricular_estudiante(self, grado: int, nombre: str, apellido: str) -> Student:
        salon = self.salones[grado]
        alumno = Student(nombre, apellido)
        salon.agregar_estudiante(alumno)
        return alumno

    def inscribir_en_curso(self, estudiante: Student, curso: Course) -> StudentRecord:
        if estudiante.salon is None or estudiante.salon.grado != curso.salon_id:
            raise ValueError("El estudiante debe pertenecer al mismo salón (grado)")