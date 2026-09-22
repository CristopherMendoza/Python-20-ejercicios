class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        tarea = (descripcion, prioridad)
        self.tareas.append(tarea)

    def tareas_prioritarias(self):
        resultado = []

        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)

        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break


gestor = Tareas()

gestor.agregar_tarea("Estudiar Python", "alta")
gestor.agregar_tarea("Hacer ejercicio", "baja")
gestor.agregar_tarea("Terminar tarea", "alta")
gestor.agregar_tarea("Ordenar cuarto", "media")

print(gestor.tareas)
print(gestor.tareas_prioritarias())

gestor.eliminar_completada("Hacer ejercicio")

print(gestor.tareas)

#Tenga un método agregar_pelicula(titulo, genero, duracion) que guarde las películas en una lista de diccionarios.
#Tenga un método peliculas_por_genero(genero) que retorne una lista con los títulos de las películas que pertenezcan al género indicado.
#Tenga un método duracion_promedio() que calcule y retorne la duración promedio de todas las películas.
#Tenga un método peliculas_largas(minutos) que retorne una lista con los títulos de las películas cuya duración sea mayor o igual al número de minutos indicado.
#Tenga un método pelicula_mas_larga() que retorne una tupla con el título y duración de la película más larga.

class ControlPeliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, titulo, genero, duracion):
        pelicula = {
            "titulo": titulo,
            "genero": genero,
            "duracion": duracion
        }

        self.peliculas.append(pelicula)

    def peliculas_por_genero(self, genero):
        resultado = []

        for pelicula in self.peliculas:
            if pelicula["genero"] == genero:
                resultado.append(pelicula["titulo"])

        return resultado

    def duracion_promedio(self):
        if len(self.peliculas) == 0:
            return 0

        suma = 0

        for pelicula in self.peliculas:
            suma += pelicula["duracion"]

        return suma / len(self.peliculas)

    def peliculas_largas(self, minutos):
        resultado = []

        for pelicula in self.peliculas:
            if pelicula["duracion"] >= minutos:
                resultado.append(pelicula["titulo"])

        return resultado

    def pelicula_mas_larga(self):
        titulo_mayor = ""
        duracion_mayor = 0

        for pelicula in self.peliculas:
            if pelicula["duracion"] > duracion_mayor:
                duracion_mayor = pelicula["duracion"]
                titulo_mayor = pelicula["titulo"]

        return titulo_mayor, duracion_mayor


control = ControlPeliculas()

control.agregar_pelicula("Interestelar", "Ciencia Ficcion", 169)
control.agregar_pelicula("Titanic", "Romance", 195)
control.agregar_pelicula("Avatar", "Ciencia Ficcion", 162)
control.agregar_pelicula("Toy Story", "Animacion", 81)

print(control.peliculas)
print(control.peliculas_por_genero("Ciencia Ficcion"))
print(control.duracion_promedio())
print(control.peliculas_largas(160))
print(control.pelicula_mas_larga())