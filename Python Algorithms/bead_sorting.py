def bead_sort(arr):
    """
    Sorts a list of non-negative integers using the Bead Sort algorithm.

    Bead Sort, also known as Gravity Sort, is a non-comparative integer sorting
    algorithm that simulates beads sliding on parallel rods until they settle
    in a sorted position.

    Args:
    arr (list of int): A list of non-negative integers to be sorted.

    Returns:
    list of int: The sorted list in ascending order.

    Raises:
    TypeError: If the input sequence contains non-integer or negative values.

    Example:
    >>> bead_sort([5, 3, 1, 8, 2, 9, 4, 7, 6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise TypeError("Sequence must be a list of non-negative integers")

    # Perform Bead Sort
    for _ in range(len(arr)):
        for i, (rod_upper, rod_lower) in enumerate(zip(arr, arr[1:])):
            if rod_upper > rod_lower:
                arr[i] -= rod_upper - rod_lower
                arr[i + 1] += rod_upper - rod_lower

    return arr

# Driver code to test the function
if __name__ == "__main__":
    arr = [5, 3, 1, 8, 2, 9, 4, 7, 6]
    sorted_arr = bead_sort(arr)
    print("Original Array:", arr)
    print("Sorted Array:", sorted_arr)

