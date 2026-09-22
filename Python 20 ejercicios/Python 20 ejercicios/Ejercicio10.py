class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        tarea = (descripcion, prioridad)
        self.tareas.append(tarea)

    def tareas_prioritarias(self):
        resultado = []

        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)

        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break


gestor = Tareas()

gestor.agregar_tarea("Estudiar Python", "alta")
gestor.agregar_tarea("Hacer ejercicio", "baja")
gestor.agregar_tarea("Terminar tarea", "alta")
gestor.agregar_tarea("Ordenar cuarto", "media")

print(gestor.tareas)
print(gestor.tareas_prioritarias())

gestor.eliminar_completada("Hacer ejercicio")

print(gestor.tareas)