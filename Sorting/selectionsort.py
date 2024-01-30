
def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if a[min_index] > a[j]:
                min_index = j
                
        a[min_index] , a[i] = a[i], a[min_index]

def selection_sort_desc(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if a[min_index] < a[j]:
                min_index = j
                
        a[min_index] , a[i] = a[i], a[min_index]

def selection_sort_len(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if len(a[min_index]) > len(a[j]):
                min_index = j
                
        a[min_index] , a[i] = a[i], a[min_index]


arr = [1,5,6,4,2,3,57,5,2]
names = ["dinil" , "saju", "arun", "anyanya", "rahul", "ashish"]

selection_sort(arr)
print(arr)
selection_sort_desc(arr)
print(arr)
selection_sort_len(names)
print(names)