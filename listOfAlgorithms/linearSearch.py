# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1


def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return None
