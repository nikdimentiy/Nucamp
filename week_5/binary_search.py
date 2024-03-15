def binary_search(the_list, target):
    """
    Perform binary search on a sorted list to find the index of the target element.

    Parameters:
        the_list (list): A sorted list of elements to be searched.
        target (int): The element to search for within the list.

    Returns:
        int: The index of the target element in the list if found, otherwise -1.
    """

    # Initialize lower and upper bounds for the search range
    lower_bound = 0
    upper_bound = len(the_list) - 1  # Subtract 1 because index starts from 0

    # Loop until the lower bound is less than or equal to the upper bound
    while lower_bound <= upper_bound:
        # Calculate the midpoint (pivot) of the current range
        pivot = (lower_bound + upper_bound) // 2
        # Get the value of the element at the pivot position
        pivot_value = the_list[pivot]

        # Check if the pivot value is equal to the target
        if pivot_value == target:
            return pivot  # Return the index of the target element

        # If pivot value is greater than the target, adjust the upper bound
        if pivot_value > target:
            upper_bound = pivot - 1
        # If pivot value is less than the target, adjust the lower bound
        else:
            lower_bound = pivot + 1

    # If the target is not found, return -1
    return -1


# Example usage
the_list = [3, 12]  # Sorted list
print(binary_search(the_list, 3))  # Output: 0 (index of 3 in the list)
