def is_palindrome(num):
    num = str(num)
    return num == num[::-1]


def palindrome_prime(num):
    """Returns the prime numbers less than or equal to the given number which are palindromes.
    Plaindromes are numbers/strings that are the same when read from left to right and right to left.
    >>> palindrome_prime(10)
    [2, 3, 5, 7]
    >>> palindrome_prime(20)
    [2, 3, 5, 7, 11]
    """
    prime = [True] * (num + 1)
    p = 2
    while (p ** 2 <= num):
        if prime[p]:
            for i in range(p * 2, num + 1, p):
                prime[i] = False
        p += 1

    arr = []
    for p in range(2, num + 1):
        if (prime[p] and is_palindrome(p)):
            arr.append(p)
    return arr
