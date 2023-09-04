def get_list_length(my_list):
    """
    Recursively calculate the length of a list.

    Arguments:
    my_list -- the list for which to calculate the length

    Returns:
    The length of the list.
    """

    if my_list == []:  # Base case: empty list
        return 0

    # Recursive case: add 1 to the length of the list starting from the second element
    return 1 + get_list_length(my_list[1:])


# Driver code to test the get_list_length function
my_user_list = [3, 5, 9, 7, 8, 5, 7]

# Call the get_list_length function
length = get_list_length(my_user_list)

# Print the length of the list
print(f"The length of the list is: {length}.")
