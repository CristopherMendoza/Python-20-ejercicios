class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)

        return resultado


inversor = InversorSecuencia()

lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30]

print(inversor.invertir_lista(lista1))
print(inversor.invertir_multiples(lista1, lista2))

#Tenga un método registrar_ciudad(ciudad, temperatura) que guarde la temperatura de cada ciudad en un diccionario.
#Tenga un método temperaturas_altas(limite) que retorne una lista con los nombres de las ciudades cuya temperatura sea mayor o igual al límite indicado.
#Tenga un método temperatura_promedio() que calcule y retorne el promedio de todas las temperaturas registradas.
#Tenga un método ciudad_mas_caliente() que retorne una tupla con el nombre de la ciudad y su temperatura más alta.

class ControlTemperaturas:
    def __init__(self):
        self.temperaturas = {}

    def registrar_ciudad(self, ciudad, temperatura):
        self.temperaturas[ciudad] = temperatura

    def temperaturas_altas(self, limite):
        resultado = []

        for ciudad, temperatura in self.temperaturas.items():
            if temperatura >= limite:
                resultado.append(ciudad)

        return resultado

    def temperatura_promedio(self):
        if len(self.temperaturas) == 0:
            return 0

        suma = sum(self.temperaturas.values())
        promedio = suma / len(self.temperaturas)

        return promedio

    def ciudad_mas_caliente(self):
        ciudad_mayor = ""
        temperatura_mayor = float("-inf")

        for ciudad, temperatura in self.temperaturas.items():
            if temperatura > temperatura_mayor:
                temperatura_mayor = temperatura
                ciudad_mayor = ciudad

        return ciudad_mayor, temperatura_mayor


control = ControlTemperaturas()

control.registrar_ciudad("Guayaquil", 31)
control.registrar_ciudad("Quito", 18)
control.registrar_ciudad("Cuenca", 20)
control.registrar_ciudad("Manta", 29)

print(control.temperaturas)
print(control.temperaturas_altas(25))
print(control.temperatura_promedio())
print(control.ciudad_mas_caliente())