import numpy as np
import model 

def delta_energy(spins: np.ndarray, i, j, J = 1):
    return 2 * J * spins[i, j] * np.sum(model.get_neighbors(spins, i, j))

def metropolis_sweep(spins: np.ndarray, beta, J = 1):
    for _ in range(spins.size):
        i = np.random.randint(0, spins.shape[0])
        j = np.random.randint(0, spins.shape[0])

        delta_E = delta_energy(spins, i, j, J)
        acceptance_threshold = min(1, np.exp(-beta * delta_E))
        if np.random.uniform() <= acceptance_threshold:
            spins[i, j] *= -1
        
def run_simulation(spins: np.ndarray, beta, J, n_thermalization, n_sweeps, measure_interval, callback):
    for _ in range(n_thermalization):
        metropolis_sweep(spins, beta, J)
    
    for step in range(n_sweeps):
        metropolis_sweep(spins, beta, J)
        if step % measure_interval == 0:
            callback(spins, step)
