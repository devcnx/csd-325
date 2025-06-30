"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 29th, 2025
Assignment: Module 6.2 Forest Fire Simulation Project: Revised Flowchart
Purpose: To demonstrate proficiency in advanced Python programming.

A simulation of a forest fire spreading through a randomly generated forest.
Trees grow randomly and can be struck by lightning, which causes fires to spread.
"""
import random
import sys
import time
from .constants import (
    CellState,
    EMPTY,
    FIRE,
    FIRE_CHANCE,
    GROW_CHANCE,
    HEIGHT,
    INITIAL_TREE_DENSITY,
    PAUSE_LENGTH,
    TREE,
    WIDTH,
    Position,
)
from dataclasses import dataclass, field


try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit(1)


@dataclass
class Forest:
    """
    A forest simulation grid.

    Fields:
        - width: The width of the forest.
        :type width: int

        - height: The height of the forest.
        :type height: int

        - cells: A dictionary of cell positions and their states.
        :type cells: dict[tuple[int, int], CellState]
    """

    width: int
    height: int
    cells: dict[tuple[int, int], CellState] = field(default_factory=dict)

    @classmethod
    def create_new(cls, width: int, height: int) -> 'Forest':
        """
        Create a new forest with the given dimensions.

        Parameters:
            width: The width of the forest.
            :type width: int

            height: The height of the forest.
            :type height: int

        Returns:
            A new Forest object with the given dimensions.
            :rtype: Forest
        """
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

        status_line = (f'Grow chance: {GROW_CHANCE * 100:.0f}%  '
                       f'Lightning chance: {FIRE_CHANCE * 100:.0f}%  '
                       'Press Ctrl-C to quit.')
        output.append(status_line)

        print('\n'.join(output), end='\r')

    def _has_burning_neighbor(self, x: int, y: int) -> bool:
        """
        Check if any neighbor cell is on fire.

        Parameters:
            x: X coordinate of the cell
            :type x: int

            y: Y coordinate of the cell
            :type y: int

        Returns:
            True if any neighbor cell is on fire, False otherwise.
            :rtype: bool
        """
        for dx, dy in self._get_neighbors():
            nx, ny = x + dx, y + dy
            if (0 <= nx < self.width and 0 <= ny < self.height
                    and self.cells.get((nx, ny), EMPTY) == FIRE):
                return True
        return False

    def _spread_fire_to_neighbors(self, center_x: int, center_y: int,
                                  cells_to_update: dict[Position, CellState]) -> None:
        """
        Spread fire to neighboring trees.

        Parameters:
            center_x: X coordinate of the center cell
            :type center_x: int

            center_y: Y coordinate of the center cell
            :type center_y: int

            cells_to_update: Dictionary of cells to update
            :type cells_to_update: dict[Position, CellState]
        """
        for delta_x, delta_y in self._get_neighbors():
            neighbor_x, neighbor_y = center_x + delta_x, center_y + delta_y
            if (0 <= neighbor_x < self.width and 0 <= neighbor_y < self.height and
                    self.cells.get((neighbor_x, neighbor_y), EMPTY) == TREE):
                cells_to_update[(neighbor_x, neighbor_y)] = FIRE

    def step(self) -> None:
        """Advance the simulation by one step."""
        new_cells: dict[Position, CellState] = {}

        for x in range(self.width):
            for y in range(self.height):
                pos = (x, y)
                current = self.cells.get(pos, EMPTY)
                # Ensure current is a valid CellState
                current_state: CellState = current if current in (TREE, FIRE, EMPTY) \
                    else EMPTY
                new_state = self._determine_new_cell_state(x, y, current_state)
                new_cells[pos] = new_state
                if new_state == FIRE:
                    self._spread_fire_to_neighbors(x, y, new_cells)

        # Update cells with new states
        self.cells.update(new_cells)  # type: ignore[arg-type]

    def _determine_new_cell_state(self, x: int, y: int,
                                  current: CellState) -> CellState:
        """
        Determine the new state of a cell based on its current state and neighbors.

        Parameters:
            x: X coordinate of the cell
            :type x: int

            y: Y coordinate of the cell
            :type y: int

            current: Current state of the cell (must be TREE, FIRE, or EMPTY)
            :type current: CellState

        Returns:
            The new state of the cell (TREE, FIRE, or EMPTY)
            :rtype: CellState
        """
        if current == EMPTY:
            return TREE if random.random() <= GROW_CHANCE else EMPTY

        if current == TREE:
            if random.random() <= FIRE_CHANCE or self._has_burning_neighbor(x, y):
                return FIRE
            return TREE

        return EMPTY if current == FIRE else current

    @staticmethod
    def _get_neighbors() -> list[tuple[int, int]]:
        """
        Return relative coordinates of all 8 neighboring cells.

        Returns:
            List of relative coordinates of all 8 neighboring cells.
            :rtype: list[tuple[int, int]]
        """
        return [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]


def main() -> None:
    """Run the forest fire simulation."""
    forest = Forest.create_new(WIDTH, HEIGHT)
    bext.clear()  # type: ignore[no-untyped-call]

    try:
        while True:  # Main program loop
            forest.display()
            forest.step()
            time.sleep(PAUSE_LENGTH)
    except KeyboardInterrupt:
        print('\nForest Fire Simulation, by Al Sweigart')  # noqa: SC100
        print('Modified by Sue Sampson')
        print('Refactored by Brittaney Perry-Morgan')
        sys.exit()  # When Ctrl-C is pressed, end the program.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
