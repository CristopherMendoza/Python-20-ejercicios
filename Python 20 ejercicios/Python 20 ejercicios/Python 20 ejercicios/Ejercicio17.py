class AgrupadorEdades:
    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        if len(self.grupos[categoria]) == 0:
            return 0

        suma = sum(self.grupos[categoria])
        promedio = suma / len(self.grupos[categoria])

        return promedio


agrupador = AgrupadorEdades()

print(agrupador.clasificar_edad(10))
print(agrupador.clasificar_edad(16))
print(agrupador.clasificar_edad(30))
print(agrupador.clasificar_edad(70))

print(agrupador.agrupar_por_categoria(8, 10, 15, 17, 25, 30, 65, 70))

print(agrupador.edad_promedio_categoria("adulto"))
print(agrupador.edad_promedio_categoria("niño"))

#agregar_nota(nombre, nota) → agrega una nota al estudiante. Si el estudiante no existe, debe crearlo.
#promedio_estudiante(nombre) → devuelve el promedio de sus notas.
#estudiantes_aprobados(minimo) → devuelve los estudiantes cuyo promedio sea igual o mayor al mínimo.
#mejor_estudiante() → devuelve el estudiante con el promedio más alto.

class GestorNotas:
    def __init__(self):
        self.notas = {}

    def agregar_nota(self, nombre, nota):
        if nombre in self.notas:
            self.notas[nombre].append(nota)
        else:
            self.notas[nombre] = [nota]

    def promedio_estudiante(self, nombre):
        if nombre not in self.notas:
            return 0

        suma = 0

        for nota in self.notas[nombre]:
            suma += nota

        promedio = suma / len(self.notas[nombre])

        return promedio

    def estudiantes_aprobados(self, minimo):
        resultado = []

        for nombre in self.notas:
            promedio = self.promedio_estudiante(nombre)

            if promedio >= minimo:
                resultado.append(nombre)

        return resultado

    def mejor_estudiante(self):
        nombre_mayor = ""
        promedio_mayor = 0

        for nombre in self.notas:
            promedio = self.promedio_estudiante(nombre)

            if promedio > promedio_mayor:
                promedio_mayor = promedio
                nombre_mayor = nombre

        return nombre_mayor, promedio_mayor


gestor = GestorNotas()

gestor.agregar_nota("Ana", 80)
gestor.agregar_nota("Ana", 90)
gestor.agregar_nota("Ana", 85)

gestor.agregar_nota("Carlos", 70)
gestor.agregar_nota("Carlos", 75)
gestor.agregar_nota("Carlos", 80)

gestor.agregar_nota("Maria", 95)
gestor.agregar_nota("Maria", 90)
gestor.agregar_nota("Maria", 100)

print(gestor.notas)
print(gestor.promedio_estudiante("Ana"))
print(gestor.estudiantes_aprobados(80))
print(gestor.mejor_estudiante())