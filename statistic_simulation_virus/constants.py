import numpy as np
# params for normal_distribution
recoveryTimeMean = 14
recoveryTimeSigma = 3

mean_already_sick = 10
sigma_already_sick = 2

mean_vaccinated = 7
sigma_vaccinated = 1.5

mean_vaccinated_and_sick = 5
sigma_vaccinated_and_sick = 1



def get_normal_distribution(centre, std, size=None):
    return np.random.normal(loc=centre, scale=std, size=size)

def get_binomial_distribution(n, p, size=None):
    return np.random.binomial(n, p, size=size)