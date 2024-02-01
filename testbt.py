class Node:
    def __init__(self, key):
        self.key = key
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
    
def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return root.key
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)
    
def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current

def find_max(root):
    current = root
    while current.right:
        current = current.right
    return current

def preorder(root):
    if root:
        print(root.key, end = " ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end = " ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end = " ")

def remove(root, val):
    if root is None:
        return root
    if val < root.key:
        remove(root.left, val)
    elif val > root.key:
        remove(root.right, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.key = find_min(root.right).key
        root.right = remove(root.right, root.key)

def contains(root, target):
    if root is None:
        return False
    elif root.key == target:
        return True
    elif target < root.key:
        contains(root.left, target)
    else:
        contains(root.left, target)

def closest(root, target):
    close = float('inf')
    while root:
        if abs(root.key - target) < abs(close - target):
            close = root.key
        root = root.left if target < root.key else root.right
    return close

def is_valid_binary_tree(root, min_val = float("-inf"), max_val = float("inf")):
    if root is None:
        return True
    if not min_val < root.key < max_val:
        return False
    return (is_valid_binary_tree(root.left, min_val, root.key) and 
            is_valid_binary_tree(root.right, root.key, max_val))
        

def bfs(root):
    if not root:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.key, end = " ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def dfs(root):
    if not root:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.key, end =" ")
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


root = None
keys = [9,6,8,4,3,1,5,0,2,7]

for key in keys:
    root = insert(root, key)

print()    
print(search(root, 8))
print("Minimum: ",find_min(root).key)
print("Maximum: ",find_max(root).key)
print("Preorder: ")
preorder(root)
print()
print("Inorder: ")
inorder(root)
print()
print("Postorder: ")
postorder(root)
print()
print("Whether contains: ",contains(root, 10))
print("Closest: ",closest(root, 4))
print("Is valid bst: ", is_valid_binary_tree(root))
print("BFS:")
bfs(root)
print()
print("DFS:")
dfs(root)
print()
remove(root, 4)
preorder(root)