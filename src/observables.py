import numpy as np

#Hamiltonian: H = -J *  sum_<i, j> sigma_i * sigma_j
def energy(spins: np.ndarray, J = 1):
    right_column = np.roll(spins, shift=-1, axis=1)
    bottom_row = np.roll(spins, shift=-1, axis=0)

    return -J * np.sum(spins * (right_column + bottom_row))

def energy_per_spin(spins: np.ndarray, J = 1):
    return energy(spins, J) / spins.size

def magnetization(spins: np.ndarray):
    return np.sum(spins)

def magnetization_per_spin(spins: np.ndarray):
    return np.sum(spins) / spins.size


