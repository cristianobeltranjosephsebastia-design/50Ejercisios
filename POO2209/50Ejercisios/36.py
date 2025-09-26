class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def total(self):
        return sum(p.precio * c for p, c in self.items)

p1 = Producto("Laptop", 1000)
p2 = Producto("Mouse", 50)
carrito = Carrito()
carrito.agregar(p1, 1)
carrito.agregar(p2, 2)
print("Total e-commerce:", carrito.total())