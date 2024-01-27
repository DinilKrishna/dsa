class Heap:
    def __init__(self):
        self.heap = []

    def build_heap(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def remove(self, value):
        idx = self.search(value)
        if idx is not None:
            self.heap[idx], self.heap[-1] = self.heap[-1], self.heap[idx]
            removed_value = self.heap.pop()
            self.heapify_down(idx)
            return removed_value
        return None

    def search(self, value):
        for i, element in enumerate(self.heap):
            if element == value:
                return i
        return None

    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def heapify_down(self, i):
        n = len(self.heap)
        while i < n:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            largest = i

            if left_child < n and self.heap[left_child] > self.heap[largest]:
                largest = left_child
            if right_child < n and self.heap[right_child] > self.heap[largest]:
                largest = right_child

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def print_heap(self):
        print("Heap:", self.heap)

    def heap_sort(self):
        sorted_arr = []
        while self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            sorted_arr.append(self.heap.pop())
            self.heapify_down(0)

        return sorted_arr


# Example usage:
heap = Heap()
arr = [4, 2, 7, 8, 2, 5, 8, 3, 5, 1, 0, 9, 6]
heap.build_heap(arr)

heap.print_heap()

heap.insert(10)
heap.print_heap()

heap.remove(5)
heap.print_heap()

print("Search for 7:", heap.search(7))

sorted_arr = heap.heap_sort()
print("Heap after heap sort:", sorted_arr)
