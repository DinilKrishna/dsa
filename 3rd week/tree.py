class Tree:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


root = Tree(4)
root.left = Tree(3)
root.right = Tree(5)
root.left.left = Tree(2)
root.left.left.left = Tree(1)
root.left.left.right = Tree(2)
root.right.right = Tree(6)

def inorder_traversal(root):
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.data)
        result += inorder_traversal(root.right)
    return result

tree = inorder_traversal(root)
print(tree)

def height(root):
    if root is None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)

h1 = height(root)
h2 = height(root.left.left)
# print(h1, h2)


def is_balanced(root):
    if root is None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    return False

# print(is_balanced(root))

def preorder_traversal(root):
    result = []
    if root:
        result.append(root.data)
        result += preorder_traversal(root.left)
        result += preorder_traversal(root.right)
    return result

print(preorder_traversal(root))

def postorder_traversal(root):
    result = []
    if root:
        result += postorder_traversal(root.left)
        result += postorder_traversal(root.right)
        result.append(root.data)
    return result

print(postorder_traversal(root))

def bfs(root):
    if root is None:
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

bfs(root)

def dfs(root):
    if root is None:
        return

    stack = [root]
    while stack:
        current = stack.pop()
        print(current, end=" ")

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

dfs(root)