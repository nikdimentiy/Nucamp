# convert decimal numbers to binary numbers
def decimal_to_binary(decimal_number):
    binary_number = ''
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number

# Alternative method - built-in function
bin(decimal_number)
