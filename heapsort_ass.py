nums=[5,6,8,4,1,9,7,2]

def heapfy(arr,i,n):

    left_child = 2 * i + 1
    right_child = 2 * i + 2
    largest = i
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    if largest != i :
        arr[i],arr[largest] = arr[largest], arr[i]
        heapfy(arr,largest,n)

def sort(arr):
    n= len(arr)
    for i in range(n//2-1,-1,-1):
        heapfy(arr,i,n)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapfy(arr, 0, i)

sort(nums)
print(nums)

