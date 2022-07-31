def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr.pop()
    greater: list[int] = []
    lesser: list[int] = []
    for element in arr:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
