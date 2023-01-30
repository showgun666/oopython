import random
from .die import Die
class Hand:
    def __init__(self, dice_values=None):
        if dice_values is None:
            self.dice = [Die() for _ in range(5)]
        else:
            self.dice = [Die(value) for value in dice_values]

    def roll(self, indexes=None):
        if indexes is None:
            for die in self.dice:
                die.roll()
        else:
            for index in range(indexes):
                self.dice[index].roll()

    def __str__(self):
        return ", ".join(str(die) for die in self.dice)

