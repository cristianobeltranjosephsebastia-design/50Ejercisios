class Avatar:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mundo = None

    def entrar(self, mundo):
        self.mundo = mundo
        mundo.usuarios.append(self)

class MundoVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []

meta = MundoVirtual("MetaWorld")
user = Avatar("Sebas")
user.entrar(meta)
print(f"{user.nombre} entró a {meta.nombre} con {len(meta.usuarios)} usuario(s).")