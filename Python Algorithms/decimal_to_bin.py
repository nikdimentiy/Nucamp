def decimal_to_binary(decimal_number):
    """
    Convert a decimal number to a binary number.

    Args:
        decimal_number (int): The decimal number to be converted.

    Returns:
        str: The binary representation of the decimal number.
    """
    binary_number = ''  # Initialize an empty string to store the binary representation.
    
    # Perform the conversion using repeated division by 2.
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number  # Append the remainder to the left of the current binary representation.
        decimal_number = decimal_number // 2  # Perform integer division by 2.

    return binary_number

# Driver code to test the function
if __name__ == "__main__":
    decimal_input = 150
    binary_result = decimal_to_binary(decimal_input)
    print(f"The binary representation of {decimal_input} is: {binary_result}")
