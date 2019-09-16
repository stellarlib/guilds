

class Map(object):

    def __init__(self):

        self.cells = {}
        self.level = 1

    def artifact_bonus(self):
        return self.level

    def add_cell(self, cell):
        self.cells[cell.coord.coord] = cell

    def get_cell(self, coord):
        return self.cells.get(coord, None)

    def all_cells(self):
        return self.cells.values()
