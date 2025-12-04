class Alumno:
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula


    def estudiar(self):
        pass

    def inscribirse(self):
        pass

alumno1 = Alumno("juan perez", 20, "A12345")
alumno2 = Alumno("maria lopez", 22, "B67890")


class Curso:
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

    def asginar(self):
        pass

curso1 = Curso("Matematicas", "MATH101", 4)
curso2 = Curso("Historia", "HIST201", 3)

class Profesor:
    def __init__(self, nombre, experiencia, num_profesor):
        self.nombre = nombre
        self.departamento = experiencia
        self.salario = num_profesor

    def impartir(self):
        pass

    def evaluar(self):
        pass

profesor1 = Profesor("Dagoberto Fiscal", 10, "P001")
profesor2 = Profesor("Ociel Rodriguez", 8, "P002")