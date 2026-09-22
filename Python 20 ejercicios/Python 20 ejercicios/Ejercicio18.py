import math


class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]

        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_menor = float("inf")

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano


calculador = CalculadorDistancia()

p1 = (0, 0)
p2 = (3, 4)

print(calculador.distancia_euclidiana(p1, p2))

referencia = (0, 0)
punto1 = (5, 5)
punto2 = (2, 3)
punto3 = (10, 1)

print(calculador.punto_mas_cercano(referencia, punto1, punto2, punto3))

print(calculador.distancias)