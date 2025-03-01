
import numpy as np


def modulus_rigidity(E:float, v:float):
    """_summary_

    Args:
        E (float): _description_
        v (float): _description_

    Returns:
        _type_: _description_
    """
    return E/(2*(1+v))


def ms(load:float, limit:float, sf:float) -> float:
    
    return limit/(sf*load) - 1


def von_mises(stress_tensor: np.ndarray):
    term1 = (stress_tensor[0,0] - stress_tensor[1,1])**2
    term2 = (stress_tensor[1,1] - stress_tensor[2,2])**2
    term3 = (stress_tensor[2,2] - stress_tensor[0,0])**2
    term4 = 6*(stress_tensor[1,2]**2 + stress_tensor[2,0]**2 + stress_tensor[0,1]**2)
    return np.sqrt(1/2*(term1 + term2 + term3 + term4))


def tresca(stress_tensor: np.ndarray):
    return stress_tensor[0,0] - stress_tensor[2,2]