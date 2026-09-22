class AnalizadorPatrones:
    def __init__(self):
        self.palabras = []

    def encontrar_palabras(self, texto, patron):
        resultado = []

        palabras = texto.split()

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        resultado = {}

        palabras = texto.split()

        for palabra in palabras:
            longitud = len(palabra)

            if longitud in resultado:
                resultado[longitud].append(palabra)
            else:
                resultado[longitud] = [palabra]

        return resultado

    def palabras_unicas(self):
        return set(self.palabras)


analizador = AnalizadorPatrones()

texto = "Python programa para aprender Python y practicar"

analizador.palabras = texto.split()

print(analizador.encontrar_palabras(texto, "pro"))
print(analizador.agrupar_por_longitud(texto))
print(analizador.palabras_unicas())