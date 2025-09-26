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