def factors(x):
    """
    Find the factors of a given number.

    Args:
        x (int): The number for which to find factors.

    Returns:
        list: A list of factors of the input number.
    """
    factors = []
    i = 2
    s = int(x ** 0.5)
    while i <= s:  # Include the case where i is the square root of x.
        if x % i == 0:
            factors.append(i)
            x = int(x / i)
            s = int(x ** 0.5)
        else:
            i += 1
    factors.append(x)
    return factors

print("First 10 Fermat numbers:")
for i in range(10):
    fermat = 2 ** (2 ** i) + 1
    print(f"F{chr(0x2080 + i)} = {fermat}")

print("\nFactors of the first few Fermat numbers:")
for i in range(10):
    fermat = 2 ** (2 ** i) + 1
    fac = factors(fermat)
    if len(fac) == 1:
        print(f"F{chr(0x2080 + i)} -> IS PRIME")
    else:
        print(f"F{chr(0x2080 + i)} -> FACTORS: {fac}")
