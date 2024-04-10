class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, idx):
        if idx == 0:
            return
        parent_idx = (idx - 1) // 2
        if self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._bubble_up(parent_idx)

    def pop_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_val

    def _sink_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        smallest_idx = idx

        if (left_child_idx < len(self.heap) and
                self.heap[left_child_idx] < self.heap[smallest_idx]):
            smallest_idx = left_child_idx
        if (right_child_idx < len(self.heap) and
                self.heap[right_child_idx] < self.heap[smallest_idx]):
            smallest_idx = right_child_idx

        if smallest_idx != idx:
            self.heap[idx], self.heap[smallest_idx] = self.heap[smallest_idx], self.heap[idx]
            self._sink_down(smallest_idx)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, idx):
        if idx == 0:
            return
        parent_idx = (idx - 1) // 2
        if self.heap[idx] > self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._bubble_up(parent_idx)

    def pop_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_val

    def _sink_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        largest_idx = idx

        if (left_child_idx < len(self.heap) and
                self.heap[left_child_idx] > self.heap[largest_idx]):
            largest_idx = left_child_idx
        if (right_child_idx < len(self.heap) and
                self.heap[right_child_idx] > self.heap[largest_idx]):
            largest_idx = right_child_idx

        if largest_idx != idx:
            self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx]
            self._sink_down(largest_idx)
