
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key


def insertion_sort_desc(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key > a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key


def insertion_sort_len(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and len(key) < len(a[j]):
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key        

arr = [3,63,1,6,24,6,7]
names = ["dinil" , "saju", "arun", "anyanya", "rahul", "ashish"]

insertion_sort(arr)
print('sorted array: ',arr)
insertion_sort_desc(arr)
print('desc sorted array: ',arr)
insertion_sort_len(names)
print('len sorted array: ',names)
