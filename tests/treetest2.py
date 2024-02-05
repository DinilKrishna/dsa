# 1. Implement a binary tree and write a function to perform an in-order traversal.
# 2. Given a binary tree, write a function to calculate its height.
# 3. Check if a binary tree is balanced.
# 4. Find the lowest common ancestor in a binary tree.
# 5. Serialize and deserialize a binary tree.
# 6. Convert a binary search tree to a sorted doubly linked list.

# 1:
class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
def build_bst(arr):
    if not arr:
        return None
    
    root = SearchTree(arr[0])
    for i in arr[1:]:
        insert(root, i)
    
    return root

def insert(root, key):
    if key < root.key:
        if root.left is None:
            root.left = SearchTree(key)
        else:
            insert(root.left, key)
    else:
        if root.right is None:
            root.right = SearchTree(key)
        else:
            insert(root.right, key)

def inorder_traversal(root):
    if root:
        if root.left:
            inorder_traversal(root.left)
        print(root.key, end = " ")
        if root.right:
            inorder_traversal(root.right)



arr = [4,8,2,3,9,0,1,7,5,6]
root = build_bst(arr)
inorder_traversal(root)
print()

def height_of_tree(root):
    if root is None:
        return -1
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    
    return max(left_height, right_height) + 1

print("Height of tree: ",height_of_tree(root))

def is_balanced(root):
    if is_balanced_fn(root) == -1:
        return False
    else:
        return True


def is_balanced_fn(root):
    if root is None:
        return True
    left_height = is_balanced_fn(root.left)
    right_height = is_balanced_fn(root.right)

    if left_height == -1 or right_height == -1:
        return -1
    
    if abs(left_height - right_height) > 1:
        return -1
    
    return max(left_height, right_height) + 1
    

print(is_balanced(root))

arr1 = [2,1,3]
root1 = build_bst(arr1)
print(is_balanced(root1))

def common_anc(root, x, y):
    if root is None or root == x or root == y:
        return root
    left_lca = common_anc(root.left, x, y)
    right_lca = common_anc(root.right, x, y)
    if left_lca is not None and right_lca is not None:
        return root
    return left_lca if left_lca is not None else right_lca




class DLL_Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DLL_Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_after_node(self, node, data):
        current = self.head
        while current:
            if current.data == node:
                break
            current = current.next
        if not current:
            print("Node not found")
            return
        new_node = DLL_Node(data)
        new_node.prev = current
        new_node.next = current.next
        current.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
            
        
def sort_bst(root):
    if root is None:
        return
    arr = []
    inorder_sort(root, arr)
    return arr

def inorder_sort(root, arr):
    if root:
        inorder_sort(root.left, arr)
        arr.append(root.key)
        inorder_sort(root.right, arr)

sorted_bst = sort_bst(root)
print("Sorted BST: ",sorted_bst)

dll = DLL()

for data in sorted_bst:
    dll.insert(data)

current = dll.head
while current:
    print(current.data, end= " ")
    current = current.next