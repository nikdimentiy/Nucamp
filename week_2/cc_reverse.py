def reverse(name):
    """
    Reverses the given string.

    Args:
    - name (str): The string to be reversed.

    Returns:
    - str: The reversed string.
    """
    # Using slicing with [::-1] to reverse the string
    return name[::-1]

# Ask for user input
name = input("What is your name? ")

# Call the reverse function and print the result
print("Your name reversed is:", reverse(name))
