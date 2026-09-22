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

#Tenga un método agregar_mascota(nombre, especie, edad) que guarde la información de cada mascota en una lista de diccionarios.
#Tenga un método buscar_por_especie(especie) que retorne una lista con los nombres de las mascotas que pertenezcan a la especie indicada.
#Tenga un método mascotas_mayores(edad_minima) que retorne una lista con los nombres de las mascotas cuya edad sea mayor o igual a la indicada.
#Tenga un método edad_promedio() que calcule y retorne la edad promedio de todas las mascotas.
#Tenga un método mascota_mayor() que retorne una tupla con el nombre y la edad de la mascota de mayor edad.

class GestorMascotas:
    def __init__(self):
        self.mascotas = []

    def agregar_mascota(self, nombre, especie, edad):
        mascota = {
            "nombre": nombre,
            "especie": especie,
            "edad": edad
        }

        self.mascotas.append(mascota)

    def buscar_por_especie(self, especie):
        resultado = []

        for mascota in self.mascotas:
            if mascota["especie"] == especie:
                resultado.append(mascota["nombre"])

        return resultado

    def mascotas_mayores(self, edad_minima):
        resultado = []

        for mascota in self.mascotas:
            if mascota["edad"] >= edad_minima:
                resultado.append(mascota["nombre"])

        return resultado

    def edad_promedio(self):
        if len(self.mascotas) == 0:
            return 0

        suma = 0

        for mascota in self.mascotas:
            suma += mascota["edad"]

        return suma / len(self.mascotas)

    def mascota_mayor(self):
        nombre_mayor = ""
        edad_mayor = 0

        for mascota in self.mascotas:
            if mascota["edad"] > edad_mayor:
                edad_mayor = mascota["edad"]
                nombre_mayor = mascota["nombre"]

        return nombre_mayor, edad_mayor


gestor = GestorMascotas()

gestor.agregar_mascota("Max", "Perro", 5)
gestor.agregar_mascota("Luna", "Gato", 3)
gestor.agregar_mascota("Rocky", "Perro", 8)
gestor.agregar_mascota("Michi", "Gato", 6)

print(gestor.mascotas)
print(gestor.buscar_por_especie("Perro"))
print(gestor.mascotas_mayores(5))
print(gestor.edad_promedio())
print(gestor.mascota_mayor())