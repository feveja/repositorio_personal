#Crea un arbol binario de prioridad como una clase
class Heap:
    def __init__(self):
        #crea la lista que contendra los valores
        self.heap = []

    #agrega un valor a la lista del arbol
    def insert(self, value):
        self.heap.append(value)
        #se ordenara el elemento en el arbol
        #el indice a trabajar sera el del ultimo elemento agregado
        index = len(self.heap) - 1
        #mientras el indice sea mayor a 0
        while index > 0:
            #identifica el padre del nuevo elemento agregado
            parent_index = (index - 1) // 2
            #si el valor agregado es mayor que el padre los intercambia
            if self.heap[parent_index] < value:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                #el nuevo indice para seguir el ciclo iterativo es el padre
                index = parent_index
            else:
                break
    
    #extrae el elemento mayor del arbol
    def extract_max(self):
        #si el arbol esta vacio no hace nada
        if len(self.heap) == 0:
            return None
        #dado que la lista esta ordenada , el valor mayor siempre estara en el principio
        #de la lista
        max_value = self.heap[0]
        #elimina el ultimo valor
        last_value = self.heap.pop()
        #si el arbol no esta vacio nuevamente, y el ultimo elemento que se elimino es mayor que
        #el primer elemento toma el valor del ultimo elemento y lo convierte en el primero
        if len(self.heap) > 0 and last_value > self.heap[0]:
            self.heap[0] = last_value
            #ordena usando el metodo bubble_down
            self.bubble_down(0)
        #retorna el elemento mayor
        return max_value

    def bubble_down(self, index):
        #ejecuta un ciclo
        while True:
            #identifica el hijo de la izquierda y el hijo de la derecha
            #del indice ingresado
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            #identifica el indice padre
            max_index = index
            #primero comprueba que el indice del hijo de la izquierda (o derecha) exista
            #luego compara el contenido del hijo de la izquierda (o derecha) con el padre 
            #si es mayor los intercambia y el nodo hijo de la izquierda (o derecha) pasa 
            #a ser el nuevo padre
            #se detiene cuando el indice no haya cambiado
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index == index:
                break

            #si luego de lo anterior el indice cambio se intercambian los valores
            #con el nuevo padre
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            index = max_index

    def print_heap(self):
        print("Heap:")
        for i in range(len(self.heap)):
            print(f"{self.heap[i]:4}", end="")
            if (i + 1) % 4 == 0:
                print()
        print()

    def build_heap(self, values):
        self.heap = values[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self.bubble_down(i)

if __name__ == "__main__":
    heap = Heap()
    values = [19, 28, 20, 59, 33, 76, 39, 6, 11, 22]
    print("Valores:")
    print(values)
    heap.build_heap(values)
    heap.print_heap()
    print("Insertar 40:")
    heap.insert(40)
    heap.print_heap()
    print("Extraer máximo:")
    print(heap.extract_max())
    heap.print_heap()
    print("Insertar 1:")
    heap.insert(1)
    heap.print_heap()
    print("Extraer máximo:")
    print(heap.extract_max())
    heap.print_heap()