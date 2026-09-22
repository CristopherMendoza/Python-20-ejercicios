class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        if letra.lower() in "aeiou":
            return True
        else:
            return False

    def contar_por_tipo(self, texto):
        vocales = 0
        consonantes = 0
        digitos = 0

        for letra in texto:
            if self.solo_vocales(letra):
                vocales += 1
            elif letra.isdigit():
                digitos += 1
            elif letra.isalpha():
                consonantes += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return {
            'vocales': vocales,
            'consonantes': consonantes,
            'digitos': digitos
        }


analizador = AnalizadorString()

print(analizador.contar_por_tipo("Hola123"))
print(analizador.contar_por_tipo("Python2026"))
print(analizador.texto_mas_largo)

#Tenga un método agregar_pedido(cliente, producto, cantidad, precio) que guarde cada pedido en una lista de diccionarios.
#Tenga un método total_pedidos() que calcule y retorne el valor total de todos los pedidos.
#Tenga un método pedidos_cliente(cliente) que retorne una lista con los nombres de los productos pedidos por ese cliente.
#Tenga un método pedido_mayor() que retorne una tupla con el nombre del cliente y el valor de su pedido individual más alto.

class GestorPedidos:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, cliente, producto, cantidad, precio):
        pedido = {
            "cliente": cliente,
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio
        }

        self.pedidos.append(pedido)

    def total_pedidos(self):
        total = 0

        for pedido in self.pedidos:
            total += pedido["cantidad"] * pedido["precio"]

        return total

    def pedidos_cliente(self, cliente):
        resultado = []

        for pedido in self.pedidos:
            if pedido["cliente"] == cliente:
                resultado.append(pedido["producto"])

        return resultado

    def pedido_mayor(self):
        cliente_mayor = ""
        valor_mayor = 0

        for pedido in self.pedidos:
            valor = pedido["cantidad"] * pedido["precio"]

            if valor > valor_mayor:
                valor_mayor = valor
                cliente_mayor = pedido["cliente"]

        return cliente_mayor, valor_mayor


gestor = GestorPedidos()

gestor.agregar_pedido("Ana", "Laptop", 1, 800)
gestor.agregar_pedido("Carlos", "Mouse", 3, 25)
gestor.agregar_pedido("Ana", "Teclado", 2, 50)
gestor.agregar_pedido("Pedro", "Monitor", 2, 300)

print(gestor.pedidos)
print(gestor.total_pedidos())
print(gestor.pedidos_cliente("Ana"))
print(gestor.pedido_mayor())

