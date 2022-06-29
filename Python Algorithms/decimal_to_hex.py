# convert decimal numbers to hexadecimal numbers
def decimal_to_hexadecimal(decimal_number):
    hexadecimal_number = ''
    hexadecimal_number_list = ['0', '1', '2', '3', '4',
                               '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while decimal_number > 0:
        hexadecimal_number = hexadecimal_number_list[decimal_number %
                                                     16] + hexadecimal_number
        decimal_number = decimal_number // 16
    return hexadecimal_number



result = decimal_to_hexadecimal(255)
print(result)
