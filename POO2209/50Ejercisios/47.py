class Pedido:
    def __init__(self, codigo, destino):
        self.codigo = codigo
        self.destino = destino
        self.entregado = False

    def entregar(self):
        self.entregado = True

pedido = Pedido("X123", "Bogotá")
pedido.entregar()
print(f"Pedido {pedido.codigo} entregado:", pedido.entregado)