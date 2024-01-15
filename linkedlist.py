class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.ref:
                current = current.ref
            current.ref = new_node


    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node




def merge_lists(l1, l2):
    merged = LinkedList()
    cur1 = l1.head
    cur2 = l2.head
    while cur1 is not None and cur2 is not None:
        if cur1.data < cur2.data:
            merged.add_at_end(cur1.data)
            cur1 = cur1.ref
        else:
            merged.add_at_end(cur2.data)
            cur2 = cur2.ref
    while cur1 is not None:
        merged.add_at_end(cur1.data)
        cur1 = cur1.ref
    while cur2 is not None:
        merged.add_at_end(cur2.data)
        cur2 = cur2.ref
    return merged

LL1 = LinkedList()
LL1.add_at_end(10)
LL1.add_at_end(20)
LL1.add_at_end(30)
# LL1.print_LL()
LL2 = LinkedList()
LL2.add_at_end(15)
LL2.add_at_end(28)
LL2.add_at_end(29)


merged_list = merge_lists(LL1, LL2)
merged_list.print_LL()



#############################################################

# lst =[1,2,3]
# lst.append(1)
# lst.append(2)
# lst.append(3)
# lst.append(4)
# a = input("Enter a number to be added")
# lst.append(a)
# print(lst[3])

#############################################################

# from array import array

# # # Initialize an array of integers with a fixed size of 10
# my_array = array('i', [0] * 10)

# # # Set values in the array
# my_array[0] = 10
# my_array[1] = 20
# my_array[2] = 30
# my_array[3] = 40
# my_array[4] = 50
# my_array[5] = 60
# my_array[6] = 70
# my_array[7] = 80
# my_array[8] = 90
# my_array[9] = 100
# # my_array[10] = 110
# a = int(input("Enter a number to be added"))
# my_array.append(a)

# print(my_array)

# print(my_array)

#############################################################

# arr = [1,2,3,4,5,6,7,8,2,9]

# a = int(input("Enter the number to be searched: "))
# for i in range(len(arr)):
#     if arr[i] == a:
#         print(f"The element occur at the index:{i} ")
        


#############################################################