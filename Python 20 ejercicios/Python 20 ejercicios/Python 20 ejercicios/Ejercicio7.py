class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0

        suma = sum(self.personas.values())
        promedio = suma / len(self.personas)

        return promedio


gestor = GestorPersonas()

gestor.agregar_persona("Ana", 20)
gestor.agregar_persona("Carlos", 17)
gestor.agregar_persona("Maria", 25)
gestor.agregar_persona("Pedro", 30)

print(gestor.personas)
print(gestor.personas_mayores(18))
print(gestor.edad_promedio())

#Tenga un método agregar_pelicula(titulo, genero, calificacion) que guarde las películas en una lista de diccionarios.
#Tenga un método buscar_por_genero(genero) que retorne una lista con los títulos de las películas que pertenecen al género indicado.
#Tenga un método peliculas_buenas(calificacion_minima) que retorne una lista con los títulos de las películas cuya calificación sea mayor o igual a la indicada.
#Tenga un método pelicula_mejor_calificada() que retorne una tupla con el título y la calificación de la película con mayor puntuación.

class GestorPeliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, titulo, genero, calificacion):
        pelicula = {
            "titulo": titulo,
            "genero": genero,
            "calificacion": calificacion
        }

        self.peliculas.append(pelicula)

    def buscar_por_genero(self, genero):
        resultado = []

        for pelicula in self.peliculas:
            if pelicula["genero"] == genero:
                resultado.append(pelicula["titulo"])

        return resultado

    def peliculas_buenas(self, calificacion_minima):
        resultado = []

        for pelicula in self.peliculas:
            if pelicula["calificacion"] >= calificacion_minima:
                resultado.append(pelicula["titulo"])

        return resultado

    def pelicula_mejor_calificada(self):
        titulo_mayor = ""
        calificacion_mayor = 0

        for pelicula in self.peliculas:
            if pelicula["calificacion"] > calificacion_mayor:
                calificacion_mayor = pelicula["calificacion"]
                titulo_mayor = pelicula["titulo"]

        return titulo_mayor, calificacion_mayor


gestor = GestorPeliculas()

gestor.agregar_pelicula("Interestelar", "Ciencia Ficcion", 9.0)
gestor.agregar_pelicula("Titanic", "Romance", 8.5)
gestor.agregar_pelicula("Avatar", "Ciencia Ficcion", 8.0)
gestor.agregar_pelicula("El Padrino", "Drama", 9.2)

print(gestor.peliculas)
print(gestor.buscar_por_genero("Ciencia Ficcion"))
print(gestor.peliculas_buenas(8.5))
print(gestor.pelicula_mejor_calificada())