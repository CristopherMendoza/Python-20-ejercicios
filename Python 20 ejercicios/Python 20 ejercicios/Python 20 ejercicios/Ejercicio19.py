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

#agregar_contacto(nombre, telefono, correo) → agrega un contacto.
#buscar_contacto(nombre) → devuelve los datos del contacto.
#actualizar_telefono(nombre, nuevo_telefono) → cambia el teléfono de un contacto.
#eliminar_contacto(nombre) → elimina un contacto.
#cantidad_contactos() → devuelve cuántos contactos existen.

class AgendaContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, correo):
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "correo": correo
        }

        self.contactos.append(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto["nombre"] == nombre:
                return contacto

        return None

    def actualizar_telefono(self, nombre, nuevo_telefono):
        for contacto in self.contactos:
            if contacto["nombre"] == nombre:
                contacto["telefono"] = nuevo_telefono

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto["nombre"] == nombre:
                self.contactos.remove(contacto)
                return

    def cantidad_contactos(self):
        return len(self.contactos)


agenda = AgendaContactos()

agenda.agregar_contacto("Ana", "0991111111", "ana@gmail.com")
agenda.agregar_contacto("Carlos", "0982222222", "carlos@gmail.com")
agenda.agregar_contacto("Maria", "0973333333", "maria@gmail.com")

print(agenda.contactos)

print(agenda.buscar_contacto("Carlos"))

agenda.actualizar_telefono("Carlos", "0969999999")

print(agenda.buscar_contacto("Carlos"))

agenda.eliminar_contacto("Ana")

print(agenda.contactos)
print(agenda.cantidad_contactos())