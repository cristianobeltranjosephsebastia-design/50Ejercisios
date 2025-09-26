import random
class Accion:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def fluctuacion(self):
        self.precio += random.randint(-5, 5)

apple = Accion("AAPL", 150)
for _ in range(3):
    apple.fluctuacion()
    print(f"{apple.nombre}: ${apple.precio}")