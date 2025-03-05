
import numpy as np
from pyaeromech.exceptions import OutsideRange

    
def Kt_calc(h, r, D, C):
    ratio = h/r
    coefficients = C[:,0] + C[:,1]*np.sqrt(ratio) + C[:,2]*ratio
    C1 = coefficients[0]
    C2 = coefficients[1]
    C3 = coefficients[2]
    C4 = coefficients[3]
    ratio = 2*h/D
    return C1 + C2*ratio + C3*ratio**2 + C4*ratio**3
        
def SquareShoulderFilletRectangularSection(L, D, r, h, loadtype):
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
    
    return Kt_calc(h, r, D, C)
        
    
def TwoUNotchesRectangularSection(h, r, D, loadtype):

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
    

    return Kt_calc(h, r, D, C)

    
def SingleUNotchRectangularSection(h, r, D, loadtype):
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
    
    return Kt_calc(h, r, D, C)
        
    
def SingleVNotchRectangularSection(h, r, D, theta):
    ratio = 2*h/D
    Ktu = SingleUNotchRectangularSection(h,r,D, loadtype="in_plane_bending")
    
    if theta <= 150:
        KtTheta = 1.11*Ktu - (0.0275 + 0.1125 * (theta/150)**4)*Ktu**2
    else:
        KtTheta = 1e3
    
    Kt = min(Ktu, KtTheta)
    
    return Kt
        
    
def TwoVNotchesRectangularSection(h, r, D, theta) -> None:

    ratio = 2*h/D
    Ktu = TwoUNotchesRectangularSection(h,r,D, loadtype="axial_tension")
    
    if ratio == 0.4 and theta <= 120:
        KtTheta = 1.11*Ktu - (0.0275 + 0.000145*theta + 0.00164 * (theta/120)**8)*Ktu**2
    elif ratio == 0.667 and theta <= 120:
        KtTheta = 1.11*Ktu - (0.0275 + 0.00042*theta + 0.0075 * (theta/120)**8)*Ktu**2
    else:
        KtTheta = 1e3
    
    Kt = min(Ktu, KtTheta)
    return Kt
        

def sigma_nom(M, t, d):

    return 6*M/(t*d**2)


def rectangular_bar_with_notches(w, h, r): # Does not seem to align with Roarks, seventh edition?
    """
    Source: 
    :param w:
    :param h:
    :param r:
    :return:
    """

    a_set = h/r
    Kt_set = np.empty(a_set.shape)

    for idx, a in enumerate(a_set):
        if 0.1 <= a <= 2.0:
            C1 = 1.024 + 2.092*np.sqrt(a) - 0.051*a
            C2 = -0.630 - 7.194*np.sqrt(a) + 1.288*a
            C3 = 2.117 + 8.574*np.sqrt(a) - 2.160*a
            C4 = -1.420 - 3.494*np.sqrt(a) + 0.932*a
        elif 2.0 <= a <= 50.0:
            C1 = 1.113 + 1.957*np.sqrt(a)
            C2 = -2.579 - 4.017*np.sqrt(a) - 0.013*a
            C3 = 4.100 + 3.922*np.sqrt(a) + 0.083*a
            C4 = -1.528 - 1.893*np.sqrt(a) - 0.066*a
        else:
            raise OutsideRange("Outside valid range")

        hw = h[idx]/w
        Kt_set[idx] = C1 + C2*(2*hw) + C3*(2*hw)**2 + C4*(2*hw)**3

    return Kt_set


def rectangular_single_notch_bending(h, D, r):
    """_summary_

    Args:
        h (_type_): _description_
        D (_type_): _description_
        r (_type_): _description_

    Raises:
        OutsideRange: _description_

    Returns:
        _type_: _description_
    """
    a_set = h/r
    Kt_set = np.empty(a_set.shape)

    for idx, a in enumerate(a_set):
        if a == 1:
            C1 = 2.988
            C2 = -7.735
            C3 = 10.674
            C4 = -4.927
        elif 0.5 <= a <= 4.0:
            C1 = 0.721 + 2.394*np.sqrt(a) - 0.127*a
            C2 = -0.426 - 8.827*np.sqrt(a) + 1.518*a
            C3 = 2.161 + 10.968*np.sqrt(a) - 2.455*a
            C4 = -1.456 - 4.535*np.sqrt(a) + 1.064*a
        else:
            raise OutsideRange("Outside valid range")

        hw = h[idx]/D
        Kt_set[idx] = C1 + C2*(2*hw) + C3*(2*hw)**2 + C4*(2*hw)**3

    return Kt_set


def rectangular_bar_with_fillet(D, d, r):
    """
    Source: 
    :param D:
    :param d:
    :param r:
    :return:
    """

    h = (D-d)/2

    if isinstance(r, np.ndarray):
        a_set = h/r
        Kt_set = np.empty(a_set.shape)

        for idx, a in enumerate(a_set):
            if 0.1 <= a <= 2.0:
                C1 = 1.007 + 1.000*np.sqrt(a) - 0.031*a
                C2 = -0.270 - 2.404*np.sqrt(a) + 0.749*a
                C3 = 0.677 + 1.133*np.sqrt(a) - 0.904*a
                C4 = -0.414 - 0.271*np.sqrt(a) + 0.186*a
            elif 2.0 <= a <= 20.0:
                C1 = 1.042 + 0.982*np.sqrt(a) - 0.036*a
                C2 = -3.599 + 1.619*np.sqrt(a) - 0.431*a
                C3 = 6.084 - 5.607*np.sqrt(a) + 1.158*a
                C4 = -2.527 + 3.006*np.sqrt(a) - 0.691*a
            else:
                raise OutsideRange("Outside valid range")
            hD = h/D
            Kt_set[idx] = C1 + C2*(2*hD) + C3*(2*hD)**2 + C4*(2*hD)**3
    else:
        a = h/r

        if 0.1 <= a <= 2.0:
            C1 = 1.007 + 1.000*np.sqrt(a) - 0.031*a
            C2 = -0.270 - 2.404*np.sqrt(a) + 0.749*a
            C3 = 0.677 + 1.133*np.sqrt(a) - 0.904*a
            C4 = -0.414 - 0.271*np.sqrt(a) + 0.186*a
        elif 2.0 <= a <= 20.0:
            C1 = 1.042 + 0.982*np.sqrt(a) - 0.036*a
            C2 = -3.599 + 1.619*np.sqrt(a) - 0.431*a
            C3 = 6.084 - 5.607*np.sqrt(a) + 1.158*a
            C4 = -2.527 + 3.006*np.sqrt(a) - 0.691*a
        else:
            raise OutsideRange("Outside valid range")
        hD = h/D
        Kt_set = C1 + C2*(2*hD) + C3*(2*hD)**2 + C4*(2*hD)**3

    return Kt_set
