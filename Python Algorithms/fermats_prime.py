# A prime number of the form (2^2^n) + 1 for some non-negative integer n.
# The first few fermat numbers are 3, 5, 17, 257, 65537, 4294967297, 18446744073709551617

def factors(x):
    factors = []
    i = 2
    s = int(x ** 0.5)
    while i < s:
        if x % i == 0:
            factors.append(i)
            x = int(x / i)
            s = int(x ** 0.5)
        i += 1
    factors.append(x)
    return factors


print("First 10 Fermat numbers:")
for i in range(10):
    fermat = 2 ** 2 ** i + 1
    print(f"F{chr(i + 0x2080)} = {fermat}")

print("\nFactors of first few Fermat numbers:")
for i in range(10):
    fermat = 2 ** 2 ** i + 1
    fac = factors(fermat)
    if len(fac) == 1:
        print(f"F{chr(i + 0x2080)} -> IS PRIME")
    else:
        print(f"F{chr(i + 0x2080)} -> FACTORS: {fac}")
