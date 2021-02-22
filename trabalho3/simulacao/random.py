from .geradores import *

import time

class Random():

    def __init__(self, a=7**5, b=2*(3**10) - 1, m=2**31 - 1, seed=time.time_ns()):
        self.a = a
        self.b = b
        self.m = m
        self.seed = seed
        self.generators = dict()

    def set_seed(self, new_seed):
        self.seed = new_seed
        self.generators.clear()

    def uniform(self, size):
        if 'uniform' not in self.generators:
            self.generators['uniform'] = uniform(self.a, self.b, self.m, self.seed)
        u = self.generators['uniform']
        return [next(u) for i in range(size)]

    def bernoulli(self, p, size):
        if 'bernoulli' not in self.generators:
            self.generators['bernoulli'] = bernoulli(p, self.a, self.b, self.m, self.seed)
        bl = self.generators['bernoulli']
        return [next(bl) for i in range(size)]

    def binomial(self, n, p, size):
        if 'binomial' not in self.generators:
            self.generators['binomial'] = binomial(n, p, self.a, self.b, self.m, self.seed)
        bl = self.generators['binomial']
        return [next(bl) for i in range(size)]

    def geometric(self, p, size):
        if 'geometric' not in self.generators:
            self.generators['geometric'] = geometric(p, self.a, self.b, self.m, self.seed)
        g = self.generators['geometric']
        return [next(g) for i in range(size)]

    def triangular(self, lower, upper, mode, size):
        if 'triangular' not in self.generators:
            self.generators['triangular'] = triangular(lower, upper, mode, self.a, self.b, self.m, self.seed)
        t = self.generators['triangular']
        return [next(t) for i in range(size)]

    def weibull(self, alpha, beta, size):
        if 'weibull' not in self.generators:
            self.generators['weibull'] = weibull(alpha, beta, self.a, self.b, self.m, self.seed)
        w = self.generators['weibull']
        return [next(w) for i in range(size)]
