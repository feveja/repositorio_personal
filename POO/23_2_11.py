# Clase Estudiante

class Estudiante:
    def __init__(self):
        self.nombre = ""
        self.institucion = ""

    # Crea el nombre del estudiante
    def setNombre(self, nombre):
        self.nombre = nombre

    # Imprime el nombre del estudiante
    def getNombre(self):
        return self.nombre

    # Crea el nombre de la institución académica
    def setInstitucion(self, institucion):
        self.institucion = institucion

    # Imprime el nombre de la institución académica
    def getInstitucion(self):
        return self.institucion


# Clase EstudianteUniversitario(Estudiante)
# Hereda todos los atributos de la clase madre
class EstudianteUniversitario(Estudiante):
    def __init__(self):
        super().__init__()
        self.carrera = ""

    # Crea el nombre de la carrera que está cursando el estudiante
    def setCarrera(self, carrera):
        self.carrera = carrera

    # Imprime el nombre de la carrera que está cursando el estudiante
    def getCarrera(self):
        return self.carrera


# Clase EstudianteEducacionMedia(Estudiante)
# Hereda todos los atributos de la clase madre
class EstudianteEducacionMedia(Estudiante):
    def __init__(self):
        super().__init__()
        self.curso = 0

    # Crea el nombre del curso que está cursando el estudiante
    def setCurso(self, curso):
        self.curso = curso

    # Imprime el nombre del curso que está cursando el estudiante
    def getCurso(self):
        return self.curso


A = EstudianteUniversitario()
A.setNombre("Antoine Briones")
A.setInstitucion("Universidad de los Lagos")
A.setCarrera("Ingeniería Civil en Informática")
assert A.getNombre() == "Antoine Briones"
assert A.getInstitucion() == "Universidad de los Lagos"
assert A.getCarrera() == "Ingeniería Civil en Informática"

F = EstudianteEducacionMedia()
F.setNombre("Antoine Briones")
F.setInstitucion("Universidad de los Lagos")
F.setCurso("Segundo Medio B")
assert F.getNombre() == "Antoine Briones"
assert F.getInstitucion() == "Universidad de los Lagos"
assert F.getCurso() == "Segundo Medio B"
