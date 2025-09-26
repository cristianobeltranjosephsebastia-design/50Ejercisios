class Curso:
    def __init__(self, titulo):
        self.titulo = titulo
        self.estudiantes = []

    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

curso = Curso("Python Avanzado")
alumno = Estudiante("Ana")
curso.inscribir(alumno)
print(f"{alumno.nombre} inscrito en {curso.titulo}")
