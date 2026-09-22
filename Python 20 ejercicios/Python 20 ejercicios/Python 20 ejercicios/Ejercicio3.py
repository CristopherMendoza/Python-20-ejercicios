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

#Tenga un método registrar_venta(producto, cantidad, precio) que guarde las ventas en una lista de diccionarios.
#Tenga un método total_ventas() que calcule y retorne el dinero total de todas las ventas. Para cada venta se debe multiplicar cantidad × precio.
#Tenga un método ventas_mayores(monto) que retorne una lista con los nombres de los productos cuyas ventas individuales superen o sean iguales al monto indicado.
#Tenga un método venta_mayor() que retorne una tupla con el nombre del producto y el valor de la venta más grande.

class RegistroVentas:
    def __init__(self):
        self.ventas = []

    def registrar_venta(self, producto, cantidad, precio):
        venta = {
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio
        }

        self.ventas.append(venta)

    def total_ventas(self):
        total = 0

        for venta in self.ventas:
            total += venta["cantidad"] * venta["precio"]

        return total

    def ventas_mayores(self, monto):
        resultado = []

        for venta in self.ventas:
            total = venta["cantidad"] * venta["precio"]

            if total >= monto:
                resultado.append(venta["producto"])

        return resultado

    def venta_mayor(self):
        producto_mayor = ""
        valor_mayor = 0

        for venta in self.ventas:
            total = venta["cantidad"] * venta["precio"]

            if total > valor_mayor:
                valor_mayor = total
                producto_mayor = venta["producto"]

        return producto_mayor, valor_mayor


registro = RegistroVentas()

registro.registrar_venta("Laptop", 2, 800)
registro.registrar_venta("Mouse", 5, 25)
registro.registrar_venta("Teclado", 3, 50)
registro.registrar_venta("Monitor", 2, 300)

print(registro.ventas)
print(registro.total_ventas())
print(registro.ventas_mayores(500))
print(registro.venta_mayor())
