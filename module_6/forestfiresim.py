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

from constants import (
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
    print("This program requires the bext module, which you")
    print("can install by following the instructions at")
    print("https://pypi.org/project/Bext/")
    sys.exit(1)


@dataclass
class Forest:
    """
    A forest grid for the simulation.

    This class represents a grid of cells, each of which can be in one of three states:

    - TREE: A tree cell.
    - FIRE: A fire cell.
    - EMPTY: An empty cell.

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
    def create_new(cls, width: int, height: int) -> "Forest":
        """
        Create and initialize a new forest grid with random tree placement.

        A new Forest instance is returned with each cell set to TREE or EMPTY based on
        the initial tree density probability.

        Parameters:
            - width: Width of the forest grid.
            :type width: int

            - height: Height of the forest grid.
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
        return forest

    def display(self) -> None:
        """
        Renders the current state of the forest grid to the terminal using
        ANSI color codes.

        Displays trees in green, fires in red, and empty spaces in the default color.
        Also prints simulation parameters and user instructions below the grid.
        """
        output: list[str] = []
        for y in range(self.height):
            line_parts: list[str] = []
            for x in range(self.width):
                cell = self.cells.get((x, y), EMPTY)
                if cell == TREE:
                    line_parts.append("\x1b[32m" + TREE + "\x1b[0m")  # Green
                elif cell == FIRE:
                    line_parts.append("\x1b[31m" + FIRE + "\x1b[0m")  # Red
                else:
                    line_parts.append(EMPTY)
            output.append("".join(line_parts))

        status_line = (
            f"Grow chance: {GROW_CHANCE * 100:.0f}%  "
            f"Lightning chance: {FIRE_CHANCE * 100:.0f}%  "
            "Press Ctrl-C to quit."
        )
        output.append(status_line)

        print("\n".join(output), end="\r")

    def _has_burning_neighbor(self, x: int, y: int) -> bool:
        """
        Returns True if at least one of the eight neighboring cells around (x, y) is on
        fire; otherwise returns False.

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
            if (
                0 <= nx < self.width
                and 0 <= ny < self.height
                and self.cells.get((nx, ny), EMPTY) == FIRE
            ):
                return True
        return False

    def _spread_fire_to_neighbors(
        self, center_x: int, center_y: int, cells_to_update: dict[Position, CellState]
    ) -> None:
        """
        Marks all neighboring tree cells of the specified cell to be set on
        fire in the next simulation step.

        Parameters:
            - center_x: X coordinate of the cell currently on fire.
            :type center_x: int

            - center_y: Y coordinate of the cell currently on fire.
            :type center_y: int

            - cells_to_update: Dictionary tracking cells that will change state
            in the next update.
            :type cells_to_update: dict[Position, CellState]
        """
        for delta_x, delta_y in self._get_neighbors():
            neighbor_x, neighbor_y = center_x + delta_x, center_y + delta_y
            if (
                0 <= neighbor_x < self.width
                and 0 <= neighbor_y < self.height
                and self.cells.get((neighbor_x, neighbor_y), EMPTY) == TREE
            ):
                cells_to_update[(neighbor_x, neighbor_y)] = FIRE

    def step(self) -> None:
        """
        Advances the forest simulation by one time step.

        Updates all cell states based on growth, fire spread, and burning rules.
        """
        new_cells: dict[Position, CellState] = {}

        for x in range(self.width):
            for y in range(self.height):
                pos = (x, y)
                current = self.cells.get(pos, EMPTY)
                # Ensure current is a valid CellState
                current_state: CellState = (
                    current if current in (TREE, FIRE, EMPTY) else EMPTY
                )
                new_state = self._determine_new_cell_state(x, y, current_state)
                new_cells[pos] = new_state
                if new_state == FIRE:
                    self._spread_fire_to_neighbors(x, y, new_cells)

        # Update cells with new states
        self.cells.update(new_cells)  # type: ignore[arg-type]

    def _determine_new_cell_state(
        self, x: int, y: int, current: CellState
    ) -> CellState:
        """
        Determines the next state of a cell based on its current state and the
        states of neighboring cells.

        A cell may grow a tree, catch fire due to lightning or nearby fire, or
        become empty after burning.

        Parameters:
            - x: X coordinate of the cell.
            :type x: int

            - y: Y coordinate of the cell.
            :type y: int

            - current: The current state of the cell.
            :type current: CellState

        Returns:
            - CellState: The new state of the cell (TREE, FIRE, or EMPTY).
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
        Returns relative coordinate offsets for all 8 neighboring cells in a 2D grid.

        Returns:
            - A list of (dx, dy) tuples representing the positions of all 8
            adjacent neighbors surrounding a cell.
            :rtype: list[tuple[int, int]]
        """
        return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


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
        print("\nForest Fire Simulation, by Al Sweigart")  # noqa: SC100
        print("Modified by Sue Sampson")
        print("Refactored by Brittaney Perry-Morgan")
        sys.exit()  # When Ctrl-C is pressed, end the program.


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
