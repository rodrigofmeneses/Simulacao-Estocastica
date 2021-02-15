from math import log, log2, trunc, sqrt

## Dicionário de valores padrões ##

pr = { "a": 7**5,
      "b": 2*(3**10) - 1,
      "m": 2**31 - 1,
      "seed": 123654 }

def uniform(a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    random = (a * seed + b) % m
    while(True):
        random = (a * random + b) % m
        yield random / m

def bernoulli(p, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    u = uniform(a,b,m,seed)
    while(True):
        yield ( next(u) < p )

def binomial(n, p, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    u = uniform(a,b,m,seed)
    if p >= 1.:
        while True: yield n
    if p <= 0.:
        while True: yield 0
    c = p / (1-p)
    while True:
        random = next(u)
        fd = (1-p) ** n  #  função densidade
        ac = fd  #  função distribuição acumulada
        i = 0
        while (random >= ac):
            fd *= c * (n-i)/(i+1)
            ac += fd
            i += 1
        yield i

def binomial2(n, p, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    b = bernoulli(p, a, b, m, seed)
    while True:
        yield sum([next(b) for i in range(n)])

#  def geometric(n, p, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
#      '''
#          Explicação:
#          next(([iterator]), [default])
#          seja itr = (i for i in range(n)), itr é um iterator,
#          logo o comando next(itr) como já vimos gerará
#          o próximo elemento desse iterator.
#
#          Já a expressão (i for i in range(n) if [statment]) é um filtro,
#          logo o iterador só gerará os elementos que passam nesse filtro.
#
#          Por fim o None, será lançado caso nenhum elemento passe no filtro.
#
#          A distribuição geométrica nos retornará quantas vezes
#          um lançamento de bernoulli falhou até que ocorra o primeiro sucesso.
#      '''
#      bl = bernoulli(p, a, b, m, seed)
#      while True:
#          yield next((i for i in range(n) if next(bl)), None)
def geometric(p, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    u = uniform(a,b,m,seed)
    while True:
        yield 1 + trunc(log2(next(u)) / log2(1-p))

def triangular(lower, upper, mode,
               a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    u = uniform(a,b,m,seed)
    diff = upper - lower
    right = upper - mode
    left = mode - lower
    mode_mp = left / diff
    while True:
        p = next(u)
        if p < mode_mp:
            yield lower + sqrt(p * diff * left)
        else:
            yield upper - sqrt((1 - p) * diff * right)

def weibull(alpha, beta, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    """
    F(x) = 1 - exp{ -(x/beta)^alpha }
    """
    u = uniform(a,b,m,seed)
    while True:
        yield beta*( (-log( next(u) ))**(-alpha) )

def sample_uniform(size, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    u = uniform(a,b,m,seed)
    return [next(u) for i in range(size)]

def sample_bernoulli(p, size, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    b = bernoulli(p, a, b, m, seed)
    return [next(b) for i in range(size)]

def sample_binomial(n, p, size, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    b = binomial(n, p, pr["a"], pr["b"], pr["m"], pr["seed"])
    return [next(b) for i in range(size)]

def sample_binomial2(n, p, size, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    b = binomial2(n, p, a, b, m, seed)
    return [next(b) for i in range(size)]

def sample_geometric(p, size, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    b = geometric(p, a, b, m, seed)
    return [next(b) for i in range(size)]

def sample_triangular(lower, upper, mode,
                      size, a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    t = triangular(lower, upper, mode, a, b, m, seed)
    return [next(t) for i in range(size)]

def sample_weibull(alpha, beta, size,
                   a=pr["a"], b=pr["b"], m=pr["m"], seed=pr["seed"]):
    w = weibull(alpha, beta, a, b, m, seed)
    return [next(w) for i in range(size)]

#  print("uniform", sample_uniform(5))
#  print("Bernoulli", sample_bernoulli(0.5, 5))
#  print("Binomial", sample_binomial(10,0.5, 5))
#  print(sample_binomial_2(10,0.5, 5))
#  print("Geometric", sample_geometric(10, 0.2, 5))

