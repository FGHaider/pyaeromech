import numpy as np
from exceptions import UnknownType

#PARAMETRIC STUDIES ON THE EFFECT OF
#FOUR TYPES OF FASTENER MODELING IN
#CHANNEL TYPE TENSION FITTING
# Siddabathuni et.al

def swift(d:float, Ef:float, t1:float, E1:float, t2:float, E2:float) -> float:
    return 5/(d*Ef) + 0.8*(1/(t1*E1) + 1/(t2*E2))

def tate_rosenfeld(d:float, Ef:float, t1:float, E1:float, t2:float, E2:float, vf:float) -> float:
    term_1 = 32/(9*Ef*np.pi*d**2)*(1+vf)*(t1+t2)
    term_2 = 8/(5*Ef*np.pi*d**4)*(t1**3 + 5*t1**2*t2 + 5*t1*t2**2 + t2**3)
    return 1/(t1*Ef) + 1/(t2*Ef) + 1/(t1*E1) + 1/(t2*E2) + term_1 + term_2

def huth(d:float, Ef:float, t1:float, E1:float, t2:float, E2:float, shear_type:str, joint_type:str) -> float:
    
    match shear_type:
        case "single_shear":
            n = 1
        case "double_shear":
            n = 2
        case _:
            UnknownType("Only single or double shear are valid options")
    
    match joint_type:
        case "bolted_metallic":
            a, b = 2/3, 3.0
        case "riveted_metallic":
            a, b = 2/5, 2.2
        case "bolted_epoxy":
            a, b = 2/3, 4.2
        case _:
            UnknownType(f"The joint type {joint_type} is unknown")
    
    return ((t1 + t2)/(2*d))**a * b/n * (1/(t1*E1) + 1/(n*t2*E2) + 1/(2*t1*Ef) + 1/(2*n*t2*Ef))

def grumman(d, Ef, t1, E1, t2, E2) -> float:
    return (t1 + t2)**2/(Ef*d**3) + 3.7*(1/(t1*E1) + 1/(t2*E2))