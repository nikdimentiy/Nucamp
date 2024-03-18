def linear_search(the_list, target):
    """
    Perform linear search to find the index of the target element in the list.

    Parameters:
    the_list (list): The list to search through.
    target: The element to search for in the list.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """

    # Iterate through the list
    for x in range(len(the_list)):
        # Check if the current element matches the target
        if the_list[x] == target:
            print("Found at index", x)  # Print the index where the target is found
            return x  # Return the index of the target
    print("Target is not in the list")  # If target not found, print a message
    return -1  # Return -1 to indicate target not found

# Test the function with a list and different targets
my_list = [6, 3, 4, 2, 7, 5, 3, 1]
linear_search(my_list, 5)  # Searching for 5
linear_search(my_list, 1)  # Searching for 1
linear_search(my_list, 8)  # Searching for 8
