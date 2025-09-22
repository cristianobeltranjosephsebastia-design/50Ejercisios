class ContadorPalabras:
    def __init__(self, texto):
        self.texto = texto

    def contar(self):
        palabras = self.texto.split()
        return len(palabras)

    def frecuencia(self):
        freq = {}
        for palabra in self.texto.split():
            palabra = palabra.lower()
            freq[palabra] = freq.get(palabra, 0) + 1
        return freq

texto = "Hola mundo hola Python mundo"
contador = ContadorPalabras(texto)
print("Cantidad de palabras:", contador.contar())
print("Frecuencia:", contador.frecuencia())
