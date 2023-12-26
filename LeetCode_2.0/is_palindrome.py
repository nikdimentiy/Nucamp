# Coding interview practice: LeetCode problem -> Palindrome Number (https://leetcode.com/problems/palindrome-number/)


def is_palindrome(x):
    """
    Check if an integer is a palindrome.

    Parameters:
    - x (int): The integer to be checked for palindrome property.

    Returns:
    bool: True if the integer is a palindrome, False otherwise.

    Note:
    - Negative numbers and numbers ending with 0 are not palindromes.

    Examples:
    >>> is_palindrome(121)
    True
    >>> is_palindrome(-121)
    False
    >>> is_palindrome(10)
    False
    """
    # Special cases: Negative numbers and numbers ending with 0 are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_number = 0
    original_number = x

    while x > 0:
        # Pop the last digit and add it to the reversed number
        last_digit = x % 10
        reversed_number = reversed_number * 10 + last_digit

        # Remove the last digit from the original number
        x //= 10

    # Check if the reversed number is equal to the original number
    return reversed_number == original_number


# Example usage:
input_number = 121
output = is_palindrome(input_number)
print(output)
