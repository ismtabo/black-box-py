from copy import copy
class Table:
        # recive 2 parameters, the lenght and the whidth
    def __init__(self, size_x, size_y):
        self._size_x = size_x
        self._size_y = size_y
        self.p = self.create_table()

    # generate the table 
    def create_table(self):
        return [[0 for x in range(self._size_y)]for x in range(self._size_x)]

    # provisional process that make easy to see how works
    def print_table(self):

        for i in self.p:
            print(i)
        print("\n")

    # Process whit you can include an element on a part of the table
    def add_element(self,coordenate_y, coordenate_x, value):
        self.p[coordenate_x][coordenate_y] = value

    # obtein the element inside the coordenates (y,x)
    def get_element(self, coordenate_y, coordenate_x):
        return  self.p[coordenate_x][coordenate_y]


    # function with can know if the coordenate are in the table
    # movement is a list where there are firt de coordenate y and then the coordenate x

    def in_table(self, movement):
        coordenate_x = movement[1] - 1
        coordenate_y = movement[0] - 1 
        if (coordenate_x > self._size_x) or (coordenate_x < 0):
            raise Exception(" Coordenate X out of range")
        
        if (coordenate_y > self._size_y) or (coordenate_y < 0):
            raise Exception(" Coordenate X out of range")

        return True