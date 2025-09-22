class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.nombre} - Tel: {self.telefono}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, contacto):
        self.contactos.append(contacto)

    def buscar(self, nombre):
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                return c
        return "No encontrado"

agenda = Agenda()
agenda.agregar(Contacto("Ana", "324243", "ana874@mail.com"))
agenda.agregar(Contacto("Luis", "983242", "luis1121@mail.com"))

print(agenda.buscar("Ana"))
print(agenda.buscar("Pedro"))