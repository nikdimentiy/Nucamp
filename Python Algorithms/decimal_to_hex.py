def decimal_to_hexadecimal(decimal_number):
    """
    Convert a decimal number to a hexadecimal number.

    Args:
        decimal_number (int): The decimal number to be converted.

    Returns:
        str: The hexadecimal representation of the decimal number.
    """
    hexadecimal_number = ''  # Initialize an empty string to store the hexadecimal representation.

    # Define a list of hexadecimal digits.
    hexadecimal_number_list = ['0', '1', '2', '3', '4',
                               '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    # Perform the conversion using repeated division by 16.
    while decimal_number > 0:
        # Append the remainder (hexadecimal digit) to the left of the current hexadecimal representation.
        hexadecimal_number = hexadecimal_number_list[decimal_number % 16] + hexadecimal_number
        decimal_number = decimal_number // 16  # Perform integer division by 16.

    return hexadecimal_number

# Driver code to test the function
if __name__ == "__main__":
    decimal_input = 255
    hexadecimal_result = decimal_to_hexadecimal(decimal_input)
    print(f"The hexadecimal representation of {decimal_input} is: {hexadecimal_result}")
