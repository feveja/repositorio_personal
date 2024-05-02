class Alumno:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.siguiente = None

class RegistroAlumnos:
    def __init__(self):
        self.primer_alumno = None

    def agregar_alumno(self, alumno):
        if not self.primer_alumno:
            self.primer_alumno = alumno
        else:
            actual = self.primer_alumno
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = alumno

    def mostrar_alumnos(self):
        actual = self.primer_alumno
        while actual:
            print("Nombre:", actual.nombre)
            print("Edad:", actual.edad)
            print("Grado:", actual.grado)
            print("-----------------------")
            actual = actual.siguiente

    def buscar_alumno(self, nombre):
        actual = self.primer_alumno
        while actual:
            if actual.nombre == nombre:
                print("Alumno encontrado:")
                print("Nombre:", actual.nombre)
                print("Edad:", actual.edad)
                print("Grado:", actual.grado)
                return
            actual = actual.siguiente
        print("Alumno no encontrado.")

    def eliminar_alumno(self, nombre):
        actual = self.primer_alumno
        previo = None
        while actual:
            if actual.nombre == nombre:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.primer_alumno = actual.siguiente
                print("Alumno eliminado.")
                return
            previo = actual
            actual = actual.siguiente
        print("Alumno no encontrado.")

# Crear instancias de alumnos
registro_alumnos = RegistroAlumnos()

# Agregar alumnos
registro_alumnos.agregar_alumno(Alumno("Juan", 15, "Noveno grado"))
registro_alumnos.agregar_alumno(Alumno("María", 14, "Octavo grado"))
registro_alumnos.agregar_alumno(Alumno("Pedro", 16, "Décimo grado"))

# Mostrar alumnos
print("Alumnos registrados:")
registro_alumnos.mostrar_alumnos()

# Buscar alumno
print("Buscando alumno:")
registro_alumnos.buscar_alumno("María")

# Eliminar alumno
print("Eliminando alumno:")
registro_alumnos.eliminar_alumno("Juan")

# Mostrar alumnos actualizados
print("Alumnos después de eliminar:")
registro_alumnos.mostrar_alumnos()
