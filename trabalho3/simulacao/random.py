from .geradores import *

import time

class Random():

    def __init__(self, a=7**5, b=2*(3**10) - 1, m=2**31 - 1, seed=time.time_ns()):
        self.a = a
        self.b = b
        self.m = m
        self.seed = seed

    def set_seed(self, new_seed):
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

    def triangular(self, lower, upper, mode, size):
        t = triangular(lower, upper, mode, self.a, self.b, self.m, self.seed)
        return [next(t) for i in range(size)]

    def weibull(self, alpha, beta, size):
        w = weibull(alpha, beta, self.a, self.b, self.m, self.seed)
        return [next(w) for i in range(size)]
