def second_smallest(numbers):
    """Find the second smallest number in a list of numbers"""
    smallest = None
    second_smallest = None
    for number in numbers:
        if smallest is None or number < smallest:
            second_smallest, smallest = smallest, number
        elif second_smallest is None or number < second_smallest:
            second_smallest = number
    return second_smallest
