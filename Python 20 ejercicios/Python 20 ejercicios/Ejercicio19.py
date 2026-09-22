class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        else:
            return False

    def productos_bajo_stock(self, minimo):
        resultado = []

        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)

        return resultado


inventario = Inventario()

inventario.agregar_stock("Laptop", 10)
inventario.agregar_stock("Mouse", 5)
inventario.agregar_stock("Teclado", 8)

print(inventario.stock)

print(inventario.restar_stock("Mouse", 3))
print(inventario.stock)

print(inventario.restar_stock("Teclado", 10))

print(inventario.productos_bajo_stock(5))