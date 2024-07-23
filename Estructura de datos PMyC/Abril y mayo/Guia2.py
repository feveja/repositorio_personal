class NodoDatos:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.siguiente = None

    def imprimir(self):
        print(self.nombre)
        print(self.rut)

class ListaDatos:
    def __init__(self):
        self.cabecera = NodoDatos(None, None)

    def agrega_al_final(self, nombre, rut):
        nuevo_nodo = NodoDatos(nombre, rut)
        actual = self.cabecera
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def agrega_al_principio(self, nombre, rut):
        nuevo_nodo = NodoDatos(nombre, rut)
        nuevo_nodo.siguiente = self.cabecera.siguiente
        self.cabecera.siguiente = nuevo_nodo
    

class NodoDobleDatos:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.siguiente = None
        self.anterior = None
        

class ListaDobleEnlace:
    def __init__(self):
        self.cabecera = NodoDobleDatos(None, None)

    def agrega_al_final(self, nombre, rut):
        nuevo_nodo = NodoDobleDatos(nombre, rut)
        actual = self.cabecera
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual

    def agrega_al_principio(self, nombre, rut):
        nuevo_nodo = NodoDobleDatos(nombre, rut)
        nuevo_nodo.siguiente = self.cabecera.siguiente
        if self.cabecera.siguiente:
            self.cabecera.siguiente.anterior = nuevo_nodo
        nuevo_nodo.anterior = self.cabecera
        self.cabecera.siguiente = nuevo_nodo
    def mostrar_Lista(self):
        actual = self.cabecera.siguiente
        while actual:
            actual.imprimir()
            actual = actual.siguiente
        
# Crear una lista de enlace simple
lista_simple = ListaDatos()

# Agregar nodos al final de la lista simple
lista_simple.agrega_al_final("Marcelo Viheltsa", 12345678)
lista_simple.agrega_al_final("Ana López", 87654321)

# Agregar un nodo al principio de la lista simple
lista_simple.agrega_al_principio("Juan Pérez", 55555555)

