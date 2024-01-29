def heapify(arr,i,n):

    left_child = 2 * i + 1
    right_child = 2 * i + 2
    smallest = i

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest], arr[i]
        heapify(arr,smallest,n)

def sort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,i,n)
    
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapify(arr,0,i)


nums=[5,6,8,4,1,9,7,2]
sort(nums)
print(nums)
