from .table import Table

# var size_x and size_y are determinate of the size of the table

class Game:
    def __init__(self, size_x, size_y, mirors):
        self.__mirors = mirors
        self._size_x = size_x
        self._size_y = size_y
        self.table = Table(size_x,size_y,mirors)

    def print_table(self):
        self.table.print_table()