def bead_sort(arr):
    """
    Sorts a list of non-negative integers using the Bead Sort algorithm.

    Parameters:
        arr (list): A list of non-negative integers to be sorted.

    Returns:
        list: A sorted list in ascending order.

    Raises:
        TypeError: If the input is not a list of non-negative integers.

    Bead Sort works by using beads (represented as positive integers) on rods.
    The largest values move to the bottom of the rods, simulating a sorting process.

    Example:
        >>> bead_sort([5, 2, 9, 1, 5])
        [1, 2, 5, 5, 9]
    """

    # Check if the input is valid
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise TypeError("Sequence must be a list of non-negative integers")

    # Bead Sort algorithm
    for _ in range(len(arr)):
        for i, (rod_upper, rod_lower) in enumerate(zip(arr, arr[1:])):
            if rod_upper > rod_lower:
                arr[i] -= rod_upper - rod_lower
                arr[i + 1] += rod_upper - rod_lower

    return arr

# Driver code
if __name__ == "__main__":
    input_list = [5, 2, 9, 1, 5]
    sorted_list = bead_sort(input_list)
    print("Input List:", input_list)
    print("Sorted List:", sorted_list)

