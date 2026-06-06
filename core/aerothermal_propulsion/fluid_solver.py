import numpy as np

class HypersonicFluidEngine:
    """Simulates multi-species Navier-Stokes fluid updates mimicking LAURA/VULCAN-CFD."""
    def __init__(self):
        self.gamma = 1.4  # Ratio of specific heats
        
    def compute_mach_and_heat_flux(self, density, velocity, temperature):
        # Prevent math domain errors
        if density <= 0 or temperature <= 0:
            return 0.0, 0.0
        
        speed_of_sound = np.sqrt(self.gamma * 287.05 * temperature)
        mach_number = velocity / speed_of_sound
        
        # Approximated convective heat flux q = 0.5 * rho * v^3 * Stanton Number proxy
        convective_heat_flux = 0.5 * density * (velocity ** 3) * 0.002
        return mach_number, convective_heat_flux