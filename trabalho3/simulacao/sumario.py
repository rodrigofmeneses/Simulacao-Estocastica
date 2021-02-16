from simulacao import Random
from scipy import stats


class Sumario():
    def __init__(self):
        rd = Random()

    def binomial(self, n=10, p=10, size=1000):
        sample_binomial = rd.binomial(n, p, size)
        # Valores Obtidos
        n, (smin, smax), sm, sv, ss, sk = stats.describe(sample_binomial)
        
        # Valores Esperados
        mean_esp = n * p
        meadian_esp = n * p * (1 - p)

    
    def gerar_tabela(self, esp, obs):
        pass

    def gerar_grafico(self, esp, obs):
        pass

        
    

        