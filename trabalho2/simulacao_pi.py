def generator_mcl(a, b, m, seed):
    random_number = seed
    while True:
        random_number = (a * random_number + b) % m
        yield random_number / m

rd_gen = generator_mcl(a=7**5, b=0, m=2**31, seed=42)

n = 10000000
nc = 0

for j in range(n):
    x = next(rd_gen)
    y = next(rd_gen)

    if x**2 + y**2 < 1:
        nc += 1

pi = 4 * nc / n

print("O valor de pi é aproximadamente: ", pi)