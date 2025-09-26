class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

class Tarea:
    def __init__(self, descripcion, responsable):
        self.descripcion = descripcion
        self.responsable = responsable
        self.completada = False

    def completar(self):
        self.completada = True

proj = Proyecto("App Móvil")
proj.agregar_tarea(Tarea("Diseño UI", "Laura"))
proj.agregar_tarea(Tarea("Backend API", "Carlos"))
for t in proj.tareas:
    print(f"{t.descripcion} - {t.responsable} - {'✔' if t.completada else '✘'}")