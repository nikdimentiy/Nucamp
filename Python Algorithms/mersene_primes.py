def is_prime(num: int):
    """
    Check if a given number is prime.
    
    Args:
    num (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    i = 2
    while i ** 2 <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def mersenne_prime(num):
    """
    Generate a list of Mersenne prime numbers less than or equal to the given number.
    
    Mersenne primes are prime numbers of the form 2^n - 1.
    
    Args:
    num (int): The upper limit for generating Mersenne prime numbers.
    
    Returns:
    list: A list of Mersenne prime numbers.
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

# Driver code
if __name__ == "__main__":
    limit = int(input("Enter a limit: "))
    mersenne_primes = mersenne_prime(limit)
    print("Mersenne prime numbers less than or equal to", limit, ":", mersenne_primes)
