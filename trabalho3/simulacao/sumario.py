import numpy as np
from .random import Random
from beautifultable import BeautifulTable
from scipy import stats

class Sumario():
    def __init__(self, rd=None, n_samples=3):
        self.rd = Random() if rd == None else rd
        self.n_samples = n_samples

    def binomial(self, n=10, p=0.5, size=1000):
        mean_esp, variance_esp, skewness_esp, kurtosis_esp = stats.binom.stats(n, p, moments='mvsk')
        median_esp = stats.binom.median(n, p)
        std_esp = stats.binom.std(n, p)
        q1_esp = stats.binom.ppf(0.25, n, p)
        q3_esp = stats.binom.ppf(0.75, n, p)

        esperado = ['Teórica', size, mean_esp, median_esp, variance_esp, std_esp,
                    kurtosis_esp, skewness_esp, q1_esp, q3_esp]

        # Amostras
        observados = []
        for i in range(self.n_samples):
            sample_binomial = self.rd.binomial(n, p, size)
            sample_summary = self.describe(sample_binomial)
            sample_summary.insert(0, i)
            observados.append(sample_summary)

        return esperado, observados

    def triangular(self, lower=0., upper=1., mode=0.5, size=1000):
        scale = upper-lower
        c = mode/scale
        loc = lower
        mean_esp, variance_esp, skewness_esp, kurtosis_esp = stats.triang.stats(c, loc, scale, moments='mvsk')

        median_esp = stats.triang.median(c, loc, scale)
        std_esp = stats.triang.std(c, loc, scale)
        q1_esp = stats.triang.ppf(0.25, c, loc, scale)
        q3_esp = stats.triang.ppf(0.75, c, loc, scale)

        esperado = ['Teórica', size, mean_esp, median_esp, variance_esp, std_esp,
                    kurtosis_esp, skewness_esp, q1_esp, q3_esp]

        # Amostras
        observados = []
        for i in range(self.n_samples):
            sample_triangular = self.rd.triangular(lower, upper, mode, size)
            sample_summary = self.describe(sample_triangular)
            sample_summary.insert(0, i)
            observados.append(sample_summary)

        return esperado, observados

    def geometric(self, p=0.5, size=1000):
        loc=0
        mean_esp, variance_esp, skewness_esp, kurtosis_esp = stats.geom.stats(p, loc, moments='mvsk')

        median_esp = stats.geom.median(p, loc)
        std_esp = stats.geom.std(p, loc)
        q1_esp = stats.geom.ppf(0.25, p, loc)
        q3_esp = stats.geom.ppf(0.75, p, loc)

        esperado = ['Teórica', size, mean_esp, median_esp, variance_esp, std_esp,
                    kurtosis_esp, skewness_esp, q1_esp, q3_esp]

        # Amostras
        observados = []
        for i in range(self.n_samples):
            sample_geometric = self.rd.geometric(p, size)
            sample_summary = self.describe(sample_geometric)
            sample_summary.insert(0, i)
            observados.append(sample_summary)

        return esperado, observados

    def weibull(self, alpha=1, beta=1, size=1000):
        c = alpha
        loc = 0
        scale = beta
        mean_esp, variance_esp, skewness_esp, kurtosis_esp = stats.weibull_min.stats(c, loc, scale, moments='mvsk')

        median_esp = stats.weibull_min.median(c, loc, scale)
        std_esp = stats.weibull_min.std(c, loc, scale)
        q1_esp = stats.weibull_min.ppf(0.25, c, loc, scale)
        q3_esp = stats.weibull_min.ppf(0.75, c, loc, scale)

        esperado = ['Teórica', size, mean_esp, median_esp, variance_esp, std_esp,
                    kurtosis_esp, skewness_esp, q1_esp, q3_esp]

        # Amostras
        observados = []
        for i in range(self.n_samples):
            sample_weibull = self.rd.weibull(alpha, beta, size)
            sample_summary = self.describe(sample_weibull)
            sample_summary.insert(0, i)
            observados.append(sample_summary)

        return esperado, observados

    def gerar_tabela(self, esperado, observados, mean_stats=None):
        table = BeautifulTable()
        table.set_style(BeautifulTable.STYLE_COMPACT)
        table.columns.header = ['Amostras', 'size', 'mean', 'median', 'variance', 'std', 'kurtosis', 'skewness', 'Q1', 'Q3']
        table.rows.append(esperado)
        for row in observados:
            table.rows.append(row)
        media = ['Média']
        columns = np.array(table.columns)[1:].astype(np.double)
        media.extend(columns.mean(axis=1))
        table.rows.append(media)
        return table

    def gerar_grafico(self, esp, obs):
        pass

    def describe(self, sample):
        n, _, mean_obs, variance_obs, skewness_obs, kurtosis_obs = stats.describe(sample)
        median_obs = np.median(sample)
        std_obs = np.sqrt(variance_obs)
        q1_obs = np.quantile(sample, 0.25)
        q3_obs = np.quantile(sample, 0.75)

        return [n, mean_obs, median_obs, variance_obs, std_obs, kurtosis_obs, skewness_obs, q1_obs, q3_obs]


