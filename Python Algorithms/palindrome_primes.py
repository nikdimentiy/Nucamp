def is_palindrome(num):
    """
    Checks if the given number is a palindrome.

    A palindrome is a number that reads the same backward as forward.

    Args:
        num: The number to check.

    Returns:
        True if the number is a palindrome, False otherwise.
    """
    num_str = str(num)
    return num_str == num_str[::-1]


def palindrome_prime(num):
    """
    Returns the prime numbers less than or equal to the given number which are palindromes.

    Plaindromes are numbers/strings that are the same when read from left to right and right to left.

    Args:
        num: The upper bound of the range to search.

    Returns:
        A list of prime numbers less than or equal to `num` which are palindromes.
    """

    # Create a list of booleans indicating whether each number is prime.
    prime = [True] * (num + 1)

    # Mark all even numbers as non-prime.
    for i in range(2, num + 1, 2):
        prime[i] = False

    # Start with 2 and iterate over all odd numbers.
    p = 3
    while p <= num:
        # If `p` is prime, mark all its multiples as non-prime.
        if prime[p]:
            for i in range(p * 2, num + 1, p):
                prime[i] = False

        p += 1

    # Create an empty list to store the palindrome primes.
    arr = []

    # Iterate over all numbers from 2 to `num`.
    for p in range(2, num + 1):
        # If `p` is prime and a palindrome, add it to the list.
        if prime[p] and is_palindrome(p):
            arr.append(p)

    return arr


if __name__ == "__main__":
    print(palindrome_prime(10))
    print(palindrome_prime(20))
