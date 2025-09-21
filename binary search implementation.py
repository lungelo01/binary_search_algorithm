# A binary search algorithm on a sorted array
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    # A while loop matches the target with the index
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 3

# Calls the function
index = binary_search(arr, target)

if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")

