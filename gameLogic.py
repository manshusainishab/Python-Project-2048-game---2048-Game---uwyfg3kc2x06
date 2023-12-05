import random


class GameLogic:
    def __init__(self):
        self._board = [[0] * 4 for _ in range(4)]
        self._score = 0
        self._won = False
        self._over = False

    def initialise_board(self):
        self._board = [[0] * 4 for _ in range(4)]
        self._score = 0
        self._won = False
        self._over = False
        self._place_random()
        self._place_random()

    def _place_random(self):
        # complete this function as per question text
        # randomly places a 2 or 4 in an empty block
        pass

    def handle_placement_if_not_game_over(self):
        if self._check_if_game_over():
            self._over = True
        elif self._check_if_game_won():
            self._won = True
        else:
            self._place_random()
        self._check_if_game_over()
        self._check_if_game_won()

    # movement functions
    # do not remove this function it is used for testing purposes
    def only_move_left(self):
        # handle all the logic for left movement as
        # described in the question text
        pass

    def is_left_move_possible(self):
        pass

    # do not remove this function it is used for testing purposes
    def capture_move_left(self):
        if not self.is_left_move_possible():
            return
        self.only_move_left()

        self.handle_placement_if_not_game_over()

    def only_move_right(self):
        # handle all the logic for right movement as
        # described in the question text
        pass

    def is_right_move_possible(self):
        pass

    # do not remove this function it is used for testing purposes
    def capture_move_right(self):
        if not self.is_right_move_possible():
            return
        self.only_move_right()

        self.handle_placement_if_not_game_over()

    # do not remove this function it is used for testing purposes
    def only_move_up(self):
        # handle all the logic for up movement as
        # described in the question text
        pass

    def is_up_move_possible(self):
        pass

    # do not remove this function it is used for testing purposes
    def capture_move_up(self):
        if not self.is_up_move_possible():
            return
        self.only_move_up()

        self.handle_placement_if_not_game_over()

    # do not remove this function it is used for testing purposes
    def only_move_down(self):
        # handle all the logic for down movement as
        # described in the question text
        pass

    def is_down_move_possible(self):
        pass

    # do not remove this function it is used for testing purposes
    def capture_move_down(self):
        if not self.is_down_move_possible():
            return
        self.only_move_down()

        self.handle_placement_if_not_game_over()

    # do not remove this function it is used for testing purposes
    # also used for proper functioning of the game
    def get_score(self):
        return self._score

    # do not remove this function it is used for testing purposes
    def get_current_board(self):
        return self._board

    # do not remove this function it is used for testing purposes
    # also used for proper functioning of the game
    def get_won(self):
        return self._won

    # do not remove this function it is used for testing purposes
    # also used for proper functioning of the game
    def get_over(self):
        return self._over

    def _check_if_game_won(self):
        # complete this function to check if game has reached the winning condition
        # the condition for winning is given in the question text
        pass

    def _check_if_game_over(self):
        # complete this function to check if game has reached the losing condition
        # the condition for losing is given in the question text
        pass

    # functions to aid testing
    def set_board(self, board):
        self._board = board
