from abc import ABC, abstractmethod
import numpy as np

class cross_section_general(ABC):
    A: float
    Ix: float
    Iy: float
    
    
class rectangle(cross_section_general):
    
    def __init__(self, b:float, h:float):
        self.b = b
        self.h = h
        self.A = self.b * self.h
        self.Ix = self.b*self.h**3/12
        self.Iy = self.b**3*self.h/12

class circle(cross_section_general):
    
    def __init__(self, D:float):
        self.D = D
        self.A = np.pi*self.D**2/4
        self.Ix = np.pi*self.D**4/64
        self.Iy = self.Ix()
    
class circle_tube(cross_section_general):
    
    def __init__(self, D:float, d:float):
        self.D = D
        self.d = d
        self.A = np.pi*(self.D**2- self.d**2)/4
        self.Ix = np.pi*(self.D**4- self.d**4)/64
        self.Iy = self.Ix()
    