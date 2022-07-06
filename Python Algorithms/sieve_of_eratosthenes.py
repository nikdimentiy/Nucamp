def sieve_of_eratosthenese(num):
    """Returns a list of prime numbers less than or equal to the given number."""
    sieve = [i for i in range(2, num + 1)]
    key = 0
    while key < len(sieve):
        prime = sieve[key]
        for i in range(prime * prime, num + 1, prime):
            if i in sieve:
                sieve.remove(i)
        key += 1
    return sieve

# The following code is faster than the above array version using only odd composite operations
# (for a factor of over two) and because it has been optimized to use slice operations for
# composite number culling to avoid extra work by the interpreter:


def primes2(limit):
    if limit < 2:
        return []
    if limit < 3:
        return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    # return only odd numbers
    return [2] + [2 * i + 3 for i, v in enumerate(buf) if v]

# This uses a 235 factorial wheel for further reductions in operations
# the same techniques can be applied to the array version as well
# it runs slightly faster and uses slightly less memory as compared to the odds-only algorithms:


def primes235(limit):
    yield 2
    yield 3
    yield 5
    if limit < 7:
        return
    modPrms = [7, 11, 13, 17, 19, 23, 29, 31]
    gaps = [4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 4, 6, 2,
            6]                              # 2 loops for overflow
    ndxs = [0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5,
            5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7]  # 2 loops for overflow
    # integral number of wheels rounded up
    lmtbf = (limit + 23) // 30 * 8 - 1
    lmtsqrt = (int(limit ** 0.5) - 7)
    # round down on the wheel
    lmtsqrt = lmtsqrt // 30 * 8 + ndxs[lmtsqrt % 30]
    buf = [True] * (lmtbf + 1)
    for i in range(lmtsqrt + 1):
        if buf[i]:
            ci = i & 7
            p = 30 * (i >> 3) + modPrms[ci]
            s = p * p - 7
            p8 = p << 3
            for _ in range(8):
                c = s // 30 * 8 + ndxs[s % 30]
                buf[c::p8] = [False] * ((lmtbf - c) // p8 + 1)
                s += p * gaps[ci]
                ci += 1
    # adjust for extras
    for i in range(lmtbf - 6 + (ndxs[(limit - 7) % 30])):
        if buf[i]:
            yield (30 * (i >> 3) + modPrms[i & 7])
