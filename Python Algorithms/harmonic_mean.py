def harmonic_mean(arr):
    """Returns the harmonic mean of a list of numbers"""
    return len(arr) / sum(1 / x for x in arr)
