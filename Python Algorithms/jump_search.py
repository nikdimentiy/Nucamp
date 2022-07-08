import math
# Jump Search - time complexity: O(n^1/2)


def jump_search(arr, element):
    n = len(arr)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while arr[min(step, n) - 1] < element:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1

    while arr[prev] < element:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if arr[prev] == element:
        return prev
    return -1
