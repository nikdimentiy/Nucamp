def linear_search(arr, element):
    """
    Perform a linear search to find the index of an element in an array.

    Arguments:
    arr -- the array to search in
    element -- the element to search for

    Returns:
    The index of the element if found, -1 otherwise.
    """

    # Iterate through each element of the array
    for i in range(len(arr)):
        # Check if the current element is equal to the target element
        if arr[i] == element:
            # If found, return the index
            return i

    # If the element is not found, return -1
    return -1

# Driver code to test the linear_search function
arr = [5, 2, 9, 1, 7, 3]
element = 7

# Call the linear_search function
index = linear_search(arr, element)

# Check if the element was found
if index != -1:
    print(f"The element {element} is found at index {index}.")
else:
    print(f"The element {element} is not found in the array.")
