from math import sqrt


def quadratic_mean(array):
    """calculate the root mean square of an array."""
    sum = 0
    length = 0
    for i in range(len(array)):
        sum += array[i] ** 2
        length += 1
    return sqrt(sum / length)
