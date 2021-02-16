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

    
    def gerar_tabela(self, esp, obs):
        pass

    def gerar_grafico(self, esp, obs):
        pass

        
    

        