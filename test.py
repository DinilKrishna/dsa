class Node:
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None
    
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)
    
root = None
arr = [4,2,7,8,2,5,8,3,5,1,0,9,6]

for key in arr:
    root = print(insert(root, key))

# a = search(4, 9)
# print(a)
