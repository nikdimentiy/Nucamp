# convert binary numbers to decimal numbers
def binary_to_decimal(binary_number):
    decimal_number = 0
    power = 0
    for i in range(len(binary_number) - 1, -1, -1):
        decimal_number += int(binary_number[i]) * (2 ** power)
        power += 1
    return decimal_number


# Alternative method - built-in function
# int(binary_number, 2)
