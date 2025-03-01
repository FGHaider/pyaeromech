
import numpy as np
from pyaeromech.exceptions import UnknownType

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

def material(name: str, unit: str="SI"):
    """Provides some standard material properties for ease of experimentation.
    Values are based of:
        Steel - Stainless 316
        Titanium - Ti6Al4V
        Aluminium - 7075
        Magnesium - AZ31
    Material data is all at room temperature. 
    Returns in order, Youngs Modulus, Poission ratio, density and thermal expansion coeff.
    Args:
        name (str): Name of material
        unit (str, optional): Defaults to "SI".
    """
    if unit == "SI":
        materials = {"Titanium": {"E": 114e9, "v": 0.33, "rho": 4430, 'alpha': 8.6e-6},
                         "Steel": {"E": 193e9, "v": 0.30, "rho": 8000, 'alpha': 15.9e-6},
                         "Aluminium": {"E": 70.3e9, "v": 0.33, "rho": 2800, 'alpha': 23.6e-6},
                         "Magnesium": {"E": 44.8e9, "v": 0.35, "rho": 1770, 'alpha': 14.4e-6}}
    else:
        raise UnknownType("Only SI units supported")
    material_data = materials[name]
    return material_data["E"], material_data["v"], material_data["rho"], material_data["alpha"]