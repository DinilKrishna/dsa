def add_node(data):
    if data in graph:
        return
    else:
        graph[data]=[]

def add_edge(v1,v2):
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(node,graph):
    visited=set()
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current,end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

def bfs(node,graph):
    visited=set()
    queue=[]
    queue.append(node)
    while queue:
        current=queue.pop(0)
        if current not in visited:
            print(current,end="")
            visited.add(current)
            for i in graph[current]:
                queue.append(i)

visited=set()
graph={}
add_node(1)
add_node(2)
add_node(3)
add_node(4)
add_node(5)

add_edge(1,2)
add_edge(1,3)
add_edge(3,4)
add_edge(2,4)
add_edge(2,5)
add_edge(4,5)


print(graph)
print()
print(dfs(1,graph))
print(bfs(1,graph))
