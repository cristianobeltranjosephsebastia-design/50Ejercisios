class Estudiante:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__notas = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre:
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("Nombre inválido")

    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)

    @property
    def promedio(self):
        return sum(self.__notas) / len(self.__notas) if self.__notas else 0

alumno = Estudiante("Ana")
alumno.agregar_nota(9)
alumno.agregar_nota(8)
print(f"{alumno.nombre}, Promedio: {alumno.promedio}")