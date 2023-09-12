def hexadecimal_to_decimal(hexadecimal_number):
    """
    Convert a hexadecimal number to a decimal number.

    Args:
        hexadecimal_number (str): The hexadecimal number to convert.

    Returns:
        int: The decimal number.
    """

    decimal_number = 0
    hexadecimal_number_list = ['0', '1', '2', '3', '4',
                               '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    power = 0
    for i in range(len(hexadecimal_number) - 1, -1, -1):
        decimal_number += hexadecimal_number_list.index(
            hexadecimal_number[i]) * (16 ** power)
        power += 1
    return decimal_number


hexadecimal_number = "1A"
print(hexadecimal_to_decimal(hexadecimal_number))

