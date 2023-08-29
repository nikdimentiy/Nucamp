def median(arr):
    """Returns the median of a list of numbers

    Parameters:
    arr (list): A list of numbers

    Returns:
    float: The median of the list
    """

    # Sort the list in ascending order
    arr.sort()

    # Check if the list has an even number of elements
    if len(arr) % 2 == 0:
        # If yes, then the median is the average of the middle two elements
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        # If no, then the median is the middle element
        return arr[len(arr) // 2]

# Driver code to test the function
# Create a list of numbers
numbers = [5, 3, 7, 9, 1]

# Print the median of the list
print(median(numbers))

