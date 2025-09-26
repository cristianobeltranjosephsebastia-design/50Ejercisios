class Proyecto:
    def __init__(self, titulo, presupuesto):
        self.titulo = titulo
        self.presupuesto = presupuesto

class Freelancer:
    def __init__(self, nombre):
        self.nombre = nombre
        self.proyectos = []

    def postular(self, proyecto):
        self.proyectos.append(proyecto)

proy = Proyecto("Página web", 500)
free = Freelancer("Ana")
free.postular(proy)
print(f"{free.nombre} se postuló a {free.proyectos[0].titulo}")