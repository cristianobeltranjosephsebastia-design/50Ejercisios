import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def circunferencia(self):
        return 2 * math.pi * self.radio

c = Circulo(5)
print("Área del círculo:", c.area())
print("Circunferencia:", c.circunferencia())
