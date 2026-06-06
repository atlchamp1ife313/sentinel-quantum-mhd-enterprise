import numpy as np

class IdealMHDEngine:
    """Solves fluid-magnetic interactions mimicking NIMROD, FLASH, and ALEGRA."""
    def __init__(self):
        self.mu_0 = 4.0 * np.pi * 1e-7  # Permeability of free space
        
    def compute_magnetic_pressure(self, magnetic_field_strength_B):
        # B_magnetic pressure = B^2 / (2 * mu_0)
        magnetic_pressure = (magnetic_field_strength_B ** 2) / (2.0 * self.mu_0)
        return magnetic_pressure