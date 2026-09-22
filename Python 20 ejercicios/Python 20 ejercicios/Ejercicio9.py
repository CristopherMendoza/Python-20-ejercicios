class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        if letra.lower() in "aeiou":
            return True
        else:
            return False

    def contar_por_tipo(self, texto):
        vocales = 0
        consonantes = 0
        digitos = 0

        for letra in texto:
            if self.solo_vocales(letra):
                vocales += 1
            elif letra.isdigit():
                digitos += 1
            elif letra.isalpha():
                consonantes += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return {
            'vocales': vocales,
            'consonantes': consonantes,
            'digitos': digitos
        }


analizador = AnalizadorString()

print(analizador.contar_por_tipo("Hola123"))
print(analizador.contar_por_tipo("Python2026"))
print(analizador.texto_mas_largo)