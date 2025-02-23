from abc import ABC, abstractmethod
import numpy as np

class cross_section_general(ABC):
    
    @abstractmethod
    def A(self) -> float:
        return
    
    def Ix(self) -> float:
        return
    
    def Iy(self) -> float:
        return
    
    
class rectangle(cross_section_general):
    
    def __init__(self, b:float, h:float):
        self.b = b
        self.h = h
        super().__init__()
    
    def A(self):
        return self.b * self.h
    
    def Ix(self):
        return self.b*self.h**3/12
    
    def Iy(self):
        return self.b**3*self.h/12

class circle(cross_section_general):
    
    def __init__(self, D:float):
        self.D = D
        super().__init__()
    
    def A(self):
        return np.pi*self.D**2/4
    
    def Ix(self):
        return np.pi*self.D**4/64
    
    def Iy(self):
        return self.Ix()
    
class circle_tube(cross_section_general):
    
    def __init__(self, D:float, d:float):
        self.D = D
        self.d = d
        super().__init__()
    
    def A(self):
        return np.pi*(self.D**2- self.d**2)/4
    
    def Ix(self):
        return np.pi*(self.D**4- self.d**4)/64
    
    def Iy(self):
        return self.Ix()