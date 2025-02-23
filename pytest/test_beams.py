import pytest
from aeromech.beams import euler_beam_buckling_load
from aeromech.exceptions import UnknownBoundary

def test_buckling():
    
    assert euler_beam_buckling_load(E=1, I=1, L=1, boundary="fixed_fixed") == 1.0
    with pytest.raises(UnknownBoundary):
        euler_beam_buckling_load(E=1, I=1, L=1, boundary="tricked")
        

