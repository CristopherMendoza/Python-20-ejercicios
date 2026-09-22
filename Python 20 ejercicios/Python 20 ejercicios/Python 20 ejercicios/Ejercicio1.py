class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0

        suma = sum(self.notas)
        promedio = suma / len(self.notas)

        return promedio


calificador = Calificador()

print(calificador.cargar_notas(80, 90, 105, 70, -5, 100))
print(calificador.promedio())


#Tenga un método registrar_estudiante(nombre, nota) que guarde el nombre y la nota de cada estudiante en un diccionario.
#Tenga un método estudiantes_aprobados(nota_minima) que recorra el diccionario y retorne una lista con los estudiantes cuya nota sea mayor o igual a la nota mínima.
#Tenga un método nota_promedio() que calcule y retorne el promedio de todas las notas registradas.
#Tenga un método mejor_estudiante() que encuentre y retorne una tupla con el nombre y la nota del estudiante que tenga la calificación más alta.

class GestorCalificaciones:
    def __init__(self):
        self.notas = {}

    def registrar_estudiante(self, nombre, nota):
        self.notas[nombre] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for nombre, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(nombre)

        return aprobados

    def nota_promedio(self):
        if len(self.notas) == 0:
            return 0

        suma = sum(self.notas.values())
        promedio = suma / len(self.notas)

        return promedio

    def mejor_estudiante(self):
        nombre_mayor = ""
        nota_mayor = 0

        for nombre, nota in self.notas.items():
            if nota > nota_mayor:
                nota_mayor = nota
                nombre_mayor = nombre

        return nombre_mayor, nota_mayor


gestor = GestorCalificaciones()

gestor.registrar_estudiante("Ana", 85)
gestor.registrar_estudiante("Carlos", 60)
gestor.registrar_estudiante("Maria", 95)
gestor.registrar_estudiante("Pedro", 72)

print(gestor.notas)
print(gestor.estudiantes_aprobados(70))
print(gestor.nota_promedio())
print(gestor.mejor_estudiante())