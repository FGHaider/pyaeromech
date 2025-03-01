import pytest
from pyaeromech.cross_sections import rectangle, circle, circle_tube

def test_geometries():
    b = 10
    h = 20
    
    D = 10
    d = 5
    
    assert rectangle(b,h).A == 200