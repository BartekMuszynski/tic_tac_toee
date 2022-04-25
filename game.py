import time
class tictactoe :

    def __init__(self):
        self.gboard = ["" for _ in range(9)]
        self.used_sqares = []


    def win_check(self):
        x_win = ["x", "x", "x"]
        o_win = ["o", "o", "o"]
        if self.gboard[0:3] == x_win or self.gboard[0:3] == o_win:
            return True
        if self.gboard[3:6] == x_win or self.gboard[3:6] == o_win:
            return True
        if self.gboard[6:9] == x_win or self.gboard[6:9] == o_win:
            return True
        if self.gboard[0::4] == x_win or self.gboard[0::4] == o_win:
            return True
        if self.gboard[2:7][0::2] == x_win or self.gboard[2:7][0::2] == o_win:
            return True
        if self.gboard[0::3] == x_win or self.gboard[0::3] == o_win:
            return True
        if self.gboard[2::3] == x_win or self.gboard[2::3] == o_win:
            return True
        if self.gboard[1::3] == x_win or self.gboard[1::3] == o_win:
            return True




    def char_choice(self):
        while True :
            try :
                self.user1_move = str(input("Player 1 please chose 'x' or 'o': ").lower())
                assert  self.user1_move == "x" or self.user1_move == "o"
                if self.user1_move == "x":
                    self.user2_move = "o"
                else:
                    self.user2_move = "x"
                return self.user1_move, self.user2_move
            except AssertionError:
                print("Thats not an 'x' or 'o'. Try again !")
                continue

    def square_choice(self):
        while True :
            try:
                self.user_square = int(input(" Player 1 please chose your square: "))
                assert self.user_square not in self.used_sqares
                self.used_sqares.append(self.user_square)
                self.gboard[self.user_square] = self.user1_move
                print(self.gboard[0:3])
                print(self.gboard[3:6])
                print(self.gboard[6:9])
                break
            except AssertionError:
                print("This square has arleady been chosen")
                continue
            except IndexError:
                print("This square is out of range")
                continue
            except ValueError:
                print("That a string !")
                continue
    def squaree_choice(self):
        while True :
            try:
                self.user_square = int(input(" Player 2 please chose your square: "))
                assert self.user_square not in self.used_sqares
                self.used_sqares.append(self.user_square)
                self.gboard[self.user_square] = self.user2_move
                print(self.gboard[0:3])
                print(self.gboard[3:6])
                print(self.gboard[6:9])
                break
            except AssertionError:
                print("This square has arleady been chosen")
                continue
            except IndexError:
                print("This square is out of range")
                continue
            except ValueError:
                print("That's a string !")
                continue


    def game(self):
        lsy = [f"{_}" for _ in range(9)]
        print(lsy[0:3])
        print(lsy[3:6])
        print(lsy[6:9])
        tictactoe.char_choice(self)
        while True :
            tictactoe.square_choice(self)
            if tictactoe.win_check(self) == True :
                print("Player 1 won")
                break
            if len(self.used_sqares) == 9 and tictactoe.win_check(self) != True :
                print("Thats a draw.")
                break
            tictactoe.squaree_choice(self)
            if tictactoe.win_check(self) == True:
                print("Player 2 won")
                break
            if len(self.used_sqares) == 9 and tictactoe.win_check(self) != True :
                print("Thats a draw.")
                break




a = tictactoe().game()
time.sleep(10)

