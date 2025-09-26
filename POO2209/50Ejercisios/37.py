class Habitacion:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.disponible = True

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, hab):
        self.habitaciones.append(hab)

    def reservar(self, numero):
        for hab in self.habitaciones:
            if hab.numero == numero and hab.disponible:
                hab.disponible = False
                return f"Habitación {numero} reservada."
        return "No disponible"

hotel = Hotel("Gran Hotel")
hotel.agregar_habitacion(Habitacion(101, 120))
hotel.agregar_habitacion(Habitacion(102, 80))
print(hotel.reservar(101))