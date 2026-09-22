class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        self.pares = []
        self.impares = []

        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        return {
            'pares': self.pares,
            'impares': self.impares
        }

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


analizador = AnalizadorNumeros()

print(analizador.separar(1, 2, 3, 4, 5, 6, 7, 8))
print(analizador.cantidad_pares_impares())