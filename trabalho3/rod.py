'''
,---.     |                      ,--.          |
|---',---.|    ,---.    ,---.    |   |,---.,---|,---.
|  \ |   ||    ,---|    |   |    |   |,---||   ||   |
`   ``---'`---'`---^    `---'    `--' `---^`---'`---'
-----------------------------------------------------------

Geradores de variáveis aleatórias.
'''

def uniform(a, b, m, seed):
    random = (a * seed + b) % m
    while(True):
        random = (a * random + b) % m
        yield random / m

def bernoulli(p, a, b, m, seed):
    u = uniform(a,b,m,seed)
    while(True):
        yield ( next(u) < p )

def binomial(n, p, a, b, m, seed):
    u = uniform(a,b,m,seed)
    if p >= 1.:
        while True: yield n
    if p <= 0.:
        while True: yield 0
    c = p / (1-p)
    while True:
        random = next(u)
        pr = (1-p) ** n  #  função densidade
        ac = pr  #  função distribuição acumulada
        i = 0
        while (random >= ac):
            pr *= c * (n-i)/(i+1)
            ac += pr
            i += 1
        yield i

def binomial_2(n, p, a, b, m, seed):
    b = bernoulli(p, a, b, m, seed)
    while True:
        yield sum([next(b) for i in range(n)])

def geometric(n, p, a, b, m, seed):
    '''
        Explicação:
        next(([iterator]), [default])
        seja itr = (i for i in range(n)), itr é um iterator,
        logo o comando next(itr) como já vimos gerará 
        o próximo elemento desse iterator.
        
        Já a expressão (i for i in range(n) if [statment]) é um filtro,
        logo o iterador só gerará os elementos que passam nesse filtro.
        
        Por fim o None, será lançado caso nenhum elemento passe no filtro.

        A distribuição geométrica nos retornará quantas vezes 
        um lançamento de bernoulli falhou até que ocorra o primeiro sucesso.
    '''
    b = bernoulli(p, a, b, m, seed)
    while True:
        yield next((i for i in range(n) if next(b)), None)


# Samples

a = 7**5
b = 0
m = 2**31 - 1
seed = 5555

# Só pra não ter que botar (a, b, m, seed) em todas as funções,
# A ideia é que fique bem claro os parâmetros da distribuição
# Não sei se isso é interessante. No momento fica menos poluido

pr = { "a": a,
      "b": b,
      "m": m,
      "seed": seed }

def sample_uniform(size, pr=pr):
    u = uniform(pr['a'], pr['b'], pr['m'], pr['seed'])
    return [next(u) for i in range(size)]

def sample_bernoulli(p, size, pr=pr):
    b = bernoulli(p, pr['a'], pr['b'], pr['m'], pr['seed'])
    return [next(b) for i in range(size)]
    
def sample_binomial(n, p, size, pr=pr):
    b = binomial(n, p, pr['a'], pr['b'], pr['m'], pr['seed'])
    return [next(b) for i in range(size)]
    
def sample_binomial_2(n, p, size, pr=pr):
    b = binomial_2(n, p, pr['a'], pr['b'], pr['m'], pr['seed'])
    return [next(b) for i in range(size)]

def sample_geometric(n, p, size, pr=pr):
    b = geometric(n, p, pr['a'], pr['b'], pr['m'], pr['seed'])
    return [next(b) for i in range(size)]


print("uniform", sample_uniform(5))
print("Bernoulli", sample_bernoulli(0.5, 5))
print("Binomial", sample_binomial(10,0.5, 5))
#print(sample_binomial_2(10,0.5, 5))
print("Geometric", sample_geometric(10, 0.2, 5))