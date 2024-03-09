def print_star_triangle(rows):
    """
    Prints a triangle made of stars.

    Args:
    - rows (int): The number of rows in the triangle.

    Returns:
    - None
    """
    stars = ""  # Initialize an empty string to hold the stars
    for i in range(1, rows + 1):  # Loop through each row
        for j in range(i):  # Loop to add stars for each row
            stars += "*"  # Add a star to the string
        print(stars)  # Print the stars for the current row
        stars = ""  # Reset the stars string for the next row

# Call the function with the desired number of rows
print_star_triangle(5)
