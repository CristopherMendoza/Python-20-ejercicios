class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        numero = ord(letra.upper()) - ord("A")
        nuevo_numero = (numero + desplazamiento) % 26
        nueva_letra = chr(nuevo_numero + ord("A"))

        return nueva_letra

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


codificador = CodificadorCesar()

print(codificador.codificar_letra("A", 3))
print(codificador.codificar_letra("Z", 3))

print(codificador.codificar_palabra("HOLA", 3))
print(codificador.codificar_palabra("PYTHON", 2))

print(codificador.historial)

#agregar_libro(titulo, autor) → agrega un libro y lo registra como disponible.
#prestar_libro(titulo) → cambia el libro a no disponible.
#devolver_libro(titulo) → cambia el libro a disponible.
#libros_disponibles() → devuelve una lista con los títulos disponibles.
#libros_autor(autor) → devuelve los títulos escritos por ese autor.

class GestorBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor):
        libro = {
            "titulo": titulo,
            "autor": autor,
            "disponible": True
        }

        self.libros.append(libro)

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro["titulo"] == titulo:
                libro["disponible"] = False

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro["titulo"] == titulo:
                libro["disponible"] = True

    def libros_disponibles(self):
        resultado = []

        for libro in self.libros:
            if libro["disponible"] == True:
                resultado.append(libro["titulo"])

        return resultado

    def libros_autor(self, autor):
        resultado = []

        for libro in self.libros:
            if libro["autor"] == autor:
                resultado.append(libro["titulo"])

        return resultado


biblioteca = GestorBiblioteca()

biblioteca.agregar_libro("Python desde Cero", "Juan Perez")
biblioteca.agregar_libro("JavaScript Basico", "Maria Lopez")
biblioteca.agregar_libro("Python Avanzado", "Juan Perez")
biblioteca.agregar_libro("Bases de Datos", "Carlos Ruiz")

biblioteca.prestar_libro("Python desde Cero")

print(biblioteca.libros)
print(biblioteca.libros_disponibles())
print(biblioteca.libros_autor("Juan Perez"))

biblioteca.devolver_libro("Python desde Cero")

print(biblioteca.libros_disponibles())