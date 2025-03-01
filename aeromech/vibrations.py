
import numpy as np

class Miles:
    """_summary_
    https://femci.gsfc.nasa.gov/random/MilesEqn.html
    Args:
        fn (float): _description_
        Q (float): _description_
        ASD (float): _description_

    Returns:
        _type_: _description_
    """
    @staticmethod
    def Grms(fn: float, Q: float, ASD:float):
        return np.sqrt(np.pi/2*fn*Q*ASD)
    
    @staticmethod
    def Yrms(fn: float, Q: float, ASD:float):
        return np.sqrt(Q*ASD/(32*np.pi**3*fn**3))