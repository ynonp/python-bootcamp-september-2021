from PlayerBase import *


class HumanPlayer(PlayerBase):
    def __init__(self, name: str, symbol: str, board: Board):
        PlayerBase.__init__(self, name, symbol, board)

    def get_cell_from_user(self) -> tuple:
        # I would write:
        # user_input = input("please enter your next step (row,col)")
        # pos = [int(i) for i in user_input.split(',')]
        # return pos

        # Also - input validation would be nice here
        tpl = input("please enter your next step (row,col)").split(',')
        return int(tpl[0]), int(tpl[1])

    def next_step(self) -> Tuple:
        pos = self.get_cell_from_user()
        while not self.bord.can_choose_this_cell(pos):
            pos = self.get_cell_from_user()
        return pos

# hp = HumanPlayer("Amiel Cohen Player", 'X')
# print(hp.name)
# print(hp.next_step())
