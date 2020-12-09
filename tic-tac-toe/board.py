# author: Diana Martinez
# date: 11/08/2020
# file: board.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board
class Board:

    def __init__(self):
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        self.winner = ""

    def get_size(self):
        return self.size

    def get_winner(self):
        return self.winner

    def set(self, placeholder, sign):
        self.board[placeholder] = sign

    def isEmpty(self, placeholder):
        if self.board[placeholder] == " ":
            return True
        else:
            return False

    def isdone(self):
        done = False
        for index in range(0, 3):
            if self.board[index] == self.board[index + 1] and self.board[index + 1] == self.board[index + 2] and self.board[index + 2] in ["X", "O"]:
                self.winner = self.board[index]
                done = True
        for index in range(0, 3):
            if self.board[index] == self.board[index + 3] and self.board[index + 3] == self.board[index + 6] and self.board[index + 6] in ["X", "O"]:
                self.winner = self.board[index]
                done = True
        if self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[8] in ["X", "O"]:
            winner = self.board[0]
            done = True
        if self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[6] in ["X", "O"]:
            winner = self.board[2]
            done = True
        return done

    def show(self):
        indent = 0
        print("   A   B   C")
        for index in range(0, 3):
            print(" +---+---+---+\n{}|".format(index + 1), end=" ")
            for k in range(0, 3):
                print("{} |".format(self.board[indent]), end=" ")
                indent = indent + 1
            print()
        print(" +---+---+---+")