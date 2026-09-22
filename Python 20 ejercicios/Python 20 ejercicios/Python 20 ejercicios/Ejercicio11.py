class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        elemento_mayor = ""
        frecuencia_mayor = 0

        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > frecuencia_mayor:
                frecuencia_mayor = frecuencia
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        else:
            return 0


contador = ContadorFrecuencia()

contador.agregar_elemento("manzana")
contador.agregar_elemento("pera")
contador.agregar_elemento("manzana")
contador.agregar_elemento("banana")
contador.agregar_elemento("manzana")
contador.agregar_elemento("pera")

print(contador.frecuencias)
print(contador.elemento_mas_frecuente())
print(contador.frecuencia_elemento("pera"))

#Tenga un método agregar_videojuego(nombre, genero, precio) que guarde los videojuegos en una lista de diccionarios.
#Tenga un método buscar_por_genero(genero) que retorne una lista con los nombres de los videojuegos que pertenezcan al género indicado.
#Tenga un método precio_promedio() que calcule y retorne el precio promedio de todos los videojuegos.
#Tenga un método videojuegos_baratos(precio_maximo) que retorne una lista con los nombres de los videojuegos cuyo precio sea menor o igual al precio máximo indicado.
#Tenga un método videojuego_mas_caro() que retorne una tupla con el nombre y precio del videojuego más caro.

class GestorVideojuegos:
    def __init__(self):
        self.videojuegos = []

    def agregar_videojuego(self, nombre, genero, precio):
        videojuego = {
            "nombre": nombre,
            "genero": genero,
            "precio": precio
        }

        self.videojuegos.append(videojuego)

    def buscar_por_genero(self, genero):
        resultado = []

        for videojuego in self.videojuegos:
            if videojuego["genero"] == genero:
                resultado.append(videojuego["nombre"])

        return resultado

    def precio_promedio(self):
        if len(self.videojuegos) == 0:
            return 0

        suma = 0

        for videojuego in self.videojuegos:
            suma += videojuego["precio"]

        return suma / len(self.videojuegos)

    def videojuegos_baratos(self, precio_maximo):
        resultado = []

        for videojuego in self.videojuegos:
            if videojuego["precio"] <= precio_maximo:
                resultado.append(videojuego["nombre"])

        return resultado

    def videojuego_mas_caro(self):
        nombre_mayor = ""
        precio_mayor = 0

        for videojuego in self.videojuegos:
            if videojuego["precio"] > precio_mayor:
                precio_mayor = videojuego["precio"]
                nombre_mayor = videojuego["nombre"]

        return nombre_mayor, precio_mayor


gestor = GestorVideojuegos()

gestor.agregar_videojuego("Minecraft", "Sandbox", 30)
gestor.agregar_videojuego("FIFA", "Deportes", 60)
gestor.agregar_videojuego("GTA V", "Accion", 40)
gestor.agregar_videojuego("The Sims", "Simulacion", 25)

print(gestor.videojuegos)
print(gestor.buscar_por_genero("Accion"))
print(gestor.precio_promedio())
print(gestor.videojuegos_baratos(40))
print(gestor.videojuego_mas_caro())
