class Table:
    def __init__(self, size_x, size_y,mirors):
        self._size_x = size_x
        self._size_y = size_y
        self.mirors = mirors
        self.p = 0



    def create_table(self):
        self.p=[[0 for x in range(self._size_y)]for x in range(self._size_x)]

    def print_table(self):

        for i in self.p:

                    print(i)
        print("\n")

    def add_element(self,coordenate_y, coordenate_x, value):
        self.p[coordenate_y][coordenate_x] = value


    def in_table(self, movement):
        coordenate_x = movement[1]
        coordenate_y = movement[0]
        if (coordenate_x > self._size_x) or (coordenate_x < 0):
            raise Exception(" Coordenate X out of range")
        
        if (coordenate_y > self._size_y) or (coordenate_y < 0):
            raise Exception(" Coordenate X out of range")

        return True