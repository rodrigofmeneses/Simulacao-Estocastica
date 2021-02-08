import time
from rod import uniform, bernoulli, binomial, geometric, pr


class Random():

    def __init__(self, a=pr["a"], b=pr["b"], m=pr["m"], seed=time.time_ns()):
        self.a = a
        self.b = b
        self.m = m
        self.seed = seed

    def seed(self, new_seed):
        self.seed = new_seed

    def uniform(self, size):
        u = uniform(self.a, self.b, self.m, self.seed)
        return [next(u) for i in range(size)]

    def bernoulli(self, p, size):
        bl = bernoulli(p, self.a, self.b, self.m, self.seed)
        return [next(bl) for i in range(size)]

    def binomial(self, n, p, size):
        bl = binomial(n, p, self.a, self.b, self.m, self.seed)
        return [next(bl) for i in range(size)]

    def geometric(self, p, size):
        g = geometric(p, self.a, self.b, self.m, self.seed)
        return [next(g) for i in range(size)]

#  rd = Random()
#
#  print(rd.uniform(10))
#  print(rd.bernoulli(0.6, 10))
#  print(rd.binomial(20, 0.6, 10))
#  print(rd.geometric(20, 0.5, 10))
