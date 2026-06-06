import numpy as np

class RarefiedKineticSolver:
    """Tracks discrete particle collisions/plasma parameters mimicking SPARTA/GKEYLL."""
    def __init__(self):
        self.boltzmann_k = 1.380649e-23
        
    def compute_knudsen_number(self, density, characteristic_length, molecular_diameter=3.7e-10):
        if density <= 0 or characteristic_length <= 0:
            return float('inf')
        # Number density n
        n = density / 4.65e-26  # assuming N2 mass proxy
        # Mean free path lambda = 1 / (sqrt(2) * pi * d^2 * n)
        mean_free_path = 1.0 / (np.sqrt(2.0) * np.pi * (molecular_diameter ** 2) * n)
        knudsen_num = mean_free_path / characteristic_length
        return knudsen_num