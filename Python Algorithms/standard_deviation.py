def standard_deviation(arr, mu=None):
    """Returns the standard deviation of a list of numbers"""
    if not mu:
        mu = mean(arr)
    return sum((x - mu) ** 2 for x in arr) ** 0.5
