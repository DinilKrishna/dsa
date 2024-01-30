def binary_search(arr, target):
    arr.sort()
    high = len(arr) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

arr = [6, 9, 11, 15, 18, 21, 25]

result = binary_search(arr, 21)
print(f"The index of the element in the sorted array is :{result}")

