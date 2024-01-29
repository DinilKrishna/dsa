def add_node(v):
    global node_count
    if v in nodes:
        print("already exist")
    else:
        nodes.append(v)
        node_count+=1
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2):
    if v1 not in nodes:
        print("no data")
    elif v2 not in nodes:
        print("no data")
    else:
        i1=nodes.index(v1)
        i2=nodes.index(v2)
        graph[i1][i2]=1
        graph[i2][i1]=1

def delete_edge(v1,v2):
    if v1 not in nodes:
        print("no data")
    elif v2 not in nodes:
        print("no data")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()

def BFS(start,graph):
    visited=set()
    queue=[start]
    visited.add(start)

    while queue:
        node=queue.pop(0)
        index=nodes.index(node)
        print(node,end=" ")
        for i,j in enumerate(graph[index]):
            if j and nodes[i] not in visited:
                visited.add(nodes[i])
                queue.append(nodes[i])
    print()


   
node_count=0
nodes=[]
graph=[]

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_edge("A","B")
add_edge("B","C")
add_edge("C","D")
add_edge("D","A")

print(nodes)
print_graph()
delete_edge("C","D")
print()
print_graph()
BFS("A",graph)