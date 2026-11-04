def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
result = binary_search(numbers, target)
print("Index of target:", result)
