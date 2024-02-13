class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex in self.graph:
            print("Vertex already exists")
        else:
            self.graph[vertex] = []
    
    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            print("Vertex not found")
        elif v2 not in self.graph:
            print("Vertex not found")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def add_edge_with_cost(self, v1, v2, cost):
        if v1 not in self.graph:
            print("Vertex not found")
        elif v2 not in self.graph:
            print("Vertex not found")
        else:
            list1 = [v1, cost]
            list2 = [v2, cost]
            self.graph[v1].append(list2)
            self.graph[v2].append(list1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            self.graph.pop(vertex)
            for i in self.graph:
                list1 = self.graph[i]
                if vertex in list1:
                    list1.remove(vertex)
        else:
            print("Vertex not found")

    def remove_edge(self, v1, v2):
        if v1 not in self.graph:
            print("Vertex not found")
        elif v2 not in self.graph:
            print("Vertex not found")
        else:
            if v2 in self.graph[v1]:
                self.graph.remove(v2)
            if v1 in self.graph[v2]:
                self.graph.remove(v1)

    def bfs(self, v):
        visited = set()
        queue = [v]
        while queue:
            current = queue.pop(0)
            if current not in visited:
                print(current, end = " ")
                visited.add(current)
                for i in self.graph[current]:
                    queue.append(i)

    def dfs(self, v):
        visited = set()
        stack = [v]
        while stack:
            current = stack.pop()
            if not current in visited:
                print(current, end = " ")
                visited.add(current)
                for i in self.graph[current]:
                    stack.append(i)

    def print_graph(self):
        for key, value in self.graph.items():
            print(f'{key}: {value}')

    def node_count(self):
        count = 0
        for key in self.graph.keys():
            count += 1
        return count


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
# g.add_edge_with_cost('A', 'B', 10)
g.add_edge('A', 'D')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('D', 'C')
g.add_edge('D', 'E')
g.print_graph()
print("BFS : ")
g.bfs('A')
print()
print("DFS : ")
g.dfs('A')
print()
print("Node Count: ",g.node_count())




