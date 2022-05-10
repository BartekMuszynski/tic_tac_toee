import random
from unittest import mock
from game import tictactoe
import unittest
mylist = [f"{_}" for _ in range(9)]
a = random.sample(population=mylist, k=9)
b = random.choice(["x", "o"])
a.insert(0,b)



class Test(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=a)
    def test_1(self,input):
        tictactoe().game()


if __name__ == "__main__":
    unittest.main