class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    current = root
    while current:
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
                return root  
            current = current.left
        else:
            if current.right is None:
                current.right = Node(key)
                return root  
            current = current.right
    
def inorder_sort(root, arr):
    if root is not None:
        inorder_sort(root.left, arr)
        arr.append(root.key)
        inorder_sort(root.right, arr)

def sort(root):
    arr = []
    inorder_sort(root, arr)
    return arr

root = None

keys = [9,6,8,4,3,1,5,0,2,7]

for key in keys:
    root = insert(root, key)

sorted_arr = sort(root)
print(sorted_arr)
