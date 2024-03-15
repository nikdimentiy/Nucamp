def bubblesort(the_list):
    """
    Sorts a list using the bubble sort algorithm.

    Parameters:
        the_list (list): The list to be sorted.

    Returns:
        None. The list is sorted in-place.
    """

    high_idx = len(the_list) - 1  # Get the index of the last element

    # Iterate through the list from the beginning to the second last element
    for i in range(high_idx):
        list_changed = False  # Flag to track if any swaps were made in this pass
        # Iterate through the list from the beginning to the second last element
        for j in range(high_idx):
            item = the_list[j]  # Current item
            next = the_list[j+1]  # Next item

            # Compare adjacent elements and swap if necessary
            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True  # Set flag to True if a swap occurred
            print(the_list, i, j)  # Print list and indices for debugging
        print(list_changed)  # Print if any change occurred in this pass
        if not list_changed:  # If no swaps were made in a pass, list is sorted
            break  # Exit the loop as the list is already sorted
