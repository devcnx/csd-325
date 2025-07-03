"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 29th, 2025
Assignment: Module 6.2 Forest Fire Simulation: Program and Revised Flowchart
Purpose: A program that simulates a forest fire.

This module contains the modified version of `forestfiresim.py` from Module 5.2.
The main difference is that it now includes a lake in the center of the display.
The lake cannot be modified once it is placed. The lake acts as a firebreak that flames
cannot cross.

Modifications include:
    - Adding a lake roughly in the center of the display.
    - The water feature uses '~' (tilde) as its character and is displayed in blue.
    - The water feature cannot be modified once it is in place.
        - It acts as a firebreak that flames cannot cross.
"""
import random
import sys
import time
from dataclasses import dataclass, field
from module_6.constants import (
            CellState,
            EMPTY,
            FIRE,
            FIRE_CHANCE,
            GROW_CHANCE,
            HEIGHT,
            INITIAL_TREE_DENSITY,
            LAKE,
            PAUSE_LENGTH,
            TREE,
            WIDTH,
        )

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
        Create and initialize a new forest grid with random tree placement.

        Parameters:
            - width: The width of the forest.
            :type width: int

            - height: The height of the forest.
            :type height: int

        Returns:
            - A new Forest object with randomly initialized cell states.
            :rtype: Forest
        """
        forest = cls(width, height)
        forest.cells = {
            (x, y): TREE if random.random() <= INITIAL_TREE_DENSITY else EMPTY
            for x in range(width)
            for y in range(height)
        }
        lake_width = width // 4
        lake_height = height // 4
        lake_start_x = (width - lake_width) // 2
        lake_start_y = (height - lake_height) // 2
        for x in range(lake_start_x, lake_start_x + lake_width):
            for y in range(lake_start_y, lake_start_y + lake_height):
                forest.cells[(x, y)] = LAKE
        return forest

    def display(self) -> None:
        """
        Renders the current state of the forest grid to the terminal using ANSI color codes.

        Returns:
            - None
        """
        output: list[str] = []
        for y in range(self.height):
            line_parts: list[str] = []
            for x in range(self.width):
                cell = self.cells.get((x, y), EMPTY)
                if cell == TREE:
                    line_parts.append('\x1b[32m' + TREE + '\x1b[0m')  # Green
                elif cell == FIRE:
                    line_parts.append('\x1b[31m' + FIRE + '\x1b[0m')   # Red
                elif cell == LAKE:
                    # Display the lake as blue '~'
                    line_parts.append('\x1b[34m~\x1b[0m')  # Blue water
                else:
                    line_parts.append('\x1b[0m' + EMPTY)
            output.append(''.join(line_parts))
        status_line = (f'Grow chance: {GROW_CHANCE * 100:.0f}%  '
                       f'Lightning chance: {FIRE_CHANCE * 100:.0f}%  '
                       'Press Ctrl-C to quit.')
        output.append(status_line)
        print('\n'.join(output), end='\r')

    def _has_burning_neighbor(self, x: int, y: int) -> bool:
        """
        Parameters:
            - x: X coordinate of the cell.
            :type x: int

            - y: Y coordinate of the cell.
            :type y: int

        Returns:
            - True if any neighbor is burning, False otherwise.
            :rtype: bool
        """
        for dx, dy in self._get_neighbors():
            nx, ny = x + dx, y + dy
            if (0 <= nx < self.width and 0 <= ny < self.height
                    and self.cells.get((nx, ny), EMPTY) == FIRE):
                return True
        return False

    def _spread_fire_to_neighbors(self, center_x: int, center_y: int,
                                cells_to_update: dict[tuple[int, int], CellState]) -> None:
        """
        Marks all neighboring tree cells of the specified cell to be set on fire in the next simulation step.

        Parameters:
            - center_x: X coordinate of the cell.
            :type center_x: int

            - center_y: Y coordinate of the cell.
            :type center_y: int

            - cells_to_update: A dictionary of cells to update.
            :type cells_to_update: dict[tuple[int, int], CellState]
        """
        for delta_x, delta_y in self._get_neighbors():
            neighbor_x, neighbor_y = center_x + delta_x, center_y + delta_y
            if (0 <= neighbor_x < self.width and 0 <= neighbor_y < self.height and
                    self.cells.get((neighbor_x, neighbor_y), EMPTY) == TREE):
                cells_to_update[(neighbor_x, neighbor_y)] = FIRE

    def step(self) -> None:
        """
        Advances the forest simulation by one time step.
        """
        new_cells: dict[tuple[int, int], CellState] = {}
        for x in range(self.width):
            for y in range(self.height):
                pos = (x, y)
                current = self.cells.get(pos, EMPTY)
                # Accept any value for current_state
                current_state = current
                new_state = self._determine_new_cell_state(x, y, current_state)
                new_cells[pos] = new_state
                if new_state == FIRE:
                    self._spread_fire_to_neighbors(x, y, new_cells)
        self.cells.update(new_cells)

    def _determine_new_cell_state(
        self, x: int, y: int, current: CellState
    ) -> CellState:
        """
        Determines the next state of a cell based on its current state and the states of neighboring cells.
        """
        if current == LAKE:
            return LAKE
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
        Returns relative coordinate offsets for all 8 neighboring cells in a 2D grid.
        """
        return [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]


def main() -> None:
    """
    Starts and runs the interactive forest fire simulation loop.

    Initializes the forest, clears the terminal, and repeatedly displays the simulation
    state, advances the simulation by one step, and pauses between updates. Handles
    Ctrl-C to exit gracefully with credits.
    """
    forest = Forest.create_new(WIDTH, HEIGHT)
    bext.clear()

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
