class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)


gestor = GestorTemperatura()

gestor.registrar_temperatura(25)
gestor.registrar_temperatura(30)

gestor.registrar_multiples(28, 32, 24, 27)

print(gestor.temperaturas)
print(gestor.minima())
print(gestor.maxima())
print(gestor.promedio())