
from abc import ABC, abstractmethod
import numpy as np

class Spring(ABC):
    
    def eigenfreq(self, m: float):
        return np.sqrt(self.constant()/m)
    
    @abstractmethod
    def constant():
        pass

class CompressionSpring(Spring):

    def constant(d: float, D: float, G: float, n: int):
        """_summary_

        Args:
            d (float): wire diameter
            D (float): mean coil diameter
            G (float): modulus of rigidity
            n (int): number of active coils, number of coils subject to flexure

        Returns:
            Estimate of spring constant
        """

        return G*d**4/(8*n*D**3)
    

class BellevilleSpring(Spring):
    pass