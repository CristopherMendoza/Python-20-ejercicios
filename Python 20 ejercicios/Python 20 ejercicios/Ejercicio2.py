class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.palabras = []

    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)
        self.palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


analizador = AnalizadorTexto()

analizador.agregar_palabra("Python")
analizador.agregar_palabra("Java")
analizador.agregar_palabra("Python")

analizador.agregar_multiples("HTML", "CSS", "JavaScript", "Python")

print(analizador.palabras_unicas)
print(analizador.palabras)
print(analizador.contar_palabras())