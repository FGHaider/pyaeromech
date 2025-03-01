import pytest
from pyaeromech.beams import euler_beam_buckling_load
from pyaeromech.exceptions import UnknownBoundary

def test_buckling():
    
    assert euler_beam_buckling_load(E=1, I=1, L=1, boundary="fixed_fixed") == 39.47841760435743
    with pytest.raises(UnknownBoundary):
        euler_beam_buckling_load(E=1, I=1, L=1, boundary="tricked")
        

