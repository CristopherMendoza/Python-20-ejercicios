class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)

        return resultado


inversor = InversorSecuencia()

lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30]

print(inversor.invertir_lista(lista1))
print(inversor.invertir_multiples(lista1, lista2))