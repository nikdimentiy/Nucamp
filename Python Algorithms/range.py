def range(arr):
    """Returns the range of a list of numbers"""
    arr.sort()
    return arr[-1] - arr[0]
