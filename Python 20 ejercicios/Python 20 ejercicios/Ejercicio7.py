class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0

        suma = sum(self.personas.values())
        promedio = suma / len(self.personas)

        return promedio


gestor = GestorPersonas()

gestor.agregar_persona("Ana", 20)
gestor.agregar_persona("Carlos", 17)
gestor.agregar_persona("Maria", 25)
gestor.agregar_persona("Pedro", 30)

print(gestor.personas)
print(gestor.personas_mayores(18))
print(gestor.edad_promedio())