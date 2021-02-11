from unittest import TestCase
from simulacao import Random

class GeneratorTests(TestCase):

    def test_uniform_generator(self):
        self.rd = Random(seed=123456)
        unif = self.rd.uniform(size=3)
        esp_unif = [0.053498726363060405, 0.15314897715726353, 0.9749140753293941]
        self.assertEqual(unif, esp_unif)
    
    def test_bernoulli_generator(self):
        self.rd = Random(seed=123456)
        bern = self.rd.bernoulli(p=0.7, size=3)
        esp_bern = [True, True, False]
        self.assertEqual(bern, esp_bern)

    def test_binomial_generator(self):
        self.rd = Random(seed=123456)
        bino = self.rd.binomial(n=10, p=0.7, size=3)
        esp_bino = [5, 6, 10]
        self.assertEqual(bino, esp_bino)
    
    def test_geometric_generator(self):
        self.rd = Random(seed=123456)
        geom = self.rd.geometric(p=0.7, size=3)
        esp_geom = [3, 2, 1]
        self.assertEqual(geom, esp_geom)
    
    def test_triangular_generator(self):
        self.rd = Random(seed=123456)
        triang = self.rd.triangular(0, 1, 0.5, size=3)
        esp_triang = [0.16355232551550652, 0.2767209579678268, 0.8880046325274883]
        self.assertEqual(triang, esp_triang)
    
    def test_weibull_generator(self):
        self.rd = Random(seed=123456)
        weib = self.rd.weibull(alpha=2, beta=3, size=3)
        esp_weib = [0.3499050475203916, 0.8521111957336273, 4647.835273399275]
        self.assertEqual(weib, esp_weib)