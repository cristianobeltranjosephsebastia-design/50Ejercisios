class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
        self.publicaciones = []

    def agregar_amigo(self, usuario):
        self.amigos.append(usuario)

    def publicar(self, texto):
        self.publicaciones.append(texto)

u1 = Usuario("Pedro")
u2 = Usuario("Maria")
u1.agregar_amigo(u2)
u1.publicar("Hola, este es mi primer post en la red social.")
print(f"{u1.nombre} tiene {len(u1.amigos)} amigo(s).")