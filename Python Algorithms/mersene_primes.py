def is_prime(num: int):
    i = 2
    while i ** 2 <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def mersenne_prime(num):
    """Returns mersenne prime number less than or equal to the given number.
    mersenne primes are prime numbers of the form 2^n - 1.
    >>> mersene_prime(10)
    [3, 7]
    >>> mersene_prime(100)
    [3, 7, 31]
    """
    arr = []
    power = 1
    value = 2 ** power - 1
    while value < num:
        if is_prime(value):
            arr.append(value)
        power += 1
        value = 2 ** power - 1
    return arr
