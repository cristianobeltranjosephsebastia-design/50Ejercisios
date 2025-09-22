class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return f"Venta realizada. Stock restante: {self.stock}"
        return "Stock insuficiente"

    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

prod = Producto("Camiseta", 25.0, 10)
print(prod)
print(prod.vender(3))
print(prod)