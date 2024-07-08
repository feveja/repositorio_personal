#Crea un arbol binario de prioridad maximo con una clase.
class Heap:
    #El constructor contiene los nodos en una lista
    def __init__(self):
        self.heap = []

    #El metodo insertar agrega el nodo nuevo a la lista
    def insert(self, value):
        self.heap.append(value)
        #se entrega el largo de la lista menos 1 al metodo sift_up para ordenar los nodos
        self.sift_up(len(self.heap) - 1)

    #extrae el nodo de mayor valor dentro del arbol
    def extract_max(self):
        #si el arbol esta vacio no hace nada
        #el caso base es cuando el arbol esta vacio
        if len(self.heap) == 0:
            return None
        #gracias a que el arbol de prioridad esta ordenado el valor maximo es decir el mayor siempre estara en la primera posicion de la lista
        max_value = self.heap[0]
        #elimina el elemento de la lista
        self.heap[0] = self.heap.pop()
        #entrega el indice del valor borrado a un metodo que ordenara el arbol
        self.sift_down(0)
        #retorna el elemento mayor
        return max_value

    #ordena el arbol desde abajo hacia arriba
    #este metodo compara el valor del nodo en el indice que se entrega con el valor del nodo padre
    def sift_up(self, index):
        #si el indice es 0 no hace nada sera el nodo raiz
        #El caso base es cuando el indice es el primero
        if index == 0:
            return
        #identifica el padre, utilizando la formula para ordenar las posiciones
        #de los nodos es decir posicion p=1 el nodo hijo de la derecha sera el
        #nodo en posicion 2p+1 esto tambien permite conocer el padre del nodo hijo de la izquierda
        #ya que sera el mismo.
        parent_index = (index - 1) // 2
        #compara los valores del hijo con el padre
        if self.heap[parent_index] < self.heap[index]:
            #los da vuelta
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            #llama a la funcion recursivamente pero esta vez con el nuevo padre 
            self.sift_up(parent_index)

    #ordena el arbol desde arriba hacia abajo dado que se perdio el nodo raiz
    def sift_down(self, index):
        #identifica los indices de los hijos del nodo padre entregado
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        max_index = index

        #primero comprueba que el indice del hijo de la izquierda (o derecha) exista
        #luego compara el contenido del hijo de la izquierda (o derecha) con el padre 
        #si es mayor los intercambia y el nodo hijo de la izquierda (o derecha) pasa 
        #a ser el nuevo padre
        
        #El caso base es cuando no existen mas hijos
        #es decir cuando el indice es mayor que el largo de la lista de elementos.
        if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
            max_index = left_index
        if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
            max_index = right_index
        
        #si luego de lo anterior el indice cambio se intercambian los valores y llama recursivamente
        #con el nuevo padre
        if max_index != index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self.sift_down(max_index)

    #lee la lista y la imprime como un arreglo
    def print_heap(self):
        print("\nHeap:")
        for i in range(len(self.heap)):
            print(f"{self.heap[i]:4}", end="")
            if (i + 1) % 4 == 0:
                print()
        print()

    #dados unos valores construye el arbol y los ordena hacia abajo 
    def build_heap(self, values):
        self.heap = values[:]
        #luego de insertar los valores los ordena mediante el metodo sift_down
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.sift_down(i)

    #muestra el arbol ordenado
    def display_heap(self, index=0, level=0):
        if index < len(self.heap):
            self.display_heap(2 * index + 2, level + 1)
            print('   ' * level + str(self.heap[index]))
            self.display_heap(2 * index + 1, level + 1)

if __name__ == "__main__":
    heap = Heap()
    values = [19, 28, 20, 59, 33, 76, 39, 6, 11, 22]
    print("Values:")
    print(values)
    heap.build_heap(values)
    heap.print_heap()
    heap.display_heap()
    print("Insert 40:")
    heap.insert(40)
    heap.print_heap()
    heap.display_heap()
    print("Extract max:")
    print(heap.extract_max())
    heap.print_heap()
    heap.display_heap()
    print("Insert 1:")
    heap.insert(1)
    heap.print_heap()
    heap.display_heap()
    print("Extract max:")
    print(heap.extract_max())
    heap.print_heap()
    heap.display_heap()