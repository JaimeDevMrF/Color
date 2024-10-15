class Quimico:
    def __init__(self, nombre, especialidad, experiencia, empresa, proyectos_activos):
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia
        self.empresa = empresa
        self.proyectos = proyectos_activos
    def mostrar_informacion(self):
        print(f"nombre: {self.nombre}\nEspecialidad: {self.especialidad}\nExperiencia: {self.experiencia} años\nEmpresa: {self.empresa}\nProyectos Activos: {self.proyectos}")
    
trabajador = Quimico("Jaime", "Farmaceutica", 10, "Laboratorios C.A", 3)
trabajador1 = Quimico("Angel", "Alimentos", 6, "Colombia Chemestry", 1)
trabajador2 = Quimico("Fabian", "Bioquimico", 3, "Bioquimica s.r.l", 7)


trabajador.mostrar_informacion()
trabajador1.mostrar_informacion()
trabajador2.mostrar_informacion()