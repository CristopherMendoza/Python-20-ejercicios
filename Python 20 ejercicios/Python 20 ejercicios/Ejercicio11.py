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