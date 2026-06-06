import numpy as np

class AblationMaterialEngine:
    """Tracks matrix charring depth and ablation front movement mimicking PICA/FIAT."""
    def __init__(self):
        self.char_density_limit = 250.0  # kg/m^3
        
    def compute_char_rate(self, current_density, surface_temperature):
        if surface_temperature < 800.0:
            return 0.0  # Below pyrolysis activation threshold
        
        # Arrhenius kinetics proxy for carbon matrix pyrolyzation
        char_rate = 1e4 * np.exp(-12000.0 / surface_temperature) * current_density
        return char_rate