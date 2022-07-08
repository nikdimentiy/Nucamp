# Linear Search - time complexity: O(n)
def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1
