def luhns_algorithm(credit_card_number):
    """Checks if a credit card number is valid"""
    # convert the credit card number to a list of ints
    credit_card_number_list = [int(x) for x in str(credit_card_number)]
    # reverse the list
    credit_card_number_list.reverse()
    # initialize the total
    total = 0
    for i in range(len(credit_card_number_list)):
        # every other element
        if i % 2 == 0:
            # double the value
            credit_card_number_list[i] = credit_card_number_list[i] * 2
        # add the digits if > 9
        if credit_card_number_list[i] > 9:
            credit_card_number_list[i] = credit_card_number_list[i] - 9
        # add to the total
        total = total + credit_card_number_list[i]
    # if the total is a multiple of 10 the number is valid
    return True if total % 10 == 0 else False
