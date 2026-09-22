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

#Tenga un método agregar_curso(nombre, profesor, estudiantes) que guarde la información de cada curso en un diccionario.
#Tenga un método cursos_con_muchos_estudiantes(minimo) que retorne una lista con los nombres de los cursos que tengan una cantidad de estudiantes mayor o igual al mínimo indicado.
#Tenga un método promedio_estudiantes() que calcule y retorne el promedio de estudiantes entre todos los cursos.
#Tenga un método curso_mayor() que retorne una tupla con el nombre del curso y la cantidad de estudiantes del curso con mayor cantidad de estudiantes.

class GestorCursos:
    def __init__(self):
        self.cursos = {}

    def agregar_curso(self, nombre, profesor, estudiantes):
        self.cursos[nombre] = {
            "profesor": profesor,
            "estudiantes": estudiantes
        }

    def cursos_con_muchos_estudiantes(self, minimo):
        resultado = []

        for nombre, curso in self.cursos.items():
            if curso["estudiantes"] >= minimo:
                resultado.append(nombre)

        return resultado

    def promedio_estudiantes(self):
        if len(self.cursos) == 0:
            return 0

        suma = 0

        for curso in self.cursos.values():
            suma += curso["estudiantes"]

        return suma / len(self.cursos)

    def curso_mayor(self):
        curso_mayor = ""
        estudiantes_mayor = 0

        for nombre, curso in self.cursos.items():
            if curso["estudiantes"] > estudiantes_mayor:
                estudiantes_mayor = curso["estudiantes"]
                curso_mayor = nombre

        return curso_mayor, estudiantes_mayor


gestor = GestorCursos()

gestor.agregar_curso("Python", "Carlos", 30)
gestor.agregar_curso("JavaScript", "Maria", 25)
gestor.agregar_curso("Bases de Datos", "Pedro", 40)
gestor.agregar_curso("HTML y CSS", "Ana", 20)

print(gestor.cursos)
print(gestor.cursos_con_muchos_estudiantes(25))
print(gestor.promedio_estudiantes())
print(gestor.curso_mayor())

