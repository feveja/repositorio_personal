class NodoPolinomio:
    def __init__(self, coeficiente, potencia):
        self.coeficiente = coeficiente
        self.potencia = potencia
        self.siguiente = None  # Referencia al siguiente NodoPolinomio en la lista

class Polinomio:
    def __init__(self):
        self.cabeza = None  # Inicialmente, el polinomio está vacío

    def valor(self, x):
        """
        Evalúa el polinomio en un valor dado de x.
        """
        valor_total = 0
        nodo_actual = self.cabeza
        # Aqui es donde se hace la operación matemática donde se usa lo que sabemos de lista enlazada
        while nodo_actual:
            valor_total += nodo_actual.coeficiente * (x ** nodo_actual.potencia)
            nodo_actual = nodo_actual.siguiente
        return valor_total

    def agregaTermino(self, coeficiente, potencia):
        """
        Agrega un término al polinomio.
        """
        nuevo_termino = NodoPolinomio(coeficiente, potencia)
        if not self.cabeza:  # Si el polinomio está vacío
            self.cabeza = nuevo_termino
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_termino

# Ejemplo de uso
p = Polinomio()
p.agregaTermino(3, 2) # Agrega el término 3*x**2
p.agregaTermino(2, 1) # Agrega el termino 2*x
#Entonces tendremos 3x**2 + 2x
#Le damos un valor a x en este caso x=3 entonces 3*(3)**2 + 2*3 = 33
print(p.valor(3))  # Evalúa el polinomio en x=3
