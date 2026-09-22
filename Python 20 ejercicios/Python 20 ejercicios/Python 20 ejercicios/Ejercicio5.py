class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        self.pares = []
        self.impares = []

        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        return {
            'pares': self.pares,
            'impares': self.impares
        }

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


analizador = AnalizadorNumeros()

print(analizador.separar(1, 2, 3, 4, 5, 6, 7, 8))
print(analizador.cantidad_pares_impares())

#Tenga un método agregar_libro(titulo, autor, paginas) que guarde los libros en una lista de diccionarios.
#Tenga un método buscar_por_autor(autor) que retorne una lista con los títulos de los libros escritos por ese autor.
#Tenga un método libros_largos(minimo_paginas) que retorne una lista con los títulos de los libros que tengan una cantidad de páginas mayor o igual al mínimo indicado.
#Tenga un método libro_mas_largo() que retorne una tupla con el título y la cantidad de páginas del libro que tenga más páginas.

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, paginas):
        libro = {
            "titulo": titulo,
            "autor": autor,
            "paginas": paginas
        }

        self.libros.append(libro)

    def buscar_por_autor(self, autor):
        resultado = []

        for libro in self.libros:
            if libro["autor"] == autor:
                resultado.append(libro["titulo"])

        return resultado

    def libros_largos(self, minimo_paginas):
        resultado = []

        for libro in self.libros:
            if libro["paginas"] >= minimo_paginas:
                resultado.append(libro["titulo"])

        return resultado

    def libro_mas_largo(self):
        titulo_mayor = ""
        paginas_mayor = 0

        for libro in self.libros:
            if libro["paginas"] > paginas_mayor:
                paginas_mayor = libro["paginas"]
                titulo_mayor = libro["titulo"]

        return titulo_mayor, paginas_mayor


biblioteca = Biblioteca()

biblioteca.agregar_libro("Python desde Cero", "Juan Perez", 250)
biblioteca.agregar_libro("Aprendiendo Java", "Maria Lopez", 400)
biblioteca.agregar_libro("Python Avanzado", "Juan Perez", 550)
biblioteca.agregar_libro("Bases de Datos", "Carlos Ruiz", 300)

print(biblioteca.libros)
print(biblioteca.buscar_por_autor("Juan Perez"))
print(biblioteca.libros_largos(300))
print(biblioteca.libro_mas_largo())