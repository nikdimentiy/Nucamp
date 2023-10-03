from math import sqrt

def arithmetic_mean(arr):
    """
    Calculates the arithmetic mean (average) of a list of numbers.

    Parameters:
        arr (list of numbers): The input list of numbers.

    Returns:
        float: The arithmetic mean of the input list.

    The arithmetic mean is calculated as the sum of all numbers in the list
    divided by the number of elements in the list.

    Example:
        >>> arithmetic_mean([1, 2, 3, 4, 5])
        3.0
    """
    # Check if the input list is empty
    if not arr:
        raise ValueError("Input list is empty")

    # Calculate the sum of squares of all numbers in the list
    sum_of_squares = sum(n * n for n in arr)

    # Calculate the arithmetic mean
    mean = sum_of_squares / len(arr)

    # Return the result after taking the square root
    return sqrt(mean)

# Example usage
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    result = arithmetic_mean(input_list)
    print("Arithmetic Mean:", result)

