class Animal:
    def __init__(self, especie, energia=100):
        self.especie = especie
        self.energia = energia

    def comer(self):
        self.energia += 20

    def moverse(self):
        self.energia -= 10
zorro = Animal("Zorro")
zorro.moverse()
zorro.comer()
print(f"{zorro.especie} energía: {zorro.energia}")