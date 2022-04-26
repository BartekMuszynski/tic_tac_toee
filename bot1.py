import subprocess
import random
import pyautogui as gui
import time


class bot:

    def open(self):
        subprocess.call(["cmd", "/c", "start", "/max", "C:\\Users\\bartosz.muszynski\\PycharmProjects\\tic_tac_toe\\game.py"])


    def choice(self):
        self.a = random.choice(["x", "o"])
        if self.a == "x":
            self.b = "o"
        else:
            self.b = "x"
        return self.a, self.b

    def moves(self):
        mylist = [f"{_}" for _ in range(9)]
        a = random.sample(population=mylist, k=9)
        last_el = []
        for i in range(len(mylist)):
            gui.press("enter")
            gui.typewrite(a[i])
            last_el.append(a[i])
            if len(last_el) == 9:
                gui.press("enter")


    def game(self):
        bot.open(self)
        time.sleep(1)
        bot.choice(self)
        gui.typewrite(self.a)
        bot.moves(self)



bot1 = bot().game()