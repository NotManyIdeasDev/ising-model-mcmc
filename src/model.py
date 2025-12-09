import numpy as np
def create_lattice(L):
    return np.random.choice([1, -1], size=(L, L))


def get_neighbors(spins: np.ndarray, i, j):
    left = spins[i, (j - 1) % spins.shape[0]]
    right = spins[i, (j + 1) % spins.shape[0]]
    up = spins[(i - 1) % spins.shape[0], j]
    down = spins[(i + 1) % spins.shape[0], j]
    return np.array([left, right, up, down]) 