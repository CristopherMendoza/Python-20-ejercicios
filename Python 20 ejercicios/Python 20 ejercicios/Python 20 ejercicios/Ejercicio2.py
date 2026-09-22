class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.palabras = []

    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)
        self.palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


analizador = AnalizadorTexto()

analizador.agregar_palabra("Python")
analizador.agregar_palabra("Java")
analizador.agregar_palabra("Python")

analizador.agregar_multiples("HTML", "CSS", "JavaScript", "Python")

print(analizador.palabras_unicas)
print(analizador.palabras)
print(analizador.contar_palabras())

#Tenga un método agregar_producto(nombre, precio, cantidad) que guarde cada producto en un diccionario.
#Tenga un método valor_inventario() que calcule y retorne el valor total de todos los productos. El valor de cada producto se obtiene multiplicando precio × cantidad.
#Tenga un método productos_bajo_stock(minimo) que retorne una lista con los nombres de los productos cuya cantidad sea menor al mínimo indicado.
#Tenga un método producto_mas_caro() que retorne una tupla con el nombre y precio del producto más caro.

class GestorProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio, cantidad):
        self.productos[nombre] = {
            "precio": precio,
            "cantidad": cantidad
        }

    def valor_inventario(self):
        total = 0

        for producto in self.productos.values():
            total += producto["precio"] * producto["cantidad"]

        return total

    def productos_bajo_stock(self, minimo):
        resultado = []

        for nombre, producto in self.productos.items():
            if producto["cantidad"] < minimo:
                resultado.append(nombre)

        return resultado

    def producto_mas_caro(self):
        nombre_mayor = ""
        precio_mayor = 0

        for nombre, producto in self.productos.items():
            if producto["precio"] > precio_mayor:
                precio_mayor = producto["precio"]
                nombre_mayor = nombre

        return nombre_mayor, precio_mayor


gestor = GestorProductos()

gestor.agregar_producto("Laptop", 800, 5)
gestor.agregar_producto("Mouse", 25, 3)
gestor.agregar_producto("Teclado", 50, 8)
gestor.agregar_producto("Monitor", 300, 2)

print(gestor.productos)
print(gestor.valor_inventario())
print(gestor.productos_bajo_stock(5))
print(gestor.producto_mas_caro())