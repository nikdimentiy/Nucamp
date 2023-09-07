import math


def quadratic_mean(array):
    """calculate the root mean square of an array."""
    """
    This function calculates the root mean square of an array.

    Args:
        array: A list of numbers.

    Returns:
        The root mean square of the array.
    """

    sum = 0
    length = 0
    for i in range(len(array)):
        # Square each element of the array and add it to the sum.
        sum += array[i] ** 2
        # Increment the length counter.
        length += 1

    # Calculate the mean of the squared elements.
    mean = sum / length

    # Calculate the root mean square.
    rms = math.sqrt(mean)

    return rms


# Driver code
array = [1, 2, 3, 4, 5]
print(quadratic_mean(array))
