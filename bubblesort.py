
def bubble_sort(a):
    n = len(a)
    for i in range (n):
        for j in range (n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


def bubble_sort_desc(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def bubble_sort_len(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if len(a[j]) > len(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]



a = [1,4,6,3,8,4,7,9,3]

bubble_sort(a)
print(a)

b = [6.2345, 2.2546, 2.2545, 34.34536, 73.34534, 1.3633, 3.353563]

bubble_sort_desc(b)
print(b)

c = ["dinil" , "saju", "arun", "anyanya", "rahul", "ashish"]

bubble_sort_len(c)
print(c)