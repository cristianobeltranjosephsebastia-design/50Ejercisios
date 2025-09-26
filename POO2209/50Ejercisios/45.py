class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Hospital:
    def __init__(self):
        self.pacientes = []

    def ingresar(self, paciente):
        self.pacientes.append(paciente)

hospital = Hospital()
hospital.ingresar(Paciente("Carlos", 40))
print("Pacientes ingresados:", [p.nombre for p in hospital.pacientes])