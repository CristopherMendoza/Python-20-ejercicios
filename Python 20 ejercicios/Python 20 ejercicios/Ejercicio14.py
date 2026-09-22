class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        estudiante_mayor = ""
        nota_mayor = 0

        for estudiante, nota in self.notas.items():
            if nota > nota_mayor:
                nota_mayor = nota
                estudiante_mayor = estudiante

        return estudiante_mayor, nota_mayor


registro = RegistroNotas()

registro.registrar("Ana", 85)
registro.registrar("Carlos", 60)
registro.registrar("Maria", 95)
registro.registrar("Pedro", 72)

print(registro.notas)
print(registro.estudiantes_aprobados(70))
print(registro.mejor_estudiante())