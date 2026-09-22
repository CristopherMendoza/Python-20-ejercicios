class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        total = sum(self.articulos.values())
        return total

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)

        return resultado


carrito = CarroCompras()

carrito.agregar_articulo("Laptop", 800)
carrito.agregar_articulo("Mouse", 25)
carrito.agregar_articulo("Teclado", 50)
carrito.agregar_articulo("Monitor", 300)

print(carrito.articulos)
print(carrito.total_carrito())
print(carrito.articulos_por_rango(20, 100))