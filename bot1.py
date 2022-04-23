import os
import random
import pyautogui as gui


class bot:

    def __int__(self):

        self.lsy = [f"{_}" for _ in range(9)]
        self.used_sqares = []

    def open(self):
        os.startfile("C:\\Users\\bartosz.muszynski\\PycharmProjects\\tic_tac_toe\\game.py")


    def choice(self):
        self.a =  random.choice(["x","o"])
        if self.a == "x":
            self.b = "o"
        else:
            self.b = "x"
        return self.a, self.b




    def game (self):
        bot.open(self)
        bot.choice(self)

        mylist = [f"{_}" for _ in range(9)]
        a = random.sample(population=mylist, k=8)
        screenWidth, screenHeight = gui.size()
        gui.click()
        gui.typewrite(self.a)
        gui.press("enter")
        gui.typewrite(a[0])
        gui.press("enter")
        gui.typewrite(a[1])
        gui.press("enter")
        gui.typewrite(a[2])
        gui.press("enter")
        gui.typewrite(a[3])
        gui.press("enter")
        gui.typewrite(a[4])
        gui.press("enter")
        gui.typewrite(a[5])
        gui.press("enter")
        gui.typewrite(a[6])
        gui.press("enter")
        gui.typewrite(a[7])
        gui.press("enter")
        gui.typewrite(a[8])
        gui.press("enter")
        gui.typewrite(a[9])
        gui.press("enter")


bot1 = bot().game()