def second_smallest(numbers):
    """
    Finds the second smallest number in a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The second smallest number in the list.
    """

    # This function finds the second smallest number in a list of numbers.

    # Initialize the smallest and second smallest numbers.
    smallest = None
    second_smallest = None

    # Iterate over the list of numbers.
    for number in numbers:
        # If the current number is smaller than the smallest number,
        # update the smallest and second smallest numbers.
        if smallest is None or number < smallest:
            second_smallest, smallest = smallest, number
        elif second_smallest is None or number < second_smallest:
            second_smallest = number

    # Return the second smallest number.
    return second_smallest


numbers = [10, 8, 7, 2, 4, 6, 5, 3, 1]

second_smallest_number = second_smallest(numbers)

print("The second smallest number is:", second_smallest_number)
