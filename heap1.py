class Heap:
    def _init_(self):
        self.heap = []

    def heapify(self, i, n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < n and self.heap[left_child] > self.heap[smallest]:
            smallest = left_child
        if right_child < n and self.heap[right_child] > self.heap[smallest]:
            smallest = right_child
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest, n)

    def build(self, a):
        self.heap = a
        n = len(a)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i, n)

        for i in range(n-1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]  
            self.heapify(0, i)

    def insert(self, data):
        self.heap.append(data)
        n = len(self.heap)-1
        while n > 0:
            parrent = (n - 1) // 2
            if self.heap[parrent] > self.heap[n]:
                self.heap[parrent], self.heap[n] = self.heap[n], self.heap[parrent]
                n = parrent
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
        self.heapify(idx, len(self.heap))
        return element

    # def sort(self):
    #     sorted=[]
    #     while self.heap:
    #         self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
    #         element=self.heap.pop()
    #         sorted.append(element)
    #         self.heapify(0,len(self.heap))
    #     return sorted
    

h=Heap()
print([7,5,3,0,4,72,38,45,87,342,76])
h.build([7,5,3,0,4,72,38,45,87,342,76])
print(h.heap)

# h.remove(3)
# print(h.heap)

# print('sorted=',h.sort())