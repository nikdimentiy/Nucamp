def linear_search_dictionary(dict, target):
    """
    Linear search for a target value in a dictionary.

    Parameters:
    - dict (dict): The dictionary to search through.
    - target: The value to search for in the dictionary.

    Returns:
    - The key associated with the target value if found, otherwise None.

    Comments:
    - This function iterates through each key in the dictionary.
    - It checks if the value associated with the current key matches the target value.
    - If a match is found, it prints the key where the match occurred and returns the key.
    - If no match is found after iterating through all keys, it prints a message indicating that the target is not in the dictionary.
    """

    # Iterate through each key in the dictionary
    for key in dict:
        # Check if the value associated with the current key matches the target value
        if dict[key] == target:
            # If a match is found, print the key where the match occurred and return the key
            print("Found at key", key)
            return key
    # If no match is found after iterating through all keys, print a message indicating that the target is not in the dictionary
    print("Target is not in the dictionary")


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}

# Test cases
linear_search_dictionary(my_dictionary, 5)  # Should print: Found at key red
linear_search_dictionary(my_dictionary, 3)  # Should print: Found at key blue
linear_search_dictionary(my_dictionary, 8)  # Should print: Target is not in the dictionary
