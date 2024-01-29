def add_node(v):
    if v in graph:
        print("already exist")
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print("no data")
    elif v2 not in graph:
        print("no data")
    else:
        graph[v1].append(v2)
        # graph[v2].append(v1)


def delete_node(v):
    
    graph.pop(v)
    for i in graph:
        list1=graph[i]
        if v in list1:
            list1.remove(v)

def DFS(node,visited,graph):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)

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

def BFS(graph,v):
    visited=set()
    queue=[v]
    visited.add(v)
    while queue:
        current=queue.pop()
        print(current, end=" ")
        for i in graph[current]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

    
graph={}
visited=set()
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A","B")
add_edge("A","C")
add_edge("A","D")
add_edge("B","E")
add_edge("B","D")
add_edge("D","C")
print(graph)


print()
dfs("A",graph)
print()
BFS(graph,"A")
