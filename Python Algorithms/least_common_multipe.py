def lcm(a, b):
    """Returns the Lowest Common Multiple (LCM) of 2 numbers."""
    return (a * b // gcd(a, b))


def gcd(a, b):
    """returns the Greatest Common Divisor (GCD) of 2 numbers."""
    while b:
        a, b = b, a % b
    return a
