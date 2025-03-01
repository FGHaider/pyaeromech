[<img src="https://img.shields.io/badge/Status-In Development-orange.svg?logo=LOGO">](<LINK>)

# pyaeromech
Python package implementating basic analytical functions focused on mechanical engineering for aerospace applications. Utilizing ESA and NASA standards for reference. 

The goal of the package is to provide the basics, no FE just some of the more fundamental formulas, parts and equations. Neatly packaged and verified so you can focus on the goal of project rather than doublechecking someone did not mess up the definition of margin of safety.

## Functionality

- Basics
- Geometry
- Vibrations
- Concentrations
- Components
    - Beams
    - Fasteners
    - Springs

### Basics

The basics include some standard material data, this data is intended for simple comparisons.

#### Margin of Safety

```python
from pyaeromech.basics import ms

margin = ms(load = 500, limit = 1000, sf = 1.25)
```

## Dependencies
- Numpy
- Scipy