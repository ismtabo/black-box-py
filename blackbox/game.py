from .table import Table
from random import randint
# var size_x and size_y are determinate of the size of the table

class Game:
    # recive 3 parameters, the lenght, the whidth, and the number of mirors
    def __init__(self, size_x, size_y, mirors):
        self._mirors = mirors
        self._size_x = size_x
        self._size_y = size_y
        self.table = Table(size_x,size_y)
        self.put_mirors()


    # Provisional process to see the table how it works
    def print_table(self):
        self.table.print_table()


    def put_mirors(self):
        i = 0
        while i < self._mirors:
            coordenate_x = randint(0, self._size_x - 1)
            coordenate_y = randint(0, self._size_y - 1)
            print (coordenate_x)
            print (coordenate_y)
            if self.table.get_element(coordenate_y,coordenate_x) != 1:
                self.table.add_element(coordenate_y,coordenate_x, 1)
                i+=1
            
