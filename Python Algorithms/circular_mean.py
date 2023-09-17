def circular_mean(arr):
    """
    Calculate the circular mean of a list of numbers.

    This function takes a list of angles (in degrees) and calculates their circular mean,
    which considers the circular nature of angles (e.g., 0 degrees and 360 degrees are
    treated as the same angle).

    Parameters:
    arr (list): A list of angles in degrees.

    Returns:
    float: The circular mean of the input angles in degrees.
    """

    # Initialize a variable to store the sum of angles.
    total = 0

    # Loop through the input list of angles.
    for i in arr:
        total += i

    # Since angles are circular, we need to wrap around 360 degrees.
    total %= 360

    # Calculate the circular mean by dividing the total by the number of angles.
    mean = total / len(arr)

    return mean

# Driver code to test the circular_mean function
if __name__ == "__main__":
    angles = [30, 45, 350, 10]
    result = circular_mean(angles)
    print(f"Circular Mean of {angles} degrees: {result:.2f} degrees")
