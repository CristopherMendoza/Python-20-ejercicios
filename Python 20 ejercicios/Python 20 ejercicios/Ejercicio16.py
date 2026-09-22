class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        numero = ord(letra.upper()) - ord("A")
        nuevo_numero = (numero + desplazamiento) % 26
        nueva_letra = chr(nuevo_numero + ord("A"))

        return nueva_letra

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


codificador = CodificadorCesar()

print(codificador.codificar_letra("A", 3))
print(codificador.codificar_letra("Z", 3))

print(codificador.codificar_palabra("HOLA", 3))
print(codificador.codificar_palabra("PYTHON", 2))

print(codificador.historial)