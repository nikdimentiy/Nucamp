"""
This program returns the range of a list of numbers.

The range of a list is the difference between the largest and smallest elements in the list.

For example, the range of the list [1, 2, 3] is 2 (3 - 1).

Usage:
    python range.py

Example:
    python range.py

Output:
    2
"""


def range(arr):
    """
    Returns the range of a list of numbers.

    Args:
        arr: The list of numbers.

    Returns:
        The range of the list.
    """

    # Sort the list.
    arr.sort()

    # Get the largest and smallest elements in the list.
    largest = arr[-1]
    smallest = arr[0]

    # Return the difference between the largest and smallest elements.
    return largest - smallest


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(range(arr))
