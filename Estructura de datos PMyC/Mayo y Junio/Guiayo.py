class NodoDobleDatos:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.siguiente = None
        self.anterior = None

    def imprimir(self):
        print(f"{self.nombre}\n{self.rut}")

class ListaDobleEnlace:
    def __init__(self):
        self.cabeza = NodoDobleDatos(None, None)

    def agrega_al_final(self, nombre, rut):
        nuevo_nodo = NodoDobleDatos(nombre, rut)
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual

    def agrega_al_principio(self, nombre, rut):
        nuevo_nodo = NodoDobleDatos(nombre, rut)
        if self.cabeza.siguiente is None:
            self.cabeza.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cabeza
        else:
            nuevo_nodo.siguiente = self.cabeza.siguiente
            self.cabeza.siguiente.anterior = nuevo_nodo
            self.cabeza.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cabeza
