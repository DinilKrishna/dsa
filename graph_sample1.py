def add_node(v):
    global node_count
    if v in nodes:
        print("already exist")
    else:
        node_count +=1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print("no node found")
    elif v2 not in nodes:
        print("no node found")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost
        
def delete_node(v):
    global node_count
    if v not in nodes:
        print("no data")
    else:
        index1=nodes.index(v)
        nodes.remove(v)
        node_count -=1
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()
    
node_count = 0
nodes=[]
graph=[]

add_node("A") 
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",20)
delete_node("B")
print_graph()
print(nodes)

