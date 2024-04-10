class Heap:
    def __init__(self):
        self.heap = []

    def _swap(self, i, j):
        """Intercambia los elementos en las posiciones i y j del heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up_recursive(self, index):
        """Reorganiza el heap hacia arriba de manera recursiva."""
        if index != 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                self._heapify_up_recursive(parent_index)

    def _heapify_down_recursive(self, index):
        """Reorganiza el heap hacia abajo de manera recursiva."""
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down_recursive(smallest)

    def insert_recursive(self, value):
        """Inserta un elemento en el heap de manera recursiva."""
        self.heap.append(value)
        self._heapify_up_recursive(len(self.heap) - 1)

    def remove_min_recursive(self):
        """Elimina el mínimo elemento del heap de manera recursiva."""
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._heapify_down_recursive(0)
        return min_value

    def _heapify_up_iterative(self, index):
        """Reorganiza el heap hacia arriba de manera iterativa."""
        while index != 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down_iterative(self, index):
        """Reorganiza el heap hacia abajo de manera iterativa."""
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def insert_iterative(self, value):
        """Inserta un elemento en el heap de manera iterativa."""
        self.heap.append(value)
        self._heapify_up_iterative(len(self.heap) - 1)

    def remove_min_iterative(self):
        """Elimina el mínimo elemento del heap de manera iterativa."""
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._heapify_down_iterative(0)
        return min_value
# Ejemplo de uso
heap = Heap()
heap.insert_recursive(3)
heap.insert_recursive(2)
heap.insert_recursive(1)
print("Heap después de insertar 3, 2, 1:", heap.heap)

print("Eliminando el mínimo (recursivo):", heap.remove_min_recursive())
print("Heap después de eliminar el mínimo:", heap.heap)

heap.insert_iterative(5)
heap.insert_iterative(4)
print("Heap después de insertar 5, 4 (iterativo):", heap.heap)

print("Eliminando el mínimo (iterativo):", heap.remove_min_iterative())
print("Heap después de eliminar el mínimo:", heap.heap)