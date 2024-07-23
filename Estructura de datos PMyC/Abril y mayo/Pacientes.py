#Class pacientes:
#Atributos: nombre, edad, genero
class Paciente:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.siguiente = None
#Class RegistroPacientes:
#Metodos: agregar_paciente(), mostrar_pacientes(), buscar_paciente(), eliminar_paciente()
class RegistroPacientes:
    def __init__(self):
        #Asumimos que empieza en cero pacientes
        self.primer_paciente = None
    #Agregar_paciente: 
    #obj: agrega un paciente a la lista
    def agregar_paciente(self, paciente):
        if not self.primer_paciente:
            self.primer_paciente = paciente
        else:
            actual = self.primer_paciente
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = paciente
    #mostrar_pacientes:
    #obj: muestra la lista de los pacientes
    def mostrar_pacientes(self):
        actual = self.primer_paciente
        while actual:
            print("Nombre:", actual.nombre)
            print("Edad:", actual.edad)
            print("Género:", actual.genero)
            print("-----------------------")
            actual = actual.siguiente

    #buscar_paciente:
    #obj: busca un paciente
    def buscar_paciente(self, nombre):
        actual = self.primer_paciente
        while actual:
            if actual.nombre == nombre:
                print("Paciente encontrado:")
                print("Nombre:", actual.nombre)
                print("Edad:", actual.edad)
                print("Género:", actual.genero)
                return
            actual = actual.siguiente
        print("Paciente no encontrado.")

    def eliminar_paciente(self, nombre):
        actual = self.primer_paciente
        previo = None
        while actual:
            if actual.nombre == nombre:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.primer_paciente = actual.siguiente
                print("Paciente eliminado.")
                return
            previo = actual
            actual = actual.siguiente
        print("Paciente no encontrado.")

# Crear instancias de pacientes
registro = RegistroPacientes()
# Agregar pacientes
registro.agregar_paciente(Paciente("Juan", 30, "Masculino"))
registro.agregar_paciente(Paciente("María", 25, "Femenino"))
registro.agregar_paciente(Paciente("Pedro", 40, "Masculino"))

# Mostrar pacientes
print("Pacientes registrados:")
registro.mostrar_pacientes()

# Buscar paciente
print("Buscando paciente:")
registro.buscar_paciente("María")

# Eliminar paciente
print("Eliminando paciente:")
registro.eliminar_paciente("Juan")

# Mostrar pacientes actualizados
print("Pacientes después de eliminar:")
registro.mostrar_pacientes()
