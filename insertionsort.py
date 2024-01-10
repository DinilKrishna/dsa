
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]


def insertion_sort_desc(a):
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] > a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]


def insertion_sort_len(a):
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if len(a[j]) < len(a[j-1]):
                a[j], a[j-1] = a[j-1], a[j]                

arr = [3,63,1,6,24,6,7]
names = ["dinil" , "saju", "arun", "anyanya", "rahul", "ashish"]

insertion_sort(arr)
print('sorted array: ',arr)
insertion_sort_desc(arr)
print('desc sorted array: ',arr)
insertion_sort_len(names)
print('len sorted array: ',names)
