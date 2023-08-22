def standard_deviation(arr, mu=None):
    """
    Returns the standard deviation of a list of numbers.

    Args:
        arr: A list of numbers.
        mu: The mean of the list. If not provided, the mean will be calculated.

    Returns:
        The standard deviation of the list.

    """

    # Check if the mean was provided. If not, calculate it.

    if not mu:
        mu = mean(arr)

    # Calculate the squared deviations from the mean for each element in the list.

    deviations = [(x - mu) ** 2 for x in arr]

    # Return the square root of the sum of the squared deviations.

    return sum(deviations) ** 0.5


