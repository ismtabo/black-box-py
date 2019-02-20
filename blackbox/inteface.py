class CLIInterface:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = None

    def ask_game_mode(self):
        game_mode = input("Elija modo de juego (p para modo de pruebas): ")
        return game_mode

    def run(self):
        # choose game mode
        # game mode = self.ask_game_mode()
        game_mode = self.ask_game_mode()

        # if test mode ask for initial positions
        if game_mode in "pP":
            initial_positions = self.ask_initial_positions()
        else:
            initial_positions = []

        # initalizate game
        # self.game = create_game(initial positions)

        # play loop
        continue_play = True

        while continue_play:
            # game loop
            game_finished = False

            while not game_finished:
                # ask and validate turn play
                turn_row, turn_col = self.ask_turn()

                # update state of game
                # self.game.update(turn_row, turn_col)

                # show game state
                # self.show_game()

            # ask  to play again
            # play_again = self.ask_play_again()
        pass
