"""
This program prints a pattern of asterisks in a specific shape.
"""

def print_pattern():
    """
    Prints a pattern of asterisks in a specific shape.
    """
    for x in range(0, 6):
        if x == 0 or x == 5:
            print("*")  # Prints a single asterisk for the first and last lines
        elif x == 1 or x == 4:
            print("**")  # Prints two asterisks for the second and second-to-last lines
        elif x == 2 or x == 3:
            print("***")  # Prints three asterisks for the third and third-to-last lines
        else:
            print("****")  # Prints four asterisks for the middle line

# Call the function to print the pattern
print_pattern()
