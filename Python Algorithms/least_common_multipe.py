def lcm(a, b):
    """
    Returns the Lowest Common Multiple (LCM) of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The LCM of the two numbers.
    """
    return (a * b // gcd(a, b))


def gcd(a, b):
    """
    Returns the Greatest Common Divisor (GCD) of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of the two numbers.
    """
    while b:
        a, b = b, a % b
    return a

# Driver code
num1 = 12
num2 = 18
lcm_result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm_result}.")

