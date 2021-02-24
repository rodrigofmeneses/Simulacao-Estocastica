import numpy as np
from .random import Random
#  from beautifultable import BeautifulTable
from scipy import stats
from scipy.special import gamma

class Sumario():
    def __init__(self, rd=None, n_samples=3):
        self.rd = Random() if rd == None else rd
        self.n_samples = n_samples

    def binomial(self, n=10, p=0.5, size=1000):
        #  mean_esp, variance_esp, skewness_esp, kurtosis_esp = stats.binom.stats(n, p, moments='mvsk')
        mean_esp = n*p
        variance_esp = n*p*(1.-p)
        skewness_esp = ((1.-p) - p) / np.sqrt(variance_esp)
        kurtosis_esp = (1.- 6*p*(1.-p)) / variance_esp
        median_esp = np.trunc(n*p)
        mode_esp = np.trunc( (n+1.)*p )
        std_esp = np.sqrt(variance_esp)
        q1_esp = stats.binom.ppf(0.25, n, p)
        q3_esp = stats.binom.ppf(0.75, n, p)

        esperado = ['Teórica', size, mean_esp, mode_esp, median_esp, variance_esp, std_esp,
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
        #  mean_esp, variance_esp, skewness_esp, kurtosis_esp = stats.triang.stats(c, loc, scale, moments='mvsk')

        mean_esp = (lower + upper + mode) / 3.
        variance_esp = (lower**2 + upper**2 + mode**2 - lower*upper - lower*mode - upper*mode)/18.
        skewness_esp = np.sqrt(2)*((lower+upper-2*mode)*(2*lower-upper-mode)*(lower-2*upper+mode)) / \
            ((lower**2 + upper**2 + mode**2 - lower*upper - lower*mode - upper*mode)**1.5)
        kurtosis_esp = -(3./5.)
        median_esp = stats.triang.median(c, loc, scale)
        mode_esp = mode
        std_esp = np.sqrt(variance_esp)
        q1_esp = stats.triang.ppf(0.25, c, loc, scale)
        q3_esp = stats.triang.ppf(0.75, c, loc, scale)

        esperado = ['Teórica', size, mean_esp, mode_esp, median_esp, variance_esp, std_esp,
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
        #  mean_esp, variance_esp, skewness_esp, kurtosis_esp = stats.geom.stats(p, loc, moments='mvsk')

        mean_esp = 1./p
        variance_esp = (1.-p)/p**2
        skewness_esp = (2.-p)/np.sqrt(1.-p)
        kurtosis_esp = 6. + p**2/(1.-p)
        median_esp = np.ceil(-1./np.log2(1.-p))
        mode_esp = 1
        std_esp = np.sqrt(variance_esp)
        q1_esp = stats.geom.ppf(0.25, p, loc)
        q3_esp = stats.geom.ppf(0.75, p, loc)

        esperado = ['Teórica', size, mean_esp, mode_esp, median_esp, variance_esp, std_esp,
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
        #  mean_esp, variance_esp, skewness_esp, kurtosis_esp = stats.weibull_min.stats(c, loc, scale, moments='mvsk')

        mean_esp = beta*gamma(1.+1./alpha)
        variance_esp = beta**2 * (gamma(1.+2./alpha)-gamma(1.+1./alpha)**2)
        median_esp = stats.weibull_min.median(c, loc, scale)
        mode_esp = beta * ( (alpha-1)/alpha )**(1/alpha) if alpha>1 else 0
        std_esp = np.sqrt(variance_esp)
        skewness_esp = (gamma(1.+3./alpha)*(beta**3) - 3.*mean_esp*variance_esp -mean_esp**3)/std_esp**3
        kurtosis_esp = (beta**4 * gamma(1.+4./alpha)-4.*skewness_esp*(std_esp**3)*mean_esp \
                                -6.*(mean_esp**2)*variance_esp - mean_esp**4)/(variance_esp**2) - 3.
        q1_esp = stats.weibull_min.ppf(0.25, c, loc, scale)
        q3_esp = stats.weibull_min.ppf(0.75, c, loc, scale)

        esperado = ['Teórica', size, mean_esp, mode_esp, median_esp, variance_esp, std_esp,
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
        #  table = BeautifulTable()
        #  table.set_style(BeautifulTable.STYLE_COMPACT)
        #  table.columns.header = ['Amostras', 'size', 'mean', 'mode', 'median', 'variance', 'std', 'kurtosis', 'skewness', 'Q1', 'Q3']
        #  table.rows.append(esperado)
        table = []
        table.append(esperado)
        table.extend(observados)
        #  for row in observados:
            #  table.rows.append(row)
        media = np.mean(table[1:], axis=0).tolist()
        media[0] = 'Média'
        table.append(media)
        return table

    def gerar_grafico(self, esp, obs):
        pass

    def describe(self, sample):
        n, _, mean_obs, variance_obs, skewness_obs, kurtosis_obs = stats.describe(sample)
        median_obs = np.median(sample)
        mode_obs, weights = stats.mode(sample)
        mode_obs = np.average(mode_obs, weights=weights)
        std_obs = np.sqrt(variance_obs)
        q1_obs = np.quantile(sample, 0.25)
        q3_obs = np.quantile(sample, 0.75)

        return [n, mean_obs, mode_obs, median_obs, variance_obs, std_obs, kurtosis_obs, skewness_obs, q1_obs, q3_obs]


