[<img src="https://img.shields.io/badge/Status-In Development-orange.svg?logo=LOGO">](<LINK>)

# pyaeromech
Python package implementating basic analytical functions focused on mechanical engineering for aerospace applications.  Utilizing ESA and NASA standards for reference. 

## Subpackages

- Basics
- Beams
- Geometry
- Fasteners
- Vibrations

### Basics

#### Margin of Safety

```python
from pyaeromech.basics import ms

margin = ms(load = 500, limit = 1000, sf = 1.25)
```

## Dependencies
- Numpy
- Scipy