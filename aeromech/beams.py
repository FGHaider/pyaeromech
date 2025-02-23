
import numpy as np
from exceptions import UnknownBoundary

def euler_beam_buckling_load(E:float, I:float, L:float, boundary: str):
    
    match boundary:
        case "pinned_pinned":
            K = 1.0
        case "fixed_fixed":
            K = 0.5
        case "fixed_pinned":
            K = 0.699
        case "fixed_latfree":
            K = 2.0
        case _:
            UnknownBoundary(f"The boundary {boundary} is not known, should be entered as 'boundary_boundary' for the top and bottom")
            
    return np.pi**2 * E * I / (K * L)**2