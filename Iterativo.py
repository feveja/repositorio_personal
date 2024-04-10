class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < value:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_value = self.heap[0]
        last_value = self.heap.pop()
        if len(self.heap) > 0 and last_value > self.heap[0]:
            self.heap[0] = last_value
            self.bubble_down(0)
        return max_value

    def bubble_down(self, index):
        while True:
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            max_index = index
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index == index:
                break
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
    values = [26, 90, 23, 44, 69, 8, 55, 20, 76, 14, 100, 53]
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