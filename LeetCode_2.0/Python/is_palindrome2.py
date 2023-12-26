# Coding interview practice: LeetCode problem -> Palindrome Number (https://leetcode.com/problems/palindrome-number/)


def isPalindrome(x):
    """
    Check if an integer is a palindrome.

    Args:
        x (int): The integer to check.

    Returns:
        bool: True if the integer is a palindrome, False otherwise.
    """
    # Convert the integer to a string
    str_x = str(x)

    # Reverse the string
    reversed_str_x = str_x[::-1]

    # Compare the original string with the reversed string
    if str_x == reversed_str_x:
        return True
    else:
        return False


# Driver code
x = 121
print(isPalindrome(x))  # True
x = -121
print(isPalindrome(x))  # False
x = 10
print(isPalindrome(x))  # False
x = -101
print(isPalindrome(x))  # False
x = 0
print(isPalindrome(x))  # True
