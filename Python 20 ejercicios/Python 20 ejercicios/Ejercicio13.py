class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        mayor = max(len(lista1), len(lista2))

        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []

        for lista in listas:
            if len(resultado) == 0:
                resultado = lista.copy()
            else:
                resultado = self.intercalar(resultado, lista)

        return resultado


combinador = CombinadorListas()

lista1 = [1, 3, 5]
lista2 = [2, 4, 6]

print(combinador.intercalar(lista1, lista2))

lista3 = [7, 8, 9]

print(combinador.intercalar_multiples(lista1, lista2, lista3))