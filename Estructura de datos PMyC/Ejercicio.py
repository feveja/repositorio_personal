class Nodo:
    def __init__(self, entero):
        self.sgte = None
        self.valor = entero

class ListaAtencion:
    def __init__(self):
        self.primero = None

    def agrega_al_principio(self, entero):
        nodo = Nodo(entero)
        if self.primero is None:
            self.primero = nodo
        else:
            nodo.sgte = self.primero
            self.primero = nodo

    def valor_del_final(self):
        if self.primero is None:
            return None
        else:
            aux = self.primero
            while aux is not None:
                if aux.sgte is None:
                    return aux.valor
                else:
                    aux = aux.sgte

    def eliminar_ultimo(self):
        if self.primero is None:
            return
        elif self.primero.sgte is None:
            self.primero = None
        else:
            aux = self.primero
            while aux.sgte.sgte is not None:
                aux = aux.sgte
            aux.sgte = None

    def agregar_al_final(self, entero):
        nodo = Nodo(entero)
        if self.primero is None:
            self.primero = nodo
        else:
            aux = self.primero
            while aux.sgte is not None:
                aux = aux.sgte
            aux.sgte = nodo

    def buscar_elemento(self, valor):
        posicion = 0
        aux = self.primero
        while aux is not None:
            if aux.valor == valor:
                return posicion
            aux = aux.sgte
            posicion += 1
        return -1

    def eliminar_en_posicion(self, posicion):
        if posicion < 0:
            return
        if posicion == 0:
            self.primero = self.primero.sgte
        else:
            anterior = None
            actual = self.primero
            contador = 0
            while contador < posicion and actual is not None:
                anterior = actual
                actual = actual.sgte
                contador += 1
            if actual is not None:
                anterior.sgte = actual.sgte

    def contar_elementos(self):
        contador = 0
        aux = self.primero
        while aux is not None:
            contador += 1
            aux = aux.sgte
        return contador

    def invertir_lista(self):
        anterior = None
        actual = self.primero
        while actual is not None:
            siguiente = actual.sgte
            actual.sgte = anterior
            anterior = actual
            actual = siguiente
        self.primero = anterior

# Ejemplo de uso:
lista1 = ListaAtencion()
lista1.agrega_al_principio(-1)
lista1.agrega_al_principio(2)

aux = lista1.primero
while aux is not None:
    print(aux.valor)
    aux = aux.sgte

print("Valor del último nodo:", lista1.valor_del_final())

lista1.eliminar_ultimo()
print("Lista después de eliminar el último elemento:")
aux = lista1.primero
while aux is not None:
    print(aux.valor)
    aux = aux.sgte
