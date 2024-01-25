import heapq

class MinHeap:
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

    def search(self, value):
        return value in self.heap

    def print_heap(self):
        print("Heap:", self.heap)

    def heap_sort(self):
        sorted_elements = []
        while self.heap:
            sorted_elements.append(self.remove_min())
        return sorted_elements

def bfs(heap):
    if heap:
        queue = [0]  # Index of the root element
        while queue:
            current_index = queue.pop(0)
            print(heap.heap[current_index], end=" ")

            left_child = 2 * current_index + 1
            right_child = 2 * current_index + 2

            if left_child < len(heap.heap):
                queue.append(left_child)
            if right_child < len(heap.heap):
                queue.append(right_child)

def dfs(heap):
    def dfs_recursive(index):
        if index < len(heap.heap):
            print(heap.heap[index], end=" ")
            dfs_recursive(2 * index + 1)
            dfs_recursive(2 * index + 2)

    if not heap.is_empty():
        dfs_recursive(0)

# Example Usage:
min_heap = MinHeap()

# Build heap
arr = [4, 2, 7, 8, 2, 5, 8, 3, 5, 1, 0, 9, 6]
min_heap.build_heap(arr)

# Insert into heap
min_heap.insert(10)

# Remove element from heap
min_heap.remove_min()

# Search
print("Is 5 in the heap?", min_heap.search(5))

# Print heap
min_heap.print_heap()

# Heap sort
sorted_elements = min_heap.heap_sort()
print("Sorted elements:", sorted_elements)

# # BFS
# print("BFS traversal:")
# bfs(min_heap)
# print()

# # DFS
# print("DFS traversal:")
# dfs(min_heap)