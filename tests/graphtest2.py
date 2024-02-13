# 1. Implement a graph using an adjacency matrix and an adjacency list.
# 2. Perform a depth-first search (DFS) on a graph.
# 3. Perform a breadth-first search (BFS) on a graph.
# 4. Check if a graph is cyclic.
# 5. Find the shortest path in an unweighted graph.
# 6. Implement Dijkstra's algorithm for finding the shortest path in a weighted graph.

from collections import defaultdict

class GraphAdjMatrix:
    def __init__(self, num_vertices):
        self.num_of_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for i in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
    
    def display(self):
        for row in self.adj_matrix:
            print(row)

# g = GraphAdjMatrix(5)
# g.add_edge(0, 1)
# g.add_edge(0, 4)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(2, 3)
# g.add_edge(3, 4)

# print("Adjacency Matrix:")
# g.display()


class GraphAdjList:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display(self):
        for vertex, neighbours in self.adj_list.items():
            print(f"{vertex} : {neighbours}")

    def dfs(self, v):
        if v in self.graph:
            visited = set()
            stack = [v]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.append(current)
                    print(current, end = " ")
                for i in self.graph[current]:
                    stack.append(i)
        else:
            print("Vertex not found")

    def bfs(self, v):
        if v in self.graph:
            visited = set()
            queue = [v]
            while queue:
                current = queue.pop(0)
                if current not in visited:
                    visited.append(current)
                    print(current, end = " ")
                for i in self.graph[current]:
                    queue.append(i)
        else:
            print("Vertex not found")



g = GraphAdjList()
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Adjacency List:")
g.display()

def is_cyclic(graph):
    visited = set()
    def dfs_cyclic(node, parent):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfs_cyclic(neighbour, node):
                    return True
                elif parent != neighbour:
                    return True
            return False
    
    for node in graph:
        if node not in visited:
            if dfs_cyclic(node, None):
                return True
        return False
    
def shortest(graph):
    visited = set()
    queue = []
    

