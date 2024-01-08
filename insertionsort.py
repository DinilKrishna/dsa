
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            

arr = [3,63,1,6,24,6,7]

insertion_sort(arr)

print(arr)
