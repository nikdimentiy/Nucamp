def median(arr):
    """Returns the median of a list of numbers"""
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        return arr[len(arr) // 2]
