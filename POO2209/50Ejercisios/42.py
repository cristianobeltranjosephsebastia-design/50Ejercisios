class Pelicula:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

class Plataforma:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []

    def agregar(self, pelicula):
        self.catalogo.append(pelicula)

netflix = Plataforma("Netflix")
netflix.agregar(Pelicula("Inception", "Sci-Fi"))
print(f"Catálogo de {netflix.nombre}: {[p.titulo for p in netflix.catalogo]}")