class Heap:
    def __init__(self):
        self.heap = []

    def min_heapify(self, i, n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < n and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < n and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest, n)
            
    def max_heapify(self, i, n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        largest = i

        if left_child < n and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < n and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest, n)


    def build_min(self, a):
        self.heap = a
        n = len(a)
        for i in range(n // 2 - 1, -1, -1):
            self.min_heapify(i, n)

    def build_max(self, a):
        self.heap = a
        n = len(a)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(i, n)

    def insert(self, data):
        self.heap.append(data)
        n = len(self.heap) - 1
        while n > 0:
            parent = (n - 1) // 2
            if self.heap[parent] > self.heap[n]:
                self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
                n = parent
            else:
                break
    
    def remove(self, data):
        idx = None
        for i in range(len(self.heap)):
            if self.heap[i] == data:
                idx = i
                break

        if idx is None:
            return None
        self.heap[idx], self.heap[-1] = self.heap[-1], self.heap[idx]
        element = self.heap.pop()
        self.min_heapify(idx, len(self.heap))
        return element
    
    def asc_sort(self):
        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.max_heapify(0, i)

    def desc_sort(self):
        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.min_heapify(0, i) 

    def __str__(self):
        return str(self.heap)

    
    

h=Heap()
arr = [7,5,3,0,4,72,38,45,87,342,76]
print("Array: ", arr)
h.build_min(arr)
print("Min Heap: ", h)
h.desc_sort()
print("Descending sorted: ", h)
h.build_max(arr)
print("Max Heap: ", h)
h.asc_sort()
print("Ascending sorted: ", h)
