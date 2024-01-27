class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].discard(vertex2)
            self.vertices[vertex2].discard(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            neighbors = self.vertices[vertex]
            del self.vertices[vertex]
            for v in neighbors:
                self.vertices[v].discard(vertex)

    def dfs(self, start_vertex):
        stack = [start_vertex]
        visited = set()

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex, end=" ")
                visited.add(current_vertex)
                stack.extend(self.vertices[current_vertex] - visited)

    def bfs(self, start_vertex):
        queue = [start_vertex]
        visited = set()

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                print(current_vertex, end=" ")
                visited.add(current_vertex)
                queue.extend(self.vertices[current_vertex] - visited)

    def is_valid_graph(self):
        for vertex in self.vertices:
            for neighbor in self.vertices[vertex]:
                if neighbor not in self.vertices:
                    return False
        return True

# Example usage:
graph = Graph()

# Add vertices
vertices = ["A", "B", "C", "D", "E"]
for vertex in vertices:
    graph.add_vertex(vertex)

# Add edges
edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "E")]
for edge in edges:
    graph.add_edge(edge[0], edge[1])

print("DFS starting from 'A':")
graph.dfs("A")
print("\nBFS starting from 'A':")
graph.bfs("A")

print("\nRemoving edge between 'A' and 'B':")
graph.remove_edge("A", "B")
graph.dfs("A")

print("\nRemoving vertex 'C':")
graph.remove_vertex("C")
graph.dfs("A")

print("\nIs a valid graph?")
print(graph.is_valid_graph())
