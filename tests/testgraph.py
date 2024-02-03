class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        self.graph[v] = []
    
    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            print("Node not present")
        elif v2 not in self.graph:
            print("Node not present")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def add_edge_with_cost(self, v1, v2, cost):
        if v1 not in self.graph:
            print("Node not present")
        elif v2 not in self.graph:
            print("Node not present")
        else:
            self.graph[v1].append([v2, cost])
            self.graph[v2].append([v1, cost])

    def remove_vertex(self, v):
        if v not in self.graph:
            print("Vertex not found")
            return
        self.graph.pop(v)
        for i in self.graph:
            list1 = self.graph[i]
            if v in list1:
                list1.remove(v)

    def bfs(self, v):
        if v in self.graph:
            queue = [v]
            visited = set()
            while queue:
                current = queue.pop(0)
                if current not in visited:
                    print(current, end = " ")
                    visited.add(current)
                    for i in self.graph[current]:
                        queue.append(i)
        else:
            print("Vertex not found")

    def dfs(self, v):
        if v in self.graph:
            stack = [v]
            visited = set()
            while stack:
                current = stack.pop()
                if current not in visited:
                    print(current, end = " ")
                    visited.add(current)
                    for i in self.graph[current]:
                        stack.append(i)
        else:
            print("Vertex not found")

    def print_graph(self):
        for key, value in self.graph.items():
            print(f'{key}:{value}')


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('A','D')
graph.add_edge('B','D')
graph.add_edge('B','E')
graph.add_edge('C','D')
graph.add_edge('D','E')
graph.print_graph()
graph.bfs('A')
print()
graph.dfs('A')
print()
graph.remove_vertex('D')
graph.print_graph()
