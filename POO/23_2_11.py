class Estudiante:
    def __init__(self):
        self.nombre = ""
        self.institucion = ""

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setInstitucion(self, institucion):
        self.institucion = institucion

    def getInstitucion(self):
        return self.institucion

class EstudianteUniversitario(Estudiante):
    def __init__(self):
        super().__init__()
        self.carrera = ""

    def setCarrera(self, carrera):
        self.carrera = carrera

    def getCarrera(self):
        return self.carrera

class EstudianteEducacionMedia(Estudiante):
    def __init__(self):
        super().__init__()
        self.curso = 0

    def setCurso(self, curso):
        self.curso = curso

    def getCurso(self):
        return self.curso