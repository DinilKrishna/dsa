def add_node(v):
    if v in graph:
        print("data alreaady exist")
    else:
        graph[v]=[]

def add_edge(v1,v2,cost):
    if v1 not in graph or v2 not in graph:
        print("no data")
    else:
        lst=[v2,cost]
        graph[v1].append(lst)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",20)
