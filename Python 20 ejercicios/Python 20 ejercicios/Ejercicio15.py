class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma = sum(divisores[:-1])

        if suma == numero:
            return True
        else:
            return False

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


finder = DivisorFinder()

print(finder.encontrar_divisores(12))
print(finder.es_perfecto(6))
print(finder.es_perfecto(12))
print(finder.encontrar_multiples_divisores(6, 10, 12, 28))