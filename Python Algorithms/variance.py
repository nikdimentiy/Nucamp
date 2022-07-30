def variance(arr):
    """Returns the variance of a list of numbers"""
    mean = mean(arr)
    total = 0
    length = 0
    for i in arr:
        total += (i - mean) ** 2
        length += 1
    return total / length
