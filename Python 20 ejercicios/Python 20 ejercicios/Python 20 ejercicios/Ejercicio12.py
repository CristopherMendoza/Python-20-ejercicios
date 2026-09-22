class SelectorRango:
    def crear_rango(self, inicio, fin):
        resultado = []

        for numero in range(inicio, fin + 1):
            resultado.append(numero)

        return tuple(resultado)

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()

        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]

            for numero in range(inicio, fin + 1):
                elementos.add(numero)

        return list(elementos)


selector = SelectorRango()

print(selector.crear_rango(1, 5))

rango1 = (1, 5)
rango2 = (4, 8)
rango3 = (7, 10)

print(selector.elementos_en_multiples_rangos(rango1, rango2, rango3))

#Tenga un método agregar_habitacion(numero, tipo, precio) que guarde las habitaciones en un diccionario, usando el número de habitación como clave.
#Tenga un método habitaciones_por_tipo(tipo) que retorne una lista con los números de las habitaciones que pertenecen al tipo indicado.
#Tenga un método precio_promedio() que calcule y retorne el precio promedio de todas las habitaciones.
#Tenga un método habitaciones_baratas(precio_maximo) que retorne una lista con los números de las habitaciones cuyo precio sea menor o igual al indicado.
#Tenga un método habitacion_mas_cara() que retorne una tupla con el número de habitación y precio de la habitación más cara.

class GestorHoteles:
    def __init__(self):
        self.habitaciones = {}

    def agregar_habitacion(self, numero, tipo, precio):
        self.habitaciones[numero] = {
            "tipo": tipo,
            "precio": precio
        }

    def habitaciones_por_tipo(self, tipo):
        resultado = []

        for numero, habitacion in self.habitaciones.items():
            if habitacion["tipo"] == tipo:
                resultado.append(numero)

        return resultado

    def precio_promedio(self):
        if len(self.habitaciones) == 0:
            return 0

        suma = 0

        for habitacion in self.habitaciones.values():
            suma += habitacion["precio"]

        return suma / len(self.habitaciones)

    def habitaciones_baratas(self, precio_maximo):
        resultado = []

        for numero, habitacion in self.habitaciones.items():
            if habitacion["precio"] <= precio_maximo:
                resultado.append(numero)

        return resultado

    def habitacion_mas_cara(self):
        numero_mayor = 0
        precio_mayor = 0

        for numero, habitacion in self.habitaciones.items():
            if habitacion["precio"] > precio_mayor:
                precio_mayor = habitacion["precio"]
                numero_mayor = numero

        return numero_mayor, precio_mayor


gestor = GestorHoteles()

gestor.agregar_habitacion(101, "Individual", 40)
gestor.agregar_habitacion(102, "Doble", 60)
gestor.agregar_habitacion(201, "Suite", 120)
gestor.agregar_habitacion(202, "Doble", 70)

print(gestor.habitaciones)
print(gestor.habitaciones_por_tipo("Doble"))
print(gestor.precio_promedio())
print(gestor.habitaciones_baratas(70))
print(gestor.habitacion_mas_cara())