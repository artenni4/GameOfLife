from dataclasses import dataclass


@dataclass(frozen=True)
class Cell:
    x: int
    y: int

Point = Cell # alias

class Pattern:
    def __init__(self, *cells: Cell):
        self.cells = set(cells)

    def add_cell(self, cell: Cell):
        self.cells.add(cell)

    def remove_cell(self, cell: Cell):
        try:
            self.cells.remove(cell)
        except KeyError:
            pass

# define some known patterns
class Patterns:
    glider: Pattern = Pattern(Cell(-2, 0), Cell(-1, 0), Cell(0, 0), Cell(0, 1), Cell(-1, 2))
    blinker: Pattern = Pattern(Cell(0, 1), Cell(0, 0), Cell(0, -1))
    block: Pattern = Pattern(Cell(0, 0), Cell(0, 1), Cell(1, 0), Cell(1, 1))
    acorn: Pattern = Pattern(Cell(-3, -1), Cell(-2, -1), Cell(1, -1), Cell(2, -1), Cell(3, -1), Cell(0, 0), Cell(-2, 1))
