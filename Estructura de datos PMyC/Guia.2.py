class NodoEstudiante:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos
        self.siguiente = None

class ListaCurso:
    def __init__(self):
        self.primer_estudiante = None

    def agregar(self, nombres, apellidos):
        nuevo_estudiante = NodoEstudiante(nombres, apellidos)
        if not self.primer_estudiante:
            self.primer_estudiante = nuevo_estudiante
        else:
            actual = self.primer_estudiante
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_estudiante

    def buscarApellido(self, apellidos):
        actual = self.primer_estudiante
        while actual:
            if actual.apellidos == apellidos:
                return actual.nombres, actual.apellidos
            actual = actual.siguiente
        return None

    def buscarNombre(self, nombre):
        actual = self.primer_estudiante
        while actual:
            if actual.nombres == nombre:
                return actual.nombres, actual.apellidos
            actual = actual.siguiente
        return None

# Ejemplo de uso:
lista_curso = ListaCurso()
lista_curso.agregar("Juan", "Perez")
lista_curso.agregar("Maria", "Gomez")
lista_curso.agregar("Luis", "Gonzalez")

print(lista_curso.buscarApellido("Gomez"))  # Salida: ('Maria', 'Gomez')
print(lista_curso.buscarNombre("Juan"))     # Salida: ('Juan', 'Perez')
