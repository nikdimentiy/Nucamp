def geometric_mean(arr):
    """Returns the geometric mean of a list of numbers"""
    return reduce(mul, num, 1) ** (1 / len(num))
