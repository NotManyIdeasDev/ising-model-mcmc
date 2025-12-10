from src import model, dynamics, observables
import matplotlib.pyplot as plt
import numpy as np

# global parameters
L = 30
temps = [0.01, 0.3, 0.6, 1, 1.5, 2, 2.269, 2.6, 3, 3.3, 4, 6, 10, 50]
thermalization_sweeps = 100
measurement_sweeps = 500
measurement_interval = 1
J = 1

M_values = np.array([])
E_values = np.array([])
steps = np.array([])

def run_visual_demo(beta):
    spins = model.create_lattice(L)
    plt.figure()
    im = plt.imshow(spins, cmap="bwr", interpolation="nearest")
    plt.colorbar(label="Spin")
    plt.title(f"Spin configuration (T = {(1 / beta):.3f})")
    plt.axis("off")
    plt.tight_layout()
    plt.ion()
    plt.show()

    def callback(spins, step):
        im.set_data(spins)
        plt.draw()
        plt.pause(0.02)

    dynamics.run_simulation(spins, beta, J, thermalization_sweeps, measurement_sweeps, measurement_interval, callback)

def main():
    run_visual_demo(1/temps[6])

if __name__ == "__main__":
    main()