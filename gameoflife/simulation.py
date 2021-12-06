from .pattern import Pattern, Cell, Point


class Simulation:
    def __init__(self, pattern: Pattern = Pattern(), coord: Point = Point(0, 0)):
        self.pattern = Pattern()
        self.add_pattern(pattern, coord)

    def make_step(self) -> None:
        counter_dict = {} # dictionary that stores number of neighbours of concrete cell
        # fill in dictionary
        for cell in self.pattern.cells:
            #check nearest cells
            for nearest in Simulation.get_surrounding_cells(cell):
                if nearest in counter_dict:
                    counter_dict[nearest] += 1
                else:
                    counter_dict[nearest] = 1
            # include cell in dictionary if it hasn't been yet, but with 0 neighbours
            if not cell in counter_dict:
                counter_dict[cell] = 0
        # apply rules according to data in the dictionary
        for cell, nbrs in counter_dict.items():
            if not self.is_alive(cell) and nbrs == 3:
                self.add_cell(cell)
            elif not (self.is_alive(cell) and (nbrs == 2 or nbrs == 3)):
                self.remove_cell(cell)

    @staticmethod
    def get_surrounding_cells(cell: Cell):
        yield Cell(cell.x, cell.y + 1)
        yield Cell(cell.x + 1, cell.y + 1)
        yield Cell(cell.x + 1, cell.y)
        yield Cell(cell.x + 1, cell.y - 1)
        yield Cell(cell.x, cell.y - 1)
        yield Cell(cell.x - 1, cell.y - 1)
        yield Cell(cell.x - 1, cell.y)
        yield Cell(cell.x - 1, cell.y + 1)

    def is_alive(self, cell: Cell) -> bool:
        return cell in self.pattern.cells

    def add_cell(self, cell: Cell) -> None:
        self.pattern.add_cell(cell)

    def add_pattern(self, pattern: Pattern, coord: Point = Point(0, 0)) -> None:
        for cell in pattern.cells:
            self.add_cell(Cell(coord.x + cell.x, coord.y + cell.y))

    def remove_cell(self, cell: Cell) -> None:
        self.pattern.remove_cell(cell)