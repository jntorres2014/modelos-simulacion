import numpy as np
import scipy.stats

def confidence_interval(n_sample, mean, std, z_value=2.57, coeff=1.):
    # By default, it calculates the CI with a confidence level of 99%
    # Change `z_value` accordingly.
    # Optionally, use `coeff` to get a CI with a greater error margin
    z_term = coeff * (z_value * std / (n_sample ** 0.5))
    inf = mean - z_term
    sup = mean + z_term
    return inf, sup



def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

    