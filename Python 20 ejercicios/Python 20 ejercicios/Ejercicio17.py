class AgrupadorEdades:
    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        if len(self.grupos[categoria]) == 0:
            return 0

        suma = sum(self.grupos[categoria])
        promedio = suma / len(self.grupos[categoria])

        return promedio


agrupador = AgrupadorEdades()

print(agrupador.clasificar_edad(10))
print(agrupador.clasificar_edad(16))
print(agrupador.clasificar_edad(30))
print(agrupador.clasificar_edad(70))

print(agrupador.agrupar_por_categoria(8, 10, 15, 17, 25, 30, 65, 70))

print(agrupador.edad_promedio_categoria("adulto"))
print(agrupador.edad_promedio_categoria("niño"))