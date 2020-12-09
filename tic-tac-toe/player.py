# author: Diana Martinez
# date: 11/08/2020
# file: player.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board
class Player:

    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def get_sign(self):
        return self.sign

    def get_name(self):
        return self.name

    def choose(self, board):
        while True:
            cell = input("{},{}: Enter a cell [A-C][1-3]: ".format(self.get_name(), self.get_sign()))
            index = (3 * int(cell[1])) + (ord(cell[0]) - 65) - 3
            if 0 <= index < 9 and board.isEmpty(index):
                board.set(index, self.get_sign())
                break
            else:
                print("You did not choose correctly")