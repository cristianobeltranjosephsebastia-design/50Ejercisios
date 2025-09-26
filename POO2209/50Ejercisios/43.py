class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, cantidad):
        self.productos[nombre] = self.productos.get(nombre, 0) + cantidad

    def stock_bajo(self):
        return {p: c for p, c in self.productos.items() if c < 5}

inv = Inventario()
inv.agregar("Manzanas", 3)
inv.agregar("Peras", 10)
print("Stock bajo:", inv.stock_bajo())