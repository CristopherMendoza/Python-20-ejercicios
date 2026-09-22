class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        mayor = max(len(lista1), len(lista2))

        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []

        for lista in listas:
            if len(resultado) == 0:
                resultado = lista.copy()
            else:
                resultado = self.intercalar(resultado, lista)

        return resultado


combinador = CombinadorListas()

lista1 = [1, 3, 5]
lista2 = [2, 4, 6]

print(combinador.intercalar(lista1, lista2))

lista3 = [7, 8, 9]

print(combinador.intercalar_multiples(lista1, lista2, lista3))

#Tenga un método agregar_estudiante(nombre, edad, carrera) que guarde la información de cada estudiante en una lista de diccionarios.
#Tenga un método buscar_por_carrera(carrera) que retorne una lista con los nombres de los estudiantes que pertenecen a la carrera indicada.
#Tenga un método estudiantes_mayores(edad_minima) que retorne una lista con los nombres de los estudiantes cuya edad sea mayor o igual a la edad indicada.
#Tenga un método edad_promedio() que calcule y retorne la edad promedio de todos los estudiantes.
#Tenga un método estudiante_mayor() que retorne una tupla con el nombre y edad del estudiante de mayor edad.

class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, edad, carrera):
        estudiante = {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera
        }

        self.estudiantes.append(estudiante)

    def buscar_por_carrera(self, carrera):
        resultado = []

        for estudiante in self.estudiantes:
            if estudiante["carrera"] == carrera:
                resultado.append(estudiante["nombre"])

        return resultado

    def estudiantes_mayores(self, edad_minima):
        resultado = []

        for estudiante in self.estudiantes:
            if estudiante["edad"] >= edad_minima:
                resultado.append(estudiante["nombre"])

        return resultado

    def edad_promedio(self):
        if len(self.estudiantes) == 0:
            return 0

        suma = 0

        for estudiante in self.estudiantes:
            suma += estudiante["edad"]

        return suma / len(self.estudiantes)

    def estudiante_mayor(self):
        nombre_mayor = ""
        edad_mayor = 0

        for estudiante in self.estudiantes:
            if estudiante["edad"] > edad_mayor:
                edad_mayor = estudiante["edad"]
                nombre_mayor = estudiante["nombre"]

        return nombre_mayor, edad_mayor


gestor = GestorEstudiantes()

gestor.agregar_estudiante("Ana", 19, "Ingenieria de Software")
gestor.agregar_estudiante("Carlos", 22, "Ingenieria Civil")
gestor.agregar_estudiante("Maria", 20, "Ingenieria de Software")
gestor.agregar_estudiante("Pedro", 25, "Ingenieria Civil")

print(gestor.estudiantes)
print(gestor.buscar_por_carrera("Ingenieria de Software"))
print(gestor.estudiantes_mayores(20))
print(gestor.edad_promedio())
print(gestor.estudiante_mayor())
