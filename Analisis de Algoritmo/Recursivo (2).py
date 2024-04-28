class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._bubble_up(parent_index)

    def build_heap(self, lst):
        for num in lst:
            self.insert(num)

    def display_heap(self, index=0, level=0):
        if index < len(self.heap):
            self.display_heap(2 * index + 2, level + 1)
            print('   ' * level + str(self.heap[index]))
            self.display_heap(2 * index + 1, level + 1)

# Ejemplo de uso
numbers = [26, 90, 23, 44, 69, 8, 55, 20, 76, 14, 100, 53]
heap = Heap()
heap.build_heap(numbers)
heap.display_heap()