import time
from rod import unif, bernoulli, binomial, geometric


class Random():
    
    def __init__(self, a=7**5, b=0, m=2**31-1, seed=time.time_ns()):
        self.a = a
        self.b = b
        self.m = m
        self.seed = seed
    
    def seed(self, new_seed):
        self.seed = new_seed

    def uniform(self, size):
        u = unif(self.a, self.b, self.m, self.seed)
        return [next(u) for i in range(size)]

    def bernoulli(self, p, size):
        b = bernoulli(p, self.a, self.b, self.m, self.seed)
        return [next(b) for i in range(size)]

    def binomial(self, n, p, size):
        b = binomial(n, p, self.a, self.b, self.m, self.seed)
        return [next(b) for i in range(size)]

    def geometric(self, n, p, size):
        g = geometric(n, p, self.a, self.b, self.m, self.seed)
        return [next(g) for i in range(size)]

rd = Random()

print(rd.uniform(10))
print(rd.bernoulli(0.6, 10))
print(rd.binomial(20, 0.6, 10))
print(rd.geometric(20, 0.5, 10))