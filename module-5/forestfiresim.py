"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 22nd, 2025
Assignment: Module 5.2 Forest Fire Simulation: Program and Revised Flowchart
Purpose: To demonstrate proficiency in advanced Python programming.

A simulation of a forest fire spreading through a randomly generated forest.
Trees grow randomly and can be struck by lightning, which causes fires to spread.
"""

import random
import sys
import time
from dataclasses import dataclass, field
from typing import Final, Literal, TypeAlias, Dict, Tuple

# Type stubs for bext
try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit(1)

# Type aliases
CellState: TypeAlias = Literal['A', '@', ' ']
Position: TypeAlias = tuple[int, int]

# Constants
WIDTH: Final[int] = 79
HEIGHT: Final[int] = 22

# Cell states
TREE: Final[CellState] = 'A'
FIRE: Final[CellState] = '@'
EMPTY: Final[CellState] = ' '

# Simulation parameters
INITIAL_TREE_DENSITY: Final[float] = 0.20  # Amount of forest that starts with trees
GROW_CHANCE: Final[float] = 0.01  # Chance a blank space turns into a tree
FIRE_CHANCE: Final[float] = 0.01  # Chance a tree is hit by lightning & burns
PAUSE_LENGTH: Final[float] = 0.5  # Time between simulation steps in seconds

@dataclass
class Forest:
    """A forest simulation grid."""
    width: int
    height: int
    cells: Dict[Tuple[int, int], str] = field(default_factory=dict)

    @classmethod
    def create_new(cls, width: int, height: int) -> 'Forest':
        """Create a new forest with the given dimensions."""
        forest = cls(width, height)
        forest.cells = {
            (x, y): TREE if random.random() <= INITIAL_TREE_DENSITY else EMPTY
            for x in range(width)
            for y in range(height)
        }
        return forest

    def display(self) -> None:
        """Display the forest on the screen using ANSI color codes."""
        output: list[str] = []
        for y in range(self.height):
            line_parts: list[str] = []
            for x in range(self.width):
                cell = self.cells.get((x, y), EMPTY)
                if cell == TREE:
                    line_parts.append('\x1b[32m' + TREE + '\x1b[0m')  # Green
                elif cell == FIRE:
                    line_parts.append('\x1b[31m' + FIRE + '\x1b[0m')   # Red
                else:
                    line_parts.append(EMPTY)
            output.append(''.join(line_parts))
        print('\n'.join(output), end='\r')

    def step(self) -> None:
        """Advance the simulation by one step."""
        new_cells = {}

        for x in range(self.width):
            for y in range(self.height):
                pos = (x, y)
                current = self.cells.get(pos, EMPTY)

                if current == EMPTY and random.random() <= GROW_CHANCE:
                    new_cells[pos] = TREE
                elif current == TREE and random.random() <= FIRE_CHANCE:
                    new_cells[pos] = FIRE
                elif current == TREE:
                    # Check adjacent cells for fire
                    for dx, dy in self._get_neighbors():
                        nx, ny = x + dx, y + dy
                        if (0 <= nx < self.width and
                            0 <= ny < self.height and
                            self.cells.get((nx, ny), '') == FIRE):
                            new_cells[pos] = FIRE
                            break
                    else:
                        new_cells[pos] = TREE
                elif current == FIRE:
                    # This tree is currently burning
                    # Loop through all the neighboring spaces:
                    for dx, dy in self._get_neighbors():
                        nx, ny = x + dx, y + dy
                        if self.cells.get((nx, ny)) == TREE:
                            new_cells[(nx, ny)] = FIRE
                    # The tree has burned down now, so erase it:
                    new_cells[pos] = EMPTY
                else:
                    # Just copy the existing object:
                    new_cells[pos] = current

        self.cells.update(new_cells)

    @staticmethod
    def _get_neighbors() -> list[tuple[int, int]]:
        """Return relative coordinates of all 8 neighboring cells."""
        return [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

def main() -> None:
    """Run the forest fire simulation."""
    forest = Forest.create_new(WIDTH, HEIGHT)
    bext.clear()

    try:
        while True:  # Main program loop
            forest.display()
            forest.step()
            time.sleep(PAUSE_LENGTH)
    except KeyboardInterrupt:
        print('\nForest Fire Simulation, by Al Sweigart')
        print('Modified by Sue Sampson')
        print('Refactored by Brittaney Perry-Morgan')
        sys.exit()  # When Ctrl-C is pressed, end the program.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
