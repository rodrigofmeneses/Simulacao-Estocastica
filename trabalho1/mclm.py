def lcg(modulus, a, c, seed):
    """Linear congruential generator."""
    i = 0
    while i < 11:
        seed = (a * seed + c) % modulus
        yield seed
        i += 1

rd = lcg(100, 19, 0, 63)

for i in rd:
    print(i)