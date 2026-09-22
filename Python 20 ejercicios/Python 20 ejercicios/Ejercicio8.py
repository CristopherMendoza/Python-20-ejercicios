class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = 0
        equipo_mayor = ""

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor:
                mayor = len(jugadores)
                equipo_mayor = equipo

        return equipo_mayor


gestor = Equipos()

gestor.crear_equipo("Barcelona")
gestor.crear_equipo("Emelec")
gestor.crear_equipo("Liga")

gestor.agregar_jugador("Barcelona", "Juan")
gestor.agregar_jugador("Barcelona", "Pedro")
gestor.agregar_jugador("Barcelona", "Carlos")

gestor.agregar_jugador("Emelec", "Luis")
gestor.agregar_jugador("Emelec", "Miguel")

gestor.agregar_jugador("Liga", "Andres")

print(gestor.equipos)
print(gestor.equipo_mayor_integrantes())