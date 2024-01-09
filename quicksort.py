
import random


def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort(left) + [pivot] + quicksort(right)




def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while right >= left and arr[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

arr = [1, 34, 6, 8, 8, 23, 5, 89, 4, 2, 6]
quick_sort(arr, 0, len(arr) - 1)
print(arr)