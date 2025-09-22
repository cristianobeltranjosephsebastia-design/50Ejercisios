class animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print(f"El animal {self.nombre} hace un sonido")

class Perro(animal):
    def ladrar(self):
        return(f"El perro {self.nombre} ladra")

perro = Perro("Firulaisss")
Gato = animal("Michigatsu")

perro.hacer_sonido()
Gato.hacer_sonido()

print(perro.ladrar())

# ======================================
# Ejercicio 36: E-commerce Completo
# ======================================
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


# ======================================
# Ejercicio 37: Sistema de Gestión Hotelera
# ======================================
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


# ======================================
# Ejercicio 38: Plataforma de Cursos Online
# ======================================
class Curso:
    def __init__(self, titulo):
        self.titulo = titulo
        self.estudiantes = []

    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

curso = Curso("Python Avanzado")
alumno = Estudiante("Ana")
curso.inscribir(alumno)
print(f"{alumno.nombre} inscrito en {curso.titulo}")


# ======================================
# Ejercicio 39: Sistema de Gestión de Proyectos
# ======================================
class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

class Tarea:
    def __init__(self, descripcion, responsable):
        self.descripcion = descripcion
        self.responsable = responsable
        self.completada = False

    def completar(self):
        self.completada = True

proj = Proyecto("App Móvil")
proj.agregar_tarea(Tarea("Diseño UI", "Laura"))
proj.agregar_tarea(Tarea("Backend API", "Carlos"))
for t in proj.tareas:
    print(f"{t.descripcion} - {t.responsable} - {'✔' if t.completada else '✘'}")


# ======================================
# Ejercicio 40: Red Social Avanzada
# ======================================
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
        self.publicaciones = []

    def agregar_amigo(self, usuario):
        self.amigos.append(usuario)

    def publicar(self, texto):
        self.publicaciones.append(texto)

u1 = Usuario("Pedro")
u2 = Usuario("Maria")
u1.agregar_amigo(u2)
u1.publicar("Hola, este es mi primer post en la red social.")
print(f"{u1.nombre} tiene {len(u1.amigos)} amigo(s).")


# ======================================
# Ejercicio 41: Sistema Bancario Completo
# ======================================
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


# ======================================
# Ejercicio 42: Plataforma de Streaming
# ======================================
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


# ======================================
# Ejercicio 43: Sistema de Inventario Inteligente
# ======================================
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


# ======================================
# Ejercicio 44: Simulador de Bolsa de Valores
# ======================================
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


# ======================================
# Ejercicio 45: Sistema de Gestión Hospitalaria
# ======================================
class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Hospital:
    def __init__(self):
        self.pacientes = []

    def ingresar(self, paciente):
        self.pacientes.append(paciente)

hospital = Hospital()
hospital.ingresar(Paciente("Carlos", 40))
print("Pacientes ingresados:", [p.nombre for p in hospital.pacientes])


# ======================================
# Ejercicio 46: Plataforma de Freelancing
# ======================================
class Proyecto:
    def __init__(self, titulo, presupuesto):
        self.titulo = titulo
        self.presupuesto = presupuesto

class Freelancer:
    def __init__(self, nombre):
        self.nombre = nombre
        self.proyectos = []

    def postular(self, proyecto):
        self.proyectos.append(proyecto)

proy = Proyecto("Página web", 500)
free = Freelancer("Ana")
free.postular(proy)
print(f"{free.nombre} se postuló a {free.proyectos[0].titulo}")


# ======================================
# Ejercicio 47: Sistema de Logística
# ======================================
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


# ======================================
# Ejercicio 48: Simulador de Ecosistemas
# ======================================
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


# ======================================
# Ejercicio 49: Sistema de Inteligencia Artificial
# ======================================
class IA:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aprendizaje = []

    def entrenar(self, datos):
        self.aprendizaje.extend(datos)

    def predecir(self, entrada):
        return f"{self.nombre} predice basado en {entrada}"

ia = IA("GPT")
ia.entrenar(["texto1", "texto2"])
print(ia.predecir("nuevo texto"))


# ======================================
# Ejercicio 50: Metaverso Virtual
# ======================================
class Avatar:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mundo = None

    def entrar(self, mundo):
        self.mundo = mundo
        mundo.usuarios.append(self)

class MundoVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []

meta = MundoVirtual("MetaWorld")
user = Avatar("Sebas")
user.entrar(meta)
print(f"{user.nombre} entró a {meta.nombre} con {len(meta.usuarios)} usuario(s).")