'''
,---.     |                      ,--.          |
|---',---.|    ,---.    ,---.    |   |,---.,---|,---.
|  \ |   ||    ,---|    |   |    |   |,---||   ||   |
`   ``---'`---'`---^    `---'    `--' `---^`---'`---'
-----------------------------------------------------------

Geradores de variáveis aleatórias.
'''

def unif(a, b, m, seed):
    random = (a * seed + b) % m
    while(True):
        random = (a * random + b) % m
        yield random / m

def bernoulli(p, a, b, m, seed):
    u = unif(a,b,m,seed)
    while(True):
        yield ( next(u) < p )

def binomial(n, p, a, b, m, seed):
    u = unif(a,b,m,seed)
    if p >= 1.:
        while True: yield n
    if p <= 0.:
        while True: yield 0
    c = p / (1-p)
    while(True):
        random = next(u)
        pr = (1-p) ** n  #  função densidade
        ac = pr  #  função distribuição acumulada
        i = 0
        while (random >= ac):
            pr *= c * (n-i)/(i+1)
            ac += pr
            i += 1
        yield i

