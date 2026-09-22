class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)


gestor = GestorTemperatura()

gestor.registrar_temperatura(25)
gestor.registrar_temperatura(30)

gestor.registrar_multiples(28, 32, 24, 27)

print(gestor.temperaturas)
print(gestor.minima())
print(gestor.maxima())
print(gestor.promedio())

#Tenga un método agregar_empleado(nombre, salario, departamento) que guarde la información de cada empleado en una lista de diccionarios.
#Tenga un método empleados_departamento(departamento) que retorne una lista con los nombres de los empleados que pertenecen al departamento indicado.
#Tenga un método salario_promedio() que calcule y retorne el salario promedio de todos los empleados.
#Tenga un método empleado_mejor_pagado() que retorne una tupla con el nombre y salario del empleado que tenga el salario más alto.

class GestorEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, nombre, salario, departamento):
        empleado = {
            "nombre": nombre,
            "salario": salario,
            "departamento": departamento
        }

        self.empleados.append(empleado)

    def empleados_departamento(self, departamento):
        resultado = []

        for empleado in self.empleados:
            if empleado["departamento"] == departamento:
                resultado.append(empleado["nombre"])

        return resultado

    def salario_promedio(self):
        if len(self.empleados) == 0:
            return 0

        suma = 0

        for empleado in self.empleados:
            suma += empleado["salario"]

        return suma / len(self.empleados)

    def empleado_mejor_pagado(self):
        nombre_mayor = ""
        salario_mayor = 0

        for empleado in self.empleados:
            if empleado["salario"] > salario_mayor:
                salario_mayor = empleado["salario"]
                nombre_mayor = empleado["nombre"]

        return nombre_mayor, salario_mayor


gestor = GestorEmpleados()

gestor.agregar_empleado("Ana", 800, "Ventas")
gestor.agregar_empleado("Carlos", 1200, "Sistemas")
gestor.agregar_empleado("Maria", 950, "Ventas")
gestor.agregar_empleado("Pedro", 1500, "Sistemas")

print(gestor.empleados)
print(gestor.empleados_departamento("Ventas"))
print(gestor.salario_promedio())
print(gestor.empleado_mejor_pagado())