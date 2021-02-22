import simulacao as sim

sm = sim.sumario.Sumario(n_samples=3)

# esp, obs = sm.binomial(size=100000)
# print('\nBinomial')
# print('Esp: ', esp)
# print('Obs: ', obs)
# esp, obs = sm.geometric(size=100000)
# print('\nGeometrica')
# print('Esp: ', esp)
# print('Obs: ', obs)
# esp, obs = sm.triangular(size=100000)
# print('\nTriangular')
# print('Esp: ', esp)
# print('Obs: ', obs)
# esp, obs = sm.weibull(size=100000)
# print('\nWeibull')
# print('Esp: ', esp)
# print('Obs: ', obs)

print(sm.binomial(1000))

