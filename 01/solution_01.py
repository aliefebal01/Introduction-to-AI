import numpy as np
import scipy as sc

def maximize_mean(mu_vector, sigma_vector):
    """
    Please modify the body of this function according to the description in exercise 1.1.1
    """
    A = len(mu_vector)
    max_mean_outcome = -np.inf 
    max_mean_action = None

    for a in range(A):
        func = lambda x: x / np.sqrt(2*np.pi*sigma_vector[a]**2) * np.exp(-(x-mu_vector[a])**2/(2*sigma_vector[a]**2))
        mean_outcome = sc.integrate.quad(func, -np.inf, np.inf)[0]
        if mean_outcome > max_mean_outcome:
            max_mean_outcome = mean_outcome
            max_mean_action = a
        
    return max_mean_action

def maximize_ucb(mu_vector, sigma_vector):
    """
    Please modify the body of this function according to the description in exercise 1.1.2
    """
    A = len(mu_vector)
    beta = 2
    max_outcome = -np.inf
    max_action = None

    for a in range(A):
        outcome = mu_vector[a] + beta * sigma_vector[a]
        if outcome > max_outcome:
            max_outcome = outcome
            max_action = a

    return max_action

def maximize_utility(mu_vector, sigma_vector, utility_function):
    """
    Please modify the body of this function according to the description in exercise 1.1.3
    """
    A = len(mu_vector)
    n_samples = 1000
    max_expected_utility = -np.inf
    best_decision = None

    for a in range(A):
        samples = np.random.normal(mu_vector[a], sigma_vector[a], n_samples)
        utilities = np.array([utility_function(sample) for sample in samples])
        expected_utility = np.mean(utilities)
        if expected_utility > max_expected_utility:
            max_expected_utility = expected_utility
            best_decision = a

    return best_decision

def maximize_mean_using_simulator(simulator, A, n):
    """
    Please modify the body of this function according to the description in exercise 1.2
    """
    max_mean_outcome = -np.inf
    max_mean_action = None
    saample_per_action = n // A #action başına kaç tane sample üreticem

    for a in range(A):
        samples = np.array([simulator(a) for _ in range(saample_per_action)])
        mean_outcome = np.mean(samples)
        if mean_outcome > max_mean_outcome:
            max_mean_outcome = mean_outcome
            max_mean_action = a
        
    return max_mean_action
