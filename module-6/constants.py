# Type Aliases
from typing import Final, Literal, TypeAlias


CellState: TypeAlias = Literal['A', '@', ' ', '~']
Position: TypeAlias = tuple[int, int]

# Constants
WIDTH: Final[int] = 79
HEIGHT: Final[int] = 22

# Cell States
TREE: Final[CellState] = 'A'
FIRE: Final[CellState] = '@'
EMPTY: Final[CellState] = ' '
WATER: Final[CellState] = '~'

# Simulation Parameters
INITIAL_TREE_DENSITY: Final[float] = 0.20  # Amount of forest that starts with trees
GROW_CHANCE: Final[float] = 0.01  # Chance a blank space turns into a tree
FIRE_CHANCE: Final[float] = 0.01  # Chance a tree is hit by lightning & burns
PAUSE_LENGTH: Final[float] = 0.5  # Time between simulation steps in seconds
