import pytest
from pyaeromech.concentrations import rectangular_bar_with_fillet
from pyaeromech.exceptions import OutsideRange

def test_rectangular_bar_with_fillet():
    with pytest.raises(OutsideRange):
        rectangular_bar_with_fillet(D=100, d=200, r=10)