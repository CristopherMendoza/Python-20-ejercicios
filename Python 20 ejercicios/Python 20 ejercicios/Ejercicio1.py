class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0

        suma = sum(self.notas)
        promedio = suma / len(self.notas)

        return promedio


calificador = Calificador()

print(calificador.cargar_notas(80, 90, 105, 70, -5, 100))
print(calificador.promedio())