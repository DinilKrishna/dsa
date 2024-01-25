from collections import deque


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

def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current

def preorder_traversal(root):
    if root is not None:
        print(root.key, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=" ")

def remove_node(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = remove_node(root.left, key)
    elif key > root.key:
        root.right = remove_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.key = find_min(root.right).key
        root.right = remove_node(root.right, root.key)

    return root

def closest(root, target):
    closest_val = float('inf')
    while root:
        if abs(root.key - target) < abs(closest_val - target):
            closest_val = root.key
        root = root.left if target < root.key else root.right
    return closest_val

def is_valid_binary_tree(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not min_val < root.key < max_val:
        return False
    return (is_valid_binary_tree(root.left, min_val, root.key) and
            is_valid_binary_tree(root.right, root.key, max_val))


def bfs(root):
    if root is None:
        return

    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.key, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def dfs(root):
    if root is None:
        return

    stack = [root]
    while stack:
        current = stack.pop()
        print(current.key, end=" ")

        # Visit left child first, then right child
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)



root = None
keys = [15, 10, 20, 8, 12, 17, 25]

for key in keys:
    root = insert(root, key)

print("\nBFS traversal:")
bfs(root)

print("\nDFS traversal:")
dfs(root)

print("In-order traversal:")
inorder_traversal(root)
print("\nSearch for 12:")
result = search(root, 12)
print(result.key if result else "Not found")

print("\nMinimum value:")
min_node = find_min(root)
print(min_node.key if min_node else "Tree is empty")

print("\nMaximum value:")
max_node = find_max(root)
print(max_node.key if max_node else "Tree is empty")

print("\nPre-order traversal:")
preorder_traversal(root)

print("\nPost-order traversal:")
postorder_traversal(root)

print("\nRemoving node with key 15:")
root = remove_node(root, 15)
inorder_traversal(root)

print("\nClosest value to 13:")
print(closest(root, 13))

print("\nIs a valid binary tree?")
print(is_valid_binary_tree(root))



