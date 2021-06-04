# Iterative Binary Search Function
# Time complexity: O(logN)
# It returns index of x in given array arr if present, else returns -1
def binary_search(arr, x):
    low = 0  # low point
    high = len(arr) - 1  # high point

    while low <= high:

        mid = (high + low) // 2 # mid point

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return None


"""
# Test your own array
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))
x = int(input())

# Function call
result = binary_search(arr, x)

if result is not None:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
"""
