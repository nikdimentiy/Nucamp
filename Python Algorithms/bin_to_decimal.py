def binary_to_decimal(binary_number):
    """
    Convert a binary number to a decimal number.

    Args:
    binary_number (str): A string representing a binary number.

    Returns:
    int: The decimal representation of the binary number.

    Example:
    >>> binary_to_decimal("1101")
    13
    >>> binary_to_decimal("1010")
    10
    """
    decimal_number = 0  # Initialize the decimal number
    power = 0  # Initialize the power variable for position calculation

    # Iterate through the binary number from right to left
    for i in range(len(binary_number) - 1, -1, -1):
        # Convert the binary digit to an integer and multiply by 2 raised to the power
        decimal_number += int(binary_number[i]) * (2 ** power)
        power += 1  # Increment the power for the next position

    return decimal_number

# Driver code to test the function
if __name__ == "__main__":
    binary_num1 = "1101"
    decimal_num1 = binary_to_decimal(binary_num1)
    print(f"Binary: {binary_num1} -> Decimal: {decimal_num1}")

    binary_num2 = "1010"
    decimal_num2 = binary_to_decimal(binary_num2)
    print(f"Binary: {binary_num2} -> Decimal: {decimal_num2}")
