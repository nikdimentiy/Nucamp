def circular_mean(arr):
    """Calculate the circular mean of a list of numbers."""
    total = 0
    for i in arr:
        total += i
    total %= 360
    return total / len(arr)
