
import numpy as np
from pyaeromech.exceptions import OutsideRange

    
def __concentration_calc(h: float, r: float, D: float, C: np.ndarray) -> float:
    """Generic function for stress concentrations"""
    
    ratio = h/r
    coefficients = C[:,0] + C[:,1]*np.sqrt(ratio) + C[:,2]*ratio
    C1 = coefficients[0]
    C2 = coefficients[1]
    C3 = coefficients[2]
    C4 = coefficients[3]
    ratio = 2*h/D
    return C1 + C2*ratio + C3*ratio**2 + C4*ratio**3
        
def square_shoulder_fillet_rect_section(L: float, D: float, r: float, h: float, loadtype:str) -> float:
    """Calculates the concentration factor for a square shoulder with fillet in a member of
    rectangular section. See Roark 7th Edition Table 17.1.5

    Args:
        L (float): Distance between fillet roots
        D (float): Width of section
        r (float): Radius of fillet
        h (float): Thickness of section
        loadtype (str): Loading type, axial_tension or in_plane_bending

    Returns:
        float: Concentration factor
    """
    ratio = h/r
    if L/D < 3/((r/(D-2*h))**(1/4)):
        raise("The ratio L/D is outside the valid limits")
    
    if loadtype == "axial_tension":
        if 0.1 <= ratio <= 2.0:
            C = np.array([[1.007, 1.000, -0.031],
                            [-0.114, -0.585, 0.314],
                            [0.241, -0.992, -0.271],
                            [-0.134, 0.577, -0.012]])
        elif 2.0 <= ratio <= 20.0:
            C = np.array([[1.042, 0.982, -0.036],
                            [-0.074, -0.156, -0.010],
                            [-3.418, 1.220, -0.005],
                            [3.450, -2.046, 0.051]])
    
    elif loadtype == "in_plane_bending":
        if 0.1 <= ratio <= 2.0:
            C = np.array([[1.007, 1.000, -0.031],
                            [-0.270, -2.404, 0.749],
                            [0.677, 1.133, -0.904],
                            [-0.414, 0.271, 0.186]])
        elif 2.0 <= ratio <= 20.0:
            C = np.array([[1.042, 0.982, -0.036],
                            [-3.599, 1.619, -0.431],
                            [6.084, -5.607, 1.158],
                            [-2.527, 3.006, -0.691]])
            
    else:
        raise(OutsideRange("The ratio h/r is outside the valid limits"))
    
    return __concentration_calc(h, r, D, C)
        
    
def two_u_notches_rect_section(h: float, r: float, D: float, loadtype:str) -> float:
    """Calculates the concentration factor for two u-notches in a member of rectangular section. 
    See Roark 7th Edition Table 17.1.1

    Args:
        h (float): Depth of u-notch
        r (float): Radius of u-notch root
        D (float): Width of rectangular section
        loadtype (str): Loading type, axial_tension, out_of_plane_bending or in_plane_bending

    Returns:
        float: Concentration factor
    """
    ratio = h/r
    
    if loadtype == "axial_tension":
        if ratio == 1:
            C = np.array([3.065, -3.370, 0.647, 0.658])
        elif 0.25 <= ratio <= 2.0:
            C = np.array([[0.850, 2.628, -0.413],
                            [-1.119, -4.826, 2.575],
                            [3.563, -0.514, -2.402],
                            [-2.294, 2.713, 0.240]])
        elif 2.0 <= ratio <= 50.0:
            C = np.array([[0.833, 2.069, -0.009],
                            [2.732, -4.157, 0.176],
                            [-8.859, 5.327, -0.320],
                            [6.294, -3.239, 0.154]])
    
    elif loadtype == "in_plane_bending":
        if ratio == 1:
            C = np.array([3.065, -6.269, 7.015, -2.812])
        elif 0.25 <= ratio <= 2.0:
            C = np.array([[0.723, 2.845, -0.504],
                            [-1.836, -5.746, 1.314],
                            [7.254, -1.885, 1.646],
                            [-5.140, 4.785, -2.456]])
        elif 2.0 <= ratio <= 50.0:
            C = np.array([[0.833, 2.069, -0.009],
                            [0.024, -5.383, 0.126],
                            [-0.856, 6.460, -0.199],
                            [0.999, -3.146, 0.082]])
    
    elif loadtype == "out_of_plane_bending":
        if ratio == 1:
            C = np.array([1.876, -2.756, 3.056, -1.175])
        elif 0.25 <= ratio <= 4.0:
            C = np.array([[1.031, 0.831, 0.014],
                            [-1.227, -1.646, 0.117],
                            [3.337, -0.750, 0.469],
                            [-2.141, 1.566, -0.600]])
            
    else:
        raise(OutsideRange("The ratio h/r is outside the valid limits"))
    

    return __concentration_calc(h, r, D, C)

    
def single_u_notch_rect_section(h: float, r: float, D: float, loadtype:str) -> float:
    """_summary_
    See Roark 7th Edition Table 17.1.3

    Args:
        h (float): _description_
        r (float): _description_
        D (float): _description_
        loadtype (str): _description_

    Returns:
        float: _description_
    """
    ratio = h/r
    
    if loadtype == "axial_tension":
        if ratio == 1:
            C = np.array([2.988, -7.300, 9.742, -4.429])
        elif 0.5 <= ratio <= 4.0:
            C = np.array([[0.721, 2.394, -0.127],
                            [1.978, -11.489, 2.211],
                            [-4.413, 18.751, -4.596],
                            [2.714, -9.655, 2.512]])
    
    elif loadtype == "in_plane_bending":
        if ratio == 1:
            C = np.array([2.988, -7.735, 10.674, -4.927])
        elif 0.5 <= ratio <= 4.0:
            C = np.array([[0.721, 2.394, -0.127],
                            [-0.426, -8.827, 1.518],
                            [2.161, 10.968, -2.455],
                            [-1.456, -4.535, 1.064]])
            
    else:
        raise(OutsideRange("The ratio h/r is outside the valid limits"))
    
    return __concentration_calc(h, r, D, C)
        
    
def single_v_notch_rect_section(h: float, r: float, D: float, theta:str) -> float:
    """_summary_
    See Roark 7th Edition Table 17.1.4

    Args:
        h (float): _description_
        r (float): _description_
        D (float): _description_
        theta (str): _description_

    Returns:
        float: _description_
    """
    ratio = 2*h/D
    Ktu = single_u_notch_rect_section(h,r,D, loadtype="in_plane_bending")
    
    if theta <= 150:
        KtTheta = 1.11*Ktu - (0.0275 + 0.1125 * (theta/150)**4)*Ktu**2
    else:
        KtTheta = 1e3
    
    Kt = min(Ktu, KtTheta)
    
    return Kt
        
    
def two_v_notches_rect_section(h: float, r: float, D: float, theta: float) -> float:
    """_summary_
    See Roark 7th Edition Table 17.1.2

    Args:
        h (float): _description_
        r (float): _description_
        D (float): _description_
        theta (float): _description_

    Returns:
        float: _description_
    """
    ratio = 2*h/D
    Ktu = two_u_notches_rect_section(h,r,D, loadtype="axial_tension")
    
    if ratio == 0.4 and theta <= 120:
        KtTheta = 1.11*Ktu - (0.0275 + 0.000145*theta + 0.00164 * (theta/120)**8)*Ktu**2
    elif ratio == 0.667 and theta <= 120:
        KtTheta = 1.11*Ktu - (0.0275 + 0.00042*theta + 0.0075 * (theta/120)**8)*Ktu**2
    else:
        KtTheta = 1e3
    
    Kt = min(Ktu, KtTheta)
    return Kt
