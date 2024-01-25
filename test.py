import heapq

class Min_heap:
    def __init__(self):
        self.heap = []

    def build_heap(self, arr):
        self.heap = arr[:]
        heapq.heapify(self.heap)

    def insert(self, value):
        heapq.heappush(self.heap, value)
    
    def remove_min(self):
        if self:
            return heapq.heappop(self.heap)
        return None
    
    def search(self, val):
        return val in self.heap
    
    def print_heap(self):
        print("Heap: ", self.heap)

    def heap_sort(self):
        sorted_element = []
        while self.heap:
            sorted_element.append(self.remove_min())
        return sorted_element
    

arr = [1,5,8,3,1,6,8]
heap = Min_heap()
heap.build_heap(arr)
heap.print_heap()
# heap.insert(2)
heap.print_heap()
print(heap.search(3))

print(heap.heap_sort())