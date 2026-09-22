class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma = sum(divisores[:-1])

        if suma == numero:
            return True
        else:
            return False

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


finder = DivisorFinder()

print(finder.encontrar_divisores(12))
print(finder.es_perfecto(6))
print(finder.es_perfecto(12))
print(finder.encontrar_multiples_divisores(6, 10, 12, 28))

#Tenga un método agregar_curso(nombre, categoria, precio, estudiantes) que guarde la información de cada curso en una lista de diccionarios.
#Tenga un método buscar_por_categoria(categoria) que retorne una lista con los nombres de los cursos que pertenezcan a la categoría indicada.
#Tenga un método cursos_economicos(precio_maximo) que retorne una lista con los nombres de los cursos cuyo precio sea menor o igual al precio indicado.
#Tenga un método promedio_precios() que calcule y retorne el precio promedio de todos los cursos.
#Tenga un método curso_mas_estudiantes() que retorne una tupla con el nombre del curso y la cantidad de estudiantes del curso con mayor cantidad de estudiantes.

class GestorCursosOnline:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, nombre, categoria, precio, estudiantes):
        curso = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "estudiantes": estudiantes
        }

        self.cursos.append(curso)

    def buscar_por_categoria(self, categoria):
        resultado = []

        for curso in self.cursos:
            if curso["categoria"] == categoria:
                resultado.append(curso["nombre"])

        return resultado

    def cursos_economicos(self, precio_maximo):
        resultado = []

        for curso in self.cursos:
            if curso["precio"] <= precio_maximo:
                resultado.append(curso["nombre"])

        return resultado

    def promedio_precios(self):
        if len(self.cursos) == 0:
            return 0

        suma = 0

        for curso in self.cursos:
            suma += curso["precio"]

        return suma / len(self.cursos)

    def curso_mas_estudiantes(self):
        nombre_mayor = ""
        estudiantes_mayor = 0

        for curso in self.cursos:
            if curso["estudiantes"] > estudiantes_mayor:
                estudiantes_mayor = curso["estudiantes"]
                nombre_mayor = curso["nombre"]

        return nombre_mayor, estudiantes_mayor


gestor = GestorCursosOnline()

gestor.agregar_curso("Python desde Cero", "Programacion", 30, 500)
gestor.agregar_curso("JavaScript", "Programacion", 45, 350)
gestor.agregar_curso("Diseño Grafico", "Diseño", 25, 200)
gestor.agregar_curso("Bases de Datos", "Programacion", 50, 600)

print(gestor.cursos)
print(gestor.buscar_por_categoria("Programacion"))
print(gestor.cursos_economicos(30))
print(gestor.promedio_precios())
print(gestor.curso_mas_estudiantes())