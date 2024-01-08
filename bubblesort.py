
def bubble_sort(a):
    n = len(a)
    for i in range (n):
        for j in range (n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


a = [1,4,6,3,8,4,7,9,3]

bubble_sort(a)
print(a)