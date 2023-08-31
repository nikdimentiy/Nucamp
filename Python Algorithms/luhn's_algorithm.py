def luhns_algorithm(credit_card_number):
    """
    Checks if a credit card number is valid using the Luhn's algorithm.

    The Luhn's algorithm is used to validate a variety of identification numbers,
    particularly credit card numbers.

    Args:
        credit_card_number (int or str): The credit card number to be validated.

    Returns:
        bool: True if the credit card number is valid, False otherwise.
    """
    # Convert the credit card number to a list of integers
    credit_card_number_list = [int(x) for x in str(credit_card_number)]
    
    # Reverse the list to start from the rightmost digit
    credit_card_number_list.reverse()
    
    # Initialize the total
    total = 0
    
    for i in range(len(credit_card_number_list)):
        # Process every other element
        if i % 2 == 0:
            # Double the value
            credit_card_number_list[i] = credit_card_number_list[i] * 2
        # If the doubled value is greater than 9, subtract 9
        if credit_card_number_list[i] > 9:
            credit_card_number_list[i] = credit_card_number_list[i] - 9
        # Add to the total
        total = total + credit_card_number_list[i]
    
    # If the total is a multiple of 10, the number is valid
    return total % 10 == 0

# Driver code for testing
if __name__ == "__main__":
    test_credit_cards = [
        "4111111111111111",  # Valid Visa card
        "4111111111111",     # Invalid Visa card (too short)
        "4012888888881881",  # Valid Visa card
        "378282246310005",   # Valid American Express card
        "6011111111111117",  # Valid Discover card
        "5105105105105100",  # Valid Mastercard
        "5105105105105106",  # Invalid Mastercard (checksum error)
    ]
    
    for card_number in test_credit_cards:
        is_valid = luhns_algorithm(card_number)
        print(f"Credit Card: {card_number}, Valid: {is_valid}")
