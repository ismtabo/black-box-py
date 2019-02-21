from blackbox import Game

if __name__ == "__main__":
    
    game = Game(10,15,2)
    game.table.create_table()
    game.table.add_element(1,5,10)
    game.table.print_table()
    