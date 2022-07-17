def second_largest(numbers):
    """Find the second largest number in a list of numbers."""
    largest = None
    second_largest = None
    for number in numbers:
        if largest is None or number > largest:
            second_largest, largest = largest, number
        elif second_largest is None or number > second_largest:
            second_largest = number
    return second_largest
