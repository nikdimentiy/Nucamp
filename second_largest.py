def second_largest(numbers):
    """
    Find the second largest number in a list of numbers.

    Parameters:
    - numbers (list): A list of numbers.

    Returns:
    - int or None: The second largest number in the list, or None if the list is empty or contains only one unique number.

    Example:
    >>> second_largest([1, 5, 3, 7, 2])
    5
    >>> second_largest([10, 10, 10, 10])
    None
    >>> second_largest([])
    None
    """

    # Initialize variables to keep track of the largest and second largest numbers
    largest = None
    second_largest = None

    # Iterate through the list of numbers
    for number in numbers:
        # Check if the current number is larger than the current largest number
        if largest is None or number > largest:
            # If true, update the second largest and largest numbers accordingly
            second_largest, largest = largest, number
        # Check if the current number is larger than the current second largest number
        elif second_largest is None or number > second_largest:
            # If true, update the second largest number
            second_largest = number

    # Return the second largest number (or None if the list is empty or contains only one unique number)
    return second_largest

# Driver code for testing
if __name__ == "__main__":
    numbers_list = [1, 5, 3, 7, 2]
    result = second_largest(numbers_list)
    print(f"The second largest number in {numbers_list} is: {result}")
