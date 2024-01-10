# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_LL(self):
#         if self.head is None:
#             print("Linked List is empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node


# LL1 = LinkedList()
# # LL1.add_begin(10)
# # LL1.add_begin(20)
# # LL1.add_begin(30)
# LL1.print_LL()

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