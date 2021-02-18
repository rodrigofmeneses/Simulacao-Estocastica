import numpy as np
from .random import Random
from beautifultable import BeautifulTable
from scipy import stats

class Sumario():
    def __init__(self):
        self.rd = Random()

    def binomial(self, n=10, p=0.5, size=1000, n_samples=10):
        # Valores Esperados
        #esperado = [mean_esp, variance_esp, skewness_esp, kurtosis_esp]
        
        mean_esp, variance_esp, skewness_esp, kurtosis_esp = stats.binom.stats(n, p, moments='mvsk')
        median_esp = stats.binom.median(n, p)
        std_esp = stats.binom.std(n, p)

        esperado = ['Teórica', mean_esp, median_esp, variance_esp, std_esp, kurtosis_esp, skewness_esp]

        # Valores Observados
        # obs = [mean_obs, median_obs, variance_obs, std_obs, kurtosis_obs, skewness_obs]
        
        # Amostras
        observados = []
        for i in range(n_samples):
            self.rd.seed = np.random.randint(10000)
            sample_binomial = self.rd.binomial(n, p, size)

            _, _, mean_obs, variance_obs, skewness_obs, kurtosis_obs = stats.describe(sample_binomial)
            median_obs = stats.median_abs_deviation(sample_binomial)
            std_obs = np.sqrt(variance_obs)
            
            observados.append([self.rd.seed, mean_obs, median_obs, variance_obs, std_obs, kurtosis_obs, skewness_obs])

        self.gerar_tabela(esperado, observados)
        # self.gerar_grafico(esp, obs)
        # return esp, obs

    def triangular(self, lower=0, upper=1, mode=0.5, size=1000):
        sample_triangular = self.rd.triangular(lower, upper, mode, size)
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
        return esp, obs

    def geometric(self, p=0.5, size=1000):
        sample_geometric = self.rd.geometric(p, size)
        # Valores Esperados
        #esp = [mean_esp, variance_esp, skewness_esp, kurtosis_esp]
        esp = stats.geom.stats(p=p, loc=0, moments='mvsk')

        # Valores Observados
        # obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]
        
        _, _, mean_obs, variance_obs, skewness_obs, kurtosis_obs = stats.describe(sample_geometric)
        obs = [mean_obs, variance_obs, skewness_obs, kurtosis_obs]

        self.gerar_tabela(esp, obs)
        self.gerar_grafico(esp, obs)
        return esp, obs

    def weibull(self, alpha=1, beta=1, size=1000):
        sample_weibull = self.rd.weibull(alpha, beta, size)
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
        return esp, obs


    def gerar_tabela(self, esperado, observados, mean_stats=None, n_samples=None):
        table = BeautifulTable()
        table.columns.header = ['Amostras', 'mean', 'median', 'variance', 'std', 'kurtosis', 'skewness']
        table.rows.append(esperado)
        for row in observados:
            table.rows.append(row)
        print(table)

    def gerar_grafico(self, esp, obs):
        pass


        
