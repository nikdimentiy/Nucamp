def siftdown(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


def heapsort(arr):
    # in pseudo-code, heapify only called once, so inline it here
    for start in range((len(arr)-2)/2, -1, -1):
        siftdown(arr, start, len(arr)-1)

    for end in range(len(arr)-1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        siftdown(arr, 0, end - 1)
    return arr
