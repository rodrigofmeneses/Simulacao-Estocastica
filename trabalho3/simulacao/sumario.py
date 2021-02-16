from .random import Random
from math import sqrt
from scipy import stats


class Sumario():
    def __init__(self):
        rd = Random()

    def binomial(self, n=10, p=10, size=1000):
        sample_binomial = rd.binomial(n, p, size)
        # Valores Esperados
        #esp = [mean_esp, variance_esp, skewness_esp, kurtosis_esp]
        esp = stats.binom.stats(n, p, moments='mvsk')

        # Valores Observados
        # obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]
        
        _, _, mean_obs, variance_obs, skewness_obs, kurtosis_obs = stats.describe(sample_binomial)
        obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]

        self.gerar_tabela(esp, obs)
        self.gerar_grafico(esp, obs)

    def triangular(self, lower=0, upper=1, mode=0.5, size=1000):
        sample_triangular = rd.triangular(lower, upper, mode, size)
        # Valores Esperados
        #esp = [mean_esp, variance_esp, skewness_esp, kurtosis_esp]
        esp = stats.triang.stats(c=mode/(upper-lower), \
                                 loc=lower, \
                                 scale=(upper-lower), \
                                 moments='mvsk')

        # Valores Observados
        # obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]
        
        _, _, mean_obs, variance_obs, skewness_obs, kurtosis_obs = stats.describe(sample_triangular)
        obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]

        self.gerar_tabela(esp, obs)
        self.gerar_grafico(esp, obs)

    def geometric(self, p=0.5, size=1000):
        sample_geometric = rd.geometric(p, size)
        # Valores Esperados
        #esp = [mean_esp, variance_esp, skewness_esp, kurtosis_esp]
        esp = stats.geom.stats(p=p, loc=0, moments='mvsk')

        # Valores Observados
        # obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]
        
        _, _, mean_obs, variance_obs, skewness_obs, kurtosis_obs = stats.describe(sample_geometric)
        obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]

        self.gerar_tabela(esp, obs)
        self.gerar_grafico(esp, obs)

    def weibull(self, alpha=1, beta=1, size=1000):
        sample_weibull = rd.weibull(alpha, beta, size)
        # Valores Esperados
        #esp = [mean_esp, variance_esp, skewness_esp, kurtosis_esp]
        esp = stats.weibull_min.stats(c=alpha, \
                                      loc=0, \
                                      scale=beta, \
                                      moments='mvsk')

        # Valores Observados
        # obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]
        
        _, _, mean_obs, variance_obs, skewness_obs, kurtosis_obs = stats.describe(sample_weibull)
        obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]

        self.gerar_tabela(esp, obs)
        self.gerar_grafico(esp, obs)


    def gerar_tabela(self, esp, obs):
        pass

    def gerar_grafico(self, esp, obs):
        pass

        
    

        
