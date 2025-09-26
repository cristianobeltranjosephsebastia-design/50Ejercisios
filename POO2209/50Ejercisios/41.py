class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")

c1 = Cuenta("Sofia", 1000)
c1.depositar(500)
c1.retirar(200)
print("Saldo actual:", c1.saldo)