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

#agregar_habitacion(numero) → agrega una habitación inicialmente disponible.
#reservar_habitacion(numero, cliente) → asigna una reserva a una habitación.
#cancelar_reserva(numero) → deja nuevamente disponible la habitación.
#habitaciones_disponibles() → devuelve los números de las habitaciones disponibles.
#reservas_activas() → devuelve los nombres de los clientes que tienen una reserva.

class GestorReservas:
    def __init__(self):
        self.habitaciones = {}

    def agregar_habitacion(self, numero):
        self.habitaciones[numero] = {
            "cliente": "",
            "reservada": False
        }

    def reservar_habitacion(self, numero, cliente):
        if numero in self.habitaciones:
            if self.habitaciones[numero]["reservada"] == False:
                self.habitaciones[numero]["cliente"] = cliente
                self.habitaciones[numero]["reservada"] = True

    def cancelar_reserva(self, numero):
        if numero in self.habitaciones:
            self.habitaciones[numero]["cliente"] = ""
            self.habitaciones[numero]["reservada"] = False

    def habitaciones_disponibles(self):
        resultado = []

        for numero, habitacion in self.habitaciones.items():
            if habitacion["reservada"] == False:
                resultado.append(numero)

        return resultado

    def reservas_activas(self):
        resultado = []

        for habitacion in self.habitaciones.values():
            if habitacion["reservada"] == True:
                resultado.append(habitacion["cliente"])

        return resultado


gestor = GestorReservas()

gestor.agregar_habitacion(101)
gestor.agregar_habitacion(102)
gestor.agregar_habitacion(103)
gestor.agregar_habitacion(104)

gestor.reservar_habitacion(101, "Ana")
gestor.reservar_habitacion(103, "Carlos")

print(gestor.habitaciones)
print(gestor.habitaciones_disponibles())
print(gestor.reservas_activas())

gestor.cancelar_reserva(101)

print(gestor.habitaciones_disponibles())
print(gestor.reservas_activas())