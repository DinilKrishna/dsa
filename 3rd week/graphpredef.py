from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)  # Assuming an undirected graph

    def remove_edge(self, source, destination):
        self.graph[source].remove(destination)
        self.graph[destination].remove(source)

    def remove_vertex(self, vertex):
        del self.graph[vertex]
        for key in self.graph:
            if vertex in self.graph[key]:
                self.graph[key].remove(vertex)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            current = queue.popleft()
            if current not in visited:
                print(current, end=" ")
                visited.add(current)
                queue.extend(neighbor for neighbor in self.graph[current] if neighbor not in visited)

    def dfs(self, start):
        visited = set()

        def dfs_recursive(node):
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph[node]:
                    dfs_recursive(neighbor)

        dfs_recursive(start)

    def is_valid(self):
        # Check if the graph has self-loops or parallel edges
        for vertex in self.graph:
            if vertex in self.graph[vertex] or len(self.graph[vertex]) != len(set(self.graph[vertex])):
                return False
        return True

# Example usage:
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "A")

print("Graph:")
print(g.graph)

print("\nBFS traversal:")
g.bfs("A")

print("\nDFS traversal:")
g.dfs("A")

print("\nIs a valid graph?")
print(g.is_valid())
