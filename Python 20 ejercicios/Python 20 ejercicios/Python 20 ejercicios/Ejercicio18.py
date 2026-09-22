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

#registrar_asistencia(nombre) → agrega un estudiante a la asistencia.
#esta_presente(nombre) → devuelve True si el estudiante asistió y False si no.
#cantidad_asistentes() → devuelve cuántos estudiantes asistieron.
#lista_asistentes() → devuelve la lista de asistentes.
#eliminar_asistencia(nombre) → elimina al estudiante de la lista si está

class RegistroAsistencia:
    def __init__(self):
        self.asistentes = []

    def registrar_asistencia(self, nombre):
        if nombre not in self.asistentes:
            self.asistentes.append(nombre)

    def esta_presente(self, nombre):
        if nombre in self.asistentes:
            return True
        else:
            return False

    def cantidad_asistentes(self):
        return len(self.asistentes)

    def lista_asistentes(self):
        return self.asistentes

    def eliminar_asistencia(self, nombre):
        if nombre in self.asistentes:
            self.asistentes.remove(nombre)


registro = RegistroAsistencia()

registro.registrar_asistencia("Ana")
registro.registrar_asistencia("Carlos")
registro.registrar_asistencia("Maria")
registro.registrar_asistencia("Pedro")

print(registro.lista_asistentes())
print(registro.esta_presente("Maria"))
print(registro.esta_presente("Luis"))
print(registro.cantidad_asistentes())

registro.eliminar_asistencia("Carlos")

print(registro.lista_asistentes())