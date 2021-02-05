def mcl(a, b, m, seed, n):
    x = [seed]
    for i in range(n):
        x.append(((a * x[i] + b) % m))
    x.remove(seed)
    return x

# Exemplo 1
print('Exemplo 1')
print(mcl(a=17, b=43, m=100, seed=27, n=10))
# Exemplo 2
print('Exemplo 2')
print('seed = ', 1, mcl(a=13, b=0, m=2**6, seed=1, n=16))
print('seed = ', 2, mcl(a=13, b=0, m=2**6, seed=2, n=8))
print('seed = ', 3, mcl(a=13, b=0, m=2**6, seed=3, n=16))
print('seed = ', 4, mcl(a=13, b=0, m=2**6, seed=4, n=4))

# Exemplo 3
print('Exemplo 3')
print(mcl(a=19, b=0, m=100, seed=63, n=10))

# Uso comercial
print('Uso comercial')
x = mcl(a=7**5, b=0, m=2**31 - 1, seed=123456, n=10)
x = [i / 2**31 for i in x]
print(x)
