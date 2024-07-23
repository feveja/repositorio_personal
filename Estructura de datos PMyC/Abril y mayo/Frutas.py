class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente

# Crear una lista enlazada e ingresar algunas frutas
lista_frutas = ListaEnlazada()
lista_frutas.agregar("Manzana")
lista_frutas.agregar("Banana")
lista_frutas.agregar("Fresa")
lista_frutas.agregar("Piña")

# Imprimir la lista de frutas
print("Lista de Frutas:")
lista_frutas.imprimir()
